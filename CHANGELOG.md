# Changelog

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
