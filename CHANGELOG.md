# Changelog

## 2.10.0 (2026-11-24)

**Payments by country, and App Store and Google Play rules.**
- New `references/payments.md`: pro-build **never assumes Stripe**. Kickoff asks where the business is registered, where the customers are and what is sold (a new critical coverage item when money moves). Stage 2 chooses: store in-app purchase for digital goods in mobile apps (never for physical goods or real-world services); Stripe only where it supports the seller's country; otherwise a merchant of record (Paddle, Polar) for digital products, a local provider for local customers, or PayPal; a foreign company only as the user's legal decision. It includes an **Israel** section (Stripe unavailable; local providers with Bit, Israeli cards, instalments and ILS) and the same safety rules for every provider (sandbox first, verified webhooks, no stored card numbers, going live is level C).
- New `references/app-stores.md`: developer accounts (personal or organization, D-U-N-S), Google's **12-tester, 14-day closed test** for new personal accounts, upload floors checked in November 2026 (**Xcode 26 and the iOS 26 SDK; target API 36, AAB, 16 KB pages**), the policies that shape the design (IAP versus physical goods, account deletion, Sign in with Apple, privacy labels and Data safety, user-generated content, quality), the submission package with review notes and a demo account, a pre-submission checklist, and the official sources to re-check before each submission.
- Wired into SKILL.md (rule 4), Kickoff, stages 2, 4, 6, 7, 8 and 9, the web and app playbooks, the toolkit, BUILD-STATE and the authorization matrix. Stripe-only wording was replaced with "the provider chosen in stage 2".
- Checker rules for the new guarantees, and scenarios **S31** (payments in Israel) and **S32** (store submission rules), both passing.

## 2.9.0 (2026-11-24)

**ECC in the same marketplace.**
- The pro-build marketplace now also lists **ECC**, installed from its official repository (`affaan-m/ECC`): `/plugin install ecc@pro-build`. One `/plugin marketplace add saeedkhoury/pro-build` gives you pro-build plus ECC's 72 agents, 328 skills and 99 commands, always at ECC's latest version, with its MIT license and credit. Nothing from ECC is copied into this repository, and its skills keep their `ecc:` names, so every pro-build reference keeps working. Tested in a clean config: both plugins install, and ECC's skills resolve.
- `references/toolkit.md` gives both ECC install paths and says to install only one.
- README: a Quick start that installs both plugins from one marketplace (with a warning not to install ECC twice), a "What's inside" table with built-in agent, skill and command counts, a step-by-step walkthrough, and an ECC-style banner.

## 2.8.0 (2026-11-23)

