# DevOps depth: reliability targets, delivery metrics, infrastructure, watching and paging

This playbook deepens stages 2, 4, 7 and 9. Size it to the project: a client site needs only an uptime monitor and DORA tracking; a SaaS with paying users needs everything. Record each choice in stage 2's **operations profile**. All actions follow `references/authorization.md`.

**The golden rule: automation may watch, report and page, but it never changes production unattended.** Scheduled jobs and agents are read-only. Fixing production always goes through a person: a hotfix release (stage 7), a pre-authorized rollback during a release watch, or a level C action by the user.

## 1. Reliability targets (SLOs): stage 2

For each user-facing journey that matters (for example, "the booking page loads", "checkout succeeds"):

| Field | Example |
|:--|:--|
| **SLI** (what's measured) | Share of `/book` requests answered with a 2xx in under 1s |
| **SLO** (target over 28 days) | 99.5% |
| **Error budget** | **In the SLI's own units:** allowed bad requests = eligible requests × (1 − 0.995). With 200,000 requests in 28 days, that's 1,000 bad requests |
| **Data source** | Uptime monitor, Sentry, hosting analytics, or Datadog or Grafana if chosen |
| **Policy when the budget is spent** | Freeze feature releases; the next cycle is reliability work (stage 9 decides) |

Rules for the budget:
- **Keep the budget in the SLI's units.** A request-based SLI has a budget of bad requests, not minutes; an outage at peak traffic burns it much faster than one at night. Only a **time-based** SLI (for example, "minutes the uptime check passed") has a budget in minutes: 99.5% over 28 days allows about 3.4 hours of failed checks.
- **Remaining budget** = 1 − (bad events so far ÷ allowed bad events), for the window so far.
- **Missing data** (a monitor outage, a gap in logs) is reported as **unknown coverage** with its duration. It's never counted as good.

Start with 1–3 SLOs and modest targets (99.0–99.5%). Write them in `02-architecture.md` → Operations profile.

## 2. Delivery metrics (DORA): stages 7 and 9

**Recording lifecycle (web, server and mobile):**
- **Every production exposure gets a deploy-log row,** with a stable ID (`D-001`, …): version, release SHA, the **included changes** (each pull request number and merge time), production exposure time, class and outcome. For web and server, exposure is the promotion. For mobile, it's the start of the phased rollout, one row per platform.
- **Outcomes** are healthy, rolled back, halted (a mobile rollout paused, or a first-launch halt), hotfixed, or failed (incident `I-…`). Keep failed and halted rows; never delete them.
- **Incidents** get a stable ID (`I-001`, …) in the incident log, with a **"caused by deployment"** link (a `D-…` ID, or "not deploy-related").
- **Updating later:** when an incident or hotfix is traced to an earlier deployment, the post-incident review (runbook, stage 4) changes that deployment's outcome to failed (`I-…`) or hotfixed. The weekly review reconciles anything missed.

Stage 9 computes:

| Metric | How | Healthy for a small team |
|:--|:--|:--|
| Deployment frequency | Production deploys per week | Weekly or more |
| Lead time for changes | Median, over **every pull request** deployed in the period (features, fixes and hotfixes), of the time from its merge to the production exposure that shipped it | Less than a week |
| Change failure rate | Share of deployments whose outcome is rolled back, halted for a defect, hotfixed or failed (`I-…`) | Under 15% |
| Time to restore | Median time from incident start to recovery, over incidents in the period | Less than a day |

These are signals, not targets to game. Use them to find the slowest part of the release flow.

## 3. Infrastructure approach: stage 2 decides, stage 4 builds

| Approach | When | How |
|:--|:--|:--|
| **Platform-managed** (default) | Vercel, Cloudflare, Supabase or Netlify cover the needs | Configure through their tools; document every setting in `04-platform.md` so it can be redone |
| **Infrastructure as code** | Several environments, cloud resources (AWS, GCP, Azure), teams, or compliance needs | Terraform (the official `terraform` plugin: `/plugin install terraform@claude-plugins-official`) or Pulumi, in `infra/`. State in a remote, locked backend (never committed). Separate state per environment |
| **Containers** | Long-running services, background workers, or a stack the platforms don't host | Docker (`ecc:docker-patterns`) for every service; Kubernetes (`ecc:kubernetes-patterns`) only when one host isn't enough. Images are tagged by commit SHA and promoted by **digest** |

**Infrastructure-as-code workflow:**
- `fmt`, `validate` and a security scan (for example `tfsec` or `checkov`) run in CI.
- Every pull request posts a `plan` for review.
- **Apply:** staging is level B (an explicit yes for that plan); production is level C (the user applies it, or approves the exact reviewed plan, which applies through a protected pipeline).
- Destroy and replace actions on stateful resources (databases, buckets) are always flagged in the CEO briefing.
- Drift detection: a scheduled `plan` that reports any difference, and never applies.

**Container workflow** (follows stage 7's configuration strategy):
- Images are built in CI, scanned (for example `trivy`), and pushed with the commit SHA tag. The release candidate's artifact ID (stage 7) is an **image digest**.
- **Runtime configuration:** one image per SHA. Staging runs that digest; production gets the **same digest** with production environment settings (level B, or C for the first deploy).
- **Build-time configuration** (for example Next.js `NEXT_PUBLIC_*` baked into the image): **two images from the same SHA**, a sandbox digest and a production-configured digest. Mutating tests run on the sandbox digest; the production digest gets only the non-mutating checks. Production deploys the **verified production digest**, never a rebuild, and never the sandbox digest.
- Every service has health checks, resource limits and rolling or blue-green updates.
- Secrets come from the platform's secret manager, never baked into images.

## 4. Always-on watching: stage 4 sets it up

Three layers, from the most to the least essential:

1. **External uptime monitor** (always, for anything public): Better Stack, UptimeRobot, Checkly or similar, checking the main URLs and a `/health` endpoint every 1–5 minutes and alerting the incident owner. The user creates the account (level C); the agent prepares the checks.
2. **Scheduled checks in CI** (recommended): a scheduled GitHub Actions workflow (daily, or every few hours) that runs read-only smoke tests against production (pages load, GET `/health`, no writes) and an infrastructure drift `plan`. Its permissions are split:
   - **Checking:** read-only credentials for production and infrastructure.
   - **Reporting only:** `issues: write` on this repository, plus the one approved alert destination (a webhook or the paging integration's event key).
   - Nothing else: no `contents: write`, no deploy or cloud write credentials.
   On failure it opens an issue and sends the alert.
3. **A scheduled AI watch** (optional): a Claude Code routine (`/schedule`) that reads errors, uptime and analytics once a day and writes a short health report (new errors, SLO burn, unusual metrics, overdue backups or restore tests). It's read-only by construction: no deploy or write tools. Its only output is the report to the user, through its routine's normal result or the one approved alert destination. It may suggest a hotfix, but never acts. Creating the routine is level B; any credentials it needs are read-only.

Record each layer as set up, not set up, or N/A in `04-platform.md`.

## 5. On-call and paging: stages 2 and 4

- **Route:** SEV1 pages the incident owner (PagerDuty, incident.io, Opsgenie or Better Stack phone alerts); SEV2 goes to chat or email within the hour; SEV3 waits for the weekly review. The official `pagerduty` and `incident-io` plugins can read incidents and on-call schedules once the user signs in.
- **Setup is level C** (accounts, phone numbers, escalation policies). The agent prepares the configuration, and the user sends a **test page** that reaches them.
- **Solo founders:** one person is on call. Keep SEV1 paging to "the product is down or data is at risk", so alerts stay meaningful.
- Every page links to the runbook in `04-platform.md`.

## 6. Weekly review additions: stage 9

- **SLOs:** the error budget remaining for each SLO. If a budget is spent, recommend a reliability-focused cycle (the user decides).
- **DORA:** the four metrics from the deploy log, compared with last month, plus one suggestion for the slowest part.
- **Watch layers:** uptime incidents, failed scheduled checks, drift reports and AI health reports since the last review.
- **On-call:** the pages received, false alarms to tune, and whether the test page still works (every 90 days).
