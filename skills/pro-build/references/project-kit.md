# Project kit: the files every project gets

pro-build produces these files over the stages. Each one is created by the stage shown, kept up to date by later stages, and listed in `docs/README.md`.

| File | Created in | Purpose |
|:--|:--|:--|
| `BUILD-STATE.md` | Kickoff | The company's memory: track, stage, gates, backlog, services, metrics, risks |
| `docs/README.md` | Kickoff | An index of every project document, with one line about each |
| `docs/company/00-brief.md` | Kickoff | The approved Project Brief |
| `docs/company/00-validation.md` | 0 Founder Office | Market, competitors, pricing, go/no-go (Startup track) |
| `docs/company/01-prd.md` | 1 Product | Product Requirements Document: users, flows, requirements, acceptance criteria, metrics |
| `docs/company/01-roadmap.md` | 1 Product | Now / Next / Later roadmap |
| `docs/company/02-architecture.md` | 2 Eng Leadership | Stack, system diagram, data model, API, auth, environments, costs |
| `docs/company/adr/NNNN-<title>.md` | 2 Eng Leadership | One architecture decision record per major decision |
| `docs/company/02-plan.md` | 2 Eng Leadership | Implementation plan: milestones (M1 = MVP), tasks, dependencies, risks, definition of done |
| `docs/company/02-plan.md` → Traceability | 2 Eng Leadership | Requirement → task mapping from the consistency check |
| `docs/company/03-design/` | 3 Design | Direction, tokens, components, key screens |
| `CLAUDE.md` | 4 Platform | Project rules for AI agents: stack, commands, conventions, where docs live, what not to touch |
| `README.md` | 4 Platform | What the project is, how to run, test and deploy it |
| `.env.example` | 4 Platform | Every environment variable by name, with no values |
| `.github/workflows/ci.yml` | 4 Platform | Lint, type-check, test, build and security scan on every pull request |
| `.github/pull_request_template.md` | 4 Platform | Summary, test plan and screenshots checklist |
| `.specify/`, `.claude/skills/speckit-*` | 4 Platform (spec-kit mode only) | spec-kit setup and constitution |
| `specs/NNN-<feature>/` | 5 Engineering (spec-kit mode only) | `spec.md`, `plan.md` and `tasks.md` for each large feature |
| `docs/company/04-platform.md` | 4 Platform | Environments, services, secrets map (names only), deploy and rollback runbook |
| `docs/company/06-launch-readiness.md` | 6 QA & Security | Check results and findings |
| `docs/company/07-releases/<version>.md` | 7 Release | Release notes and rollback plan |
| `CHANGELOG.md` | 7 Release | User-facing change history |
| `docs/company/08-gtm.md` | 8 Go-to-Market | Positioning, pricing, funnel, launch plan, live-payments checklist |
| `docs/company/09-reviews/<date>.md` | 9 Operate & Grow | Weekly operating reviews |
| `PRIVACY.md`, `TERMS.md` (drafts) | 6 QA & Security | Policy drafts for the user to review, when personal data or payments are involved |

Tracks that skip a stage skip its files. Say which ones.
