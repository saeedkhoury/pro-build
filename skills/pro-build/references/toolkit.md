# Toolkit

Every tool pro-build uses, by department. If a skill is missing, give the user its install line and continue with a fallback (operating rule 7).

## Required

| Tool | Used in | Install (inside Claude Code) |
|:--|:--|:--|
| ECC: Everything Claude Code | Every stage | `/plugin install ecc@pro-build` (from the pro-build marketplace), or `/plugin marketplace add affaan-m/ECC` then `/plugin install ecc@ecc`. Install only one of the two |
| Git and the GitHub CLI (`gh`) | 4–9 | `brew install git gh`, then `gh auth login` (the user signs in) |

## Recommended: company services (official Claude plugin directory)

These plugins connect to hosted services; each needs the user to sign in once (run `/mcp` in Claude Code). Install with `/plugin install <name>@claude-plugins-official`.

| Plugin | Department | What it does | Account |
|:--|:--|:--|:--|
| `stripe` | 4, 8, 9 | Payments, subscriptions, billing best practices, **only where Stripe supports the business's country** | The provider chosen with `references/payments.md` (Paddle, Polar, a local provider, PayPal), through its official docs and SDK, in test mode |
| `supabase` | 2, 4 | Postgres, auth, storage, row-level security | Supabase |
| `vercel` | 4, 7 | Deploys, previews, environments, Next.js | Vercel |
| `sentry` | 4, 5, 7, 9 | Error monitoring, releases, alerts | Sentry |
| `posthog` | 1, 4, 8, 9 | Product analytics, funnels, feature flags, experiments | PostHog |
| `semgrep` | 4, 6 | Security scanning while coding | Semgrep (free login) |
| `figma` | 3 | Design files and handoff (optional) | Figma |
| `cloudflare` | 4, 7 | Alternative hosting: Workers, Pages, R2, D1 | Cloudflare |

## Recommended: community skills

| Plugin | Department | Install |
|:--|:--|:--|
| marketingskills (53 growth skills) | 0, 8, 9 | `/plugin marketplace add coreyhaines31/marketingskills` then `/plugin install marketing-skills@marketingskills` |
| taste-skill (design taste) | 3 | `/plugin marketplace add Leonxlnx/taste-skill` then `/plugin install taste-skill@taste-skill` |
| claude-seo (SEO suite: audits, technical, local, clusters, AI search) | 4, 6, 8 | `/plugin marketplace add AgriciDaniel/claude-seo` then `/plugin install claude-seo@agricidaniel-claude-seo` |
| spec-kit (spec-driven mode for large features) | 4, 5 | Not a plugin: `uv tool install specify-cli` in the terminal, then pro-build runs `specify init` in the project during stage 4 |
| REA: reverse engineer anything (competitor teardown, release exposure audit, release diff, lost source) | 0, 6, 7, Existing | `/plugin marketplace add morluto/rea` then `/plugin install rea@rea` (needs Node 22.23.4+). Rules and commands: `references/reverse-engineering.md` |
| Secret scanner: gitleaks, trufflehog, or Semgrep secrets | 4, 6 | `brew install gitleaks` or `brew install trufflehog`, or the semgrep plugin (free login). Ask before installing a new tool |
| Mobile release: EAS (Expo) or fastlane | 7 | `npm i -g eas-cli` or `brew install fastlane`; store accounts are level C |
| Terraform (infrastructure as code) | 2, 4, 7 | `/plugin install terraform@claude-plugins-official`; or Pulumi. See `references/devops.md` §3 |
| PagerDuty or incident.io (paging and on-call) | 4, 9 | `/plugin install pagerduty@claude-plugins-official` or `incident-io@claude-plugins-official`; accounts are level C |
| Datadog or Grafana (observability, optional) | 4, 9 | `/plugin install datadog@claude-plugins-official` or `grafana-cloud-mcp@claude-plugins-official` |
| Uptime monitor (Better Stack, UptimeRobot, Checkly) | 4, 9 | A web account (level C); no plugin needed |
| claudex-loop (cross-model plan review) | 2, 5 | `/plugin marketplace add chaseai-yt/claudex-loop` then `/plugin install claudex-loop@claudex-loop` (also needs the Codex CLI) |

## Fallbacks

| Missing | Do instead |
|:--|:--|
| claudex-loop or Codex | `ecc:council` or `ecc:santa-loop` for the independent review |
| taste-skill | `ecc:frontend-design-direction` alone, plus a strict "no generic AI look" self-check |
| marketingskills | `ecc:seo`, `ecc:brand-voice`, `ecc:content-engine` and `ecc:market-research` |
| claude-seo | `ecc:seo` and the marketingskills SEO skills |
| REA | Manual build-output checks (`*.map`, secret patterns) plus `ecc:security-scan`; public information only for competitors |
| spec-kit | Native mode: the stage 2 consistency check and the stage 5 convergence check |
| Fable off or unavailable | `opus` (see `references/model-routing.md`) |
| Vercel | Cloudflare (`cloudflare:wrangler`), or document a manual deploy |
| Supabase | Postgres via `ecc:postgres-patterns` and `ecc:database-migrations` |
| PostHog or Sentry not wanted | Record an alternative (for example Plausible, GlitchTip, Better Stack) or N/A with a reason in stage 2's service applicability table; the stage 4 gate then checks that instead |
| PostHog or Sentry wanted but not signed in yet | Add the SDKs with environment-variable placeholders; mark the check "blocked: sign-in needed" until the user signs in |

## Telemetry notes

Some vendor plugins send anonymous usage data by default; none send prompts or file contents:

- **Vercel:** daily ping plus Vercel skill names. Turn off with `VERCEL_PLUGIN_TELEMETRY=off`.
- **Semgrep:** hook timings and scanned file types. Turn off with `DO_NOT_TRACK=1`.
- **PostHog:** session analytics are off unless `POSTHOG_LLMA_CC_ENABLED=true` is set.
- **Stripe:** reports Stripe skill names through the Stripe CLI, if it is installed.
