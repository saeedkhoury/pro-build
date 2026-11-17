# Stage 5: Engineering

**Role:** the engineering team. Ship the backlog in small, tested, reviewed increments.

## First pass: the MVP foundation

Build **milestone M1** from `docs/company/02-plan.md`. Use `ecc:orch-build-mvp` with the PRD, architecture, plan and design system, on a feature branch, opening a pull request to `main`. When M1 is merged, show the user the running MVP (a preview URL, or local run steps) and confirm before moving on to M2 and the backlog.

## Each cycle: one backlog item, one branch, one pull request

| Work | Workflow |
|:--|:--|
| New feature | `ecc:orch-add-feature` |
| Change to existing behaviour | `ecc:orch-change-feature` |
| Bug | `ecc:orch-fix-defect` |
| Refactor | `ecc:orch-refine-code` |
| Broken build | `ecc:build-fix` |
| Production error | `sentry:sentry-debug-issue`, then `ecc:orch-fix-defect` |

For each cycle:

1. Pick the next task from the current milestone in `02-plan.md` (or the top of the backlog), then restate its acceptance criteria.
2. Branch `feat/<slug>` or `fix/<slug>`.
3. Run the workflow: tests first, then implementation, then review.
4. Add analytics events and a feature flag (`posthog:instrument-feature-flags`) for risky features.
5. Open a pull request with a summary, a test plan and screenshots for UI changes. CI must pass.
6. Run `ecc:code-review`. For large or risky changes, also run `ecc:santa-loop` or `claudex-loop:codex-review`.
7. The user approves the merge. Mark the item done in `BUILD-STATE.md`.

One feature per session. Offer `ecc:save-session` at the end.

## Gate: per feature

- [ ] Acceptance criteria are met and shown (tests, screenshots or a preview URL)
- [ ] CI is green and review findings are resolved
- [ ] Analytics events exist for the feature's metric
- [ ] The user approves the merge
