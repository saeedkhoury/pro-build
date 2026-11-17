# Changelog

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
