# Spec-kit mode: large features with GitHub spec-kit

[spec-kit](https://github.com/github/spec-kit) is GitHub's spec-driven development toolkit. pro-build uses it as an **optional per-feature mode** for large features. Company-level documents (brief, PRD, architecture, plan) stay in `docs/company/`; spec-kit adds a detailed spec, plan and task list for each large feature, plus a built-in loop that confirms the code matches the spec.

## When to use it

- `BUILD-STATE.md` says `Spec mode: spec-kit`, **and**
- the feature is large: several components, multiple days of work, or requirements that are still unclear.

Small features, fixes and refactors always use the normal stage 5 cycle.

## One-time setup (stage 4)

1. Check that it's installed: `command -v specify`. If it isn't, the user can install it with `uv tool install specify-cli` (needs Python 3.11+ and uv); otherwise, stay in native mode.
2. With the user's approval, and with a clean `git status`, run:
   `specify init --here --integration claude --script sh --non-interactive --force`
   This adds `.specify/` (templates, scripts, constitution) and nine project skills in `.claude/skills/speckit-*`. It doesn't switch git branches.
3. Write the constitution: run `/speckit-constitution`, giving it the principles from `CLAUDE.md` and pro-build's operating rules (test-first, pull requests only, secrets in environment variables, accessibility, security review for auth and payments).
4. Commit `.specify/` and `.claude/skills/speckit-*`. Record `Spec mode: spec-kit` in `BUILD-STATE.md`.
5. New skills load in a **new session**. Tell the user to restart Claude Code after setup.

## The feature flow

pro-build owns the branch and the gate; spec-kit owns the feature documents. Each feature's documents go in `specs/NNN-<name>/` (`spec.md`, `plan.md`, `tasks.md`).

| Step | Command | pro-build guidance | Model |
|:--|:--|:--|:--|
| 0 | `git switch -c feat/<name>` | One branch per feature (operating rule 5) | main thread |
| 1 | `/speckit-specify <feature>` | Feed it the PRD section and acceptance criteria for this feature. Never contradict the PRD | main thread |
| 2 | `/speckit-clarify` | Up to 5 targeted questions. The user answers in the main thread | main thread |
| 3 | `/speckit-plan <stack notes>` | It must follow `02-architecture.md` and the ADRs. If it needs a new decision, write a new ADR | opus |
| 4 | `/speckit-checklist` (optional) | For features touching auth, payments or personal data | sonnet |
| 5 | `/speckit-tasks` | Tasks ordered by dependency, each small enough to review | sonnet |
| 6 | `/speckit-analyze` | A consistency check across spec, plan and tasks. Fix every critical finding before implementing | opus |
| 7 | `/speckit-implement` | Test-first, following the constitution. Delegate to a `sonnet` subagent for long task lists | sonnet |
| 8 | `/speckit-converge` | Repeat implement → converge until it reports **"✅ Converged"** | sonnet |
| 9 | Pull request → `ecc:code-review` → user approves the merge | The normal stage 5 gate. Mark the feature done in `BUILD-STATE.md` with a link to `specs/NNN-<name>/` | main thread |

## Rules

- **The PRD wins.** If the spec-kit spec and the PRD disagree, stop and ask the user. Then update one of them so they match.
- **The architecture wins.** `/speckit-plan` can't silently change the stack, data model or hosting; that needs an ADR and the user's OK.
- **The gates still apply.** Converging is not merging. CI, review and the user's approval are still required.
- **Fallback.** If spec-kit isn't installed or its skills haven't loaded, run the same steps natively: a mini-spec, the plan and tasks in the pull-request description, the consistency check from stage 2, and the convergence check from stage 5.