**Works with many AI agents.**
- pro-build is documented and packaged as a standard Agent Skill for **Claude Code, Codex, Kimi Code CLI, Gemini CLI, Grok Build, OpenCode and Cursor**: `npx skills add saeedkhoury/pro-build -a <agent>`, or `./install.sh <agent>` (claude, codex, kimi, gemini, grok, opencode, cursor), using each agent's documented skills folder.
- New `references/agents.md`: how to adapt the Claude Code mechanics in other agents (named skills → use if installed, else do the step directly; clickable questions → numbered options; model tiers → the agent's own cheap, default and strongest tiers; vendor plugins → MCP or CLI; independent review → a different model or provider). The process, gates and authorization rules stay identical, including in auto-approve modes. SKILL.md points non-Claude agents to it.
- `.codex-plugin/plugin.json` for Codex plugin packaging.
- README: a "Works with your AI agent" section with per-agent install, invocation, a capability comparison, and honest test status: **tested in Claude Code and Codex** (Codex loaded the skill from `.agents/skills`, ran Kickoff and wrote no files); the others are supported by the standard but not yet tested.

## 2.7.0 (2026-11-23)

- **Deep Kickoff interview:** rounds of 3–5 questions (typically 5–8 rounds, no fixed cap), a progress note after each round, probing vague answers, turning wishes into numbers, then risk, must-never-happen and speed/quality/cost questions. A **coverage checklist** requires that every critical item is answered by the user (never defaulted). A **fast lane** for "just start" asks only the critical items. A richer Project Brief, with type, out of scope, priorities, risks and coverage.
- **Project-type playbooks:** `references/project-types/web.md`, `system.md` and `app.md`, each with the shapes, the best default stack and decision rules, the tools for each stage, a quality bar (Core Web Vitals; contract tests and p95 latency; cold start and crash-free rate) and 12 type-specific Kickoff questions. Stage 2 picks the shape and stack from them; stage 6 checks their quality bars.
- **Rule 16:** ask before assuming at every stage.
- **Fast lane hardening:** critical items are asked as explicit questions, and are never pre-filled in a draft brief for blanket approval.
- **Decisions update the authoritative document** (brief, PRD, architecture or plan), and requirement-changing decisions, including those in BUILD-STATE → Decisions, invalidate dependent QA evidence.
- **System retry safety:** automatic retries only for reads, idempotent operations or writes the downstream deduplicates; bounded, with backoff and jitter; reconciliation for ambiguous writes; idempotent webhook and job processing.
- **App release branches:** mobile, **desktop** (a new stage 7 desktop path: per-OS channel table, Developer ID and notarization for direct macOS downloads, Mac App Store and Microsoft Store channels, signed update bundles, verifying a real update, user-run publication, halt per channel) and PWA (the web path).
- **QA mapping:** every type quality-bar item maps to one stage 6 check and inherits its waiver rules (app privacy and store items under non-waivable check 11 for Major).
- **Evals:** the runner supports **multi-turn** scenarios (` >> `, continued with `--resume`), and setup `none` is now an empty folder. S01 and S24–S27 are first-turn only; new multi-turn S28 (a completed deep interview) and S30 (incomplete: must stay at Kickoff); S29 refuses defaults for critical items. Checker rules for the coverage checklist, critical items, the playbooks and the pre-fill ban.
- **Reviewed by Codex** (GPT-6 Astra) in a fresh session: 4 rounds, 9 findings fixed, then APPROVED.

## 2.6.0 (2026-11-23)

**DevOps depth** (`references/devops.md`), sized to each project:
- **Reliability targets:** 1–3 SLOs per product with error budgets and a policy for when the budget is spent (stage 2), reviewed weekly (stage 9).
- **DORA metrics:** each release appends a deploy-log row (stage 7); the weekly review computes deployment frequency, lead time, change failure rate and time to restore.
- **Infrastructure approach:** platform-managed (default), infrastructure as code (Terraform or Pulumi: remote locked state, plan on every PR, staging apply level B, production apply level C, drift checks), or containers (built once, scanned, promoted by digest; Kubernetes only when needed).
- **Always-on watching:** an external uptime monitor, scheduled read-only CI checks (smoke tests and drift, opening an issue on failure), and an optional daily read-only AI health report via `/schedule`.
- **On-call paging:** a SEV1 route (PagerDuty, incident.io, Opsgenie, Better Stack), user-run setup, and a test page.
- **New rule 15:** automation never changes production unattended. New authorization rows cover infrastructure as code, containers, scheduled jobs and paging.
- Evals: 3 new scenarios (S21 auto-rollback job refused, S22 production Terraform apply is level C, S23 DORA and SLO review from a deploy log) and new checker rules.

## 2.5.1 (2026-11-23)

Evals only; the skill itself is unchanged.
- **Realistic fixtures** (`evals/fixtures/`): an approved SaaS at stage 5, a client site after stage 1, and an Expo app at stage 7. Scenarios opt in with `fixture:<name>`, and the runner copies the fixture into the isolated workspace.
- S02, S13, S14 and S15 now use fixtures, so they test the deeper behaviour: the compact stage 2 with analytics N/A, payment and security model routing, the mobile build-first and sandbox-only testing path, and resuming a real backlog. All 20 scenarios have been run and pass.

## 2.5.0 (2026-11-23)

Fixes from an independent Codex (GPT-6 Astra) review of v2.4.0: 9 findings plus a mobile gap, all accepted.

- **Authorization matrix** (`references/authorization.md`): levels A, B and C for every action, which win over the playbooks. It fixes contradictions about first deploys, migrations, publishing and rollback.
- **Production protection:** merges deploy to staging only; production changes only by promoting a named staging build. Gate 4 verifies it.
- **Release-bound evidence:** release candidates record the commit SHA and build ID; any merge invalidates them. Release classes (Major, Minor, Patch, Hotfix) each map to a QA profile.
- **Required-evidence QA:** each check is pass, fail, blocked or N/A (with an accepted reason). A missing required check blocks the release, and "no findings" isn't a pass.
- **The Client site track now runs a compact stage 2,** so stage 5 always has an approved M1 plan.
- **Service applicability:** stage 2 records chosen, alternative or N/A for each capability, and gate 4 checks exactly that. Optional services are truly optional.
- **Real secret scanning** (gitleaks, trufflehog or Semgrep secrets) of the history and build output, with redacted findings and user-run rotation.
- **Backups and incidents:** recovery objectives (RPO and RTO), automated backups, restore tests every 90 days, and an incident runbook with severities and alert routes. Weekly reviews check them.
- **Mobile release path:** signing, TestFlight or Play internal track, user-run store submission, phased rollout, backend compatibility.
- **Skill evals:** `evals/check.py` (structural and contradiction checks, run in CI), 20 behavioural scenarios and an **isolated** runner. The runner loads only this checkout as a plugin, uses no MCP servers and read-only tools, and records the version and content hash it tested.

Round 2 of the review (9 more findings, all accepted):
- **Release ordering and records:** release content merges before the candidate is frozen. A single invalidation policy (stage 7): release records (`BUILD-STATE.md`, the QA report, release notes, reviews) don't invalidate a candidate; requirement and decision docs (PRD, architecture, ADRs, plan) invalidate the dependent evidence; code and configuration changes invalidate everything.
- **No live effects in testing:** with build-time configuration, mutating tests run on a sandbox build of the same SHA, and the production-configured candidate gets only non-mutating checks. Store sandbox accounts isolate only payments, not the app's backend.
- **Configuration strategy:** runtime configuration promotes the staging artifact; build-time configuration builds and tests a production-configured candidate. Evidence is bound to the SHA, artifact and configuration profile.
- **Mobile:** builds and signs before QA, so the exact tested binaries are submitted; a phased-rollout halt replaces rollback.
- **First launch:** a halt plan (maintenance page, disabling the alias) replaces the non-existent rollback target.
- **QA:** an explicit "accepted risk" status, with eligible and never-eligible checks, scope, owner and expiry.
- **Service applicability is authoritative** in stages 1, 5, 8 and 9 (no hidden PostHog or Sentry requirement).
- **Approvals** come only from the user's words in the conversation; scenario S17 tests that file-only approvals are rejected.

## 2.4.0 (2026-11-17)

- **REA (Reverse Engineer Anything) integration**, optional with fallbacks:
  - **Stage 0:** competitor teardowns of public web apps and installed apps (understand, never copy).
  - **Stage 6:** a release exposure audit of your own production build. An exposed `text.credential_markers` or `javascript.source_map_sources` check blocks launch.
  - **Stage 7:** a release diff with `compare-application-versions` or `compare-artifacts`.
  - **Existing project track:** recovering understanding when the source is missing.
- Clear analysis rules: own, authorised or legitimately obtained public targets only; no copying; no bypassing DRM, licences, auth or paywalls. Details are in `references/reverse-engineering.md`.

## 2.3.0 (2026-11-17)

- **GitHub spec-kit integration:** an optional spec-kit mode for large features. Stage 4 runs `specify init --integration claude` and writes the constitution from `CLAUDE.md`; stage 5 runs specify → clarify → plan → tasks → analyze → implement → converge inside pro-build's branch, review and approval gates. See `references/spec-kit.md`.
- **Consistency check (always on):** stage 2 traces every PRD requirement to plan tasks and back, checks entities and terms across documents, and adds a Traceability table to `02-plan.md` before the gate.
- **Convergence check (always on):** stage 5 compares the code with every milestone requirement, adds missing work as tasks, and repeats until the milestone is "✅ converged" before the demo.
- `BUILD-STATE.md` records `Spec mode: native | spec-kit`.

## 2.2.0 (2026-11-17)

- **Smart model routing:** the main thread talks with you and runs the gates; self-contained work goes to helper agents on Haiku (mechanical), Sonnet (building, the default) or Opus (strategy, architecture, security), with Fable as an opt-in top tier that is off by default because it may use credits. It escalates one tier on failure, never goes below Sonnet for payments, auth or security, and only delegates when it pays off. Each department playbook has its own routing line; the full table is in `references/model-routing.md`.
- **CEO briefings:** every gate is a one-minute briefing (decision, artifacts, numbers, risks, recommendation, options).
- **SEO throughout:** site architecture in Design, technical SEO in the scaffold, SEO and AI-search checks in QA, and a content and ranking engine in Go-to-Market. Optional claude-seo integration.
- Kickoff now sets the model policy (main-session model, Fable on or off), and `BUILD-STATE.md` tracks it in a model log.

## 2.1.0 (2026-11-17)

- **Kickoff for every project:** an adaptive discovery interview (2–4 questions per round, with clickable options), a Project Brief the user must approve, and a track recommendation based on the brief. Previously the Product track skipped all questions.
- **Implementation plan:** stage 2 now writes `docs/company/02-plan.md` with milestones (M1 = MVP), tasks, acceptance criteria and a definition of done. Stage 5 builds M1 first and demos it.
- **Project kit:** every project gets `CLAUDE.md` (rules for future AI sessions), `README.md`, `.env.example`, a docs index and a roadmap file. The full list is in `references/project-kit.md`.

## 2.0.0 (2026-11-17)

**pro-build becomes an AI software company.**

- Ten departments, each with its own playbook and approval gate: Founder Office, Product, Engineering Leadership, Design, Platform/DevOps, Engineering, QA & Security, Release, Go-to-Market, Operate & Grow.
- Four tracks to size the process: Startup, Product, Client site and Existing project.
- New stages: idea validation with a go/no-go decision, a CI/CD and environments setup, staged releases with rollback plans and canary monitoring, go-to-market with live-payment checklists, and weekly operating reviews.
- Integrations with official vendor plugins: Stripe, Supabase, Vercel, Sentry, PostHog, Semgrep, plus marketingskills and taste-skill.
- CEO-only actions: live payments, production deploys, purchases, publishing and sign-ins always stay with the user.
- New commands: `status`, `stage=`, `feature`, `release`, `launch` and `review`.
- `BUILD-STATE.md` now tracks gates, services, metrics and risks.

## 1.0.0 (2026-11-17)

- First release: the five-phase workflow (Define, Design, Foundation, Features, Launch), approval gates, `BUILD-STATE.md` progress tracking, and the plugin marketplace manifest.
