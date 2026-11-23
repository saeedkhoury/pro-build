# Stage 5: Engineering

**Model routing:** merge approvals and the MVP demo in the main thread · `sonnet` runs each feature or fix cycle · `haiku` for codebase search, lint and build fixes, fixtures · `opus` for hard bugs after one failed attempt and reviews of risky pull requests.

**Role:** the engineering team. Ship the backlog in small, tested, reviewed increments.

## First pass: the MVP foundation

Build **milestone M1** from `docs/company/02-plan.md`. Use `ecc:orch-build-mvp` with the PRD, architecture, plan and design system, on a feature branch, opening a pull request to `main`. Before the demo, run a **convergence check** (like spec-kit's `converge`): compare the code with every M1 requirement and acceptance criterion in the PRD and `02-plan.md`. Add anything unbuilt, partly built or wrong as new M1 tasks, build them, and repeat until nothing remains. Then report **"✅ M1 converged"** with the evidence. Use `sonnet` for the check, and `opus` if it's disputed or unclear.

When M1 is merged and converged, show the user the running MVP (a preview URL, or local run steps) and confirm before moving on to M2 and the backlog. Run the same convergence check at the end of every milestone.

## Each cycle: one backlog item, one branch, one pull request

| Work | Workflow |
|:--|:--|
| New feature | `ecc:orch-add-feature` |
| Change to existing behaviour | `ecc:orch-change-feature` |
| Bug | `ecc:orch-fix-defect` |
| Refactor | `ecc:orch-refine-code` |
| Broken build | `ecc:build-fix` |
| Production error | `sentry:sentry-debug-issue` (or the chosen alternative), then `ecc:orch-fix-defect`. If it's urgent, ship it as a **Hotfix** release (stage 7) and follow the incident runbook (stage 4) |

**Large features: spec-kit mode.** If `BUILD-STATE.md` says `Spec mode: spec-kit`, then any feature that is large (several components, multiple days of work, or unclear requirements) follows `references/spec-kit.md` instead of the cycle below: specify → clarify → plan → tasks → analyze → implement → converge, then the same pull-request and merge steps. Small features and fixes always use the normal cycle.

For each cycle:

1. Pick the next task from the current milestone in `02-plan.md` (or the top of the backlog), then restate its acceptance criteria.
2. Branch `feat/<slug>` or `fix/<slug>`.
3. Run the workflow: tests first, then implementation, then review.
4. **If analytics applies** (stage 2's table): add the feature's analytics events with the chosen tool (PostHog by default), and a feature flag for risky features (`posthog:instrument-feature-flags` or the alternative). If analytics is N/A, skip this step and say so.
5. Open a pull request with a summary, a test plan and screenshots for UI changes. CI must pass.
6. Run `ecc:code-review`. For large or risky changes, also run `ecc:santa-loop` or `claudex-loop:codex-review`.
7. **Merge (level B):** ask "Merge PR #<n>?" and merge only on an explicit yes for that pull request; log it in `BUILD-STATE.md` → Approvals. The merge deploys to **staging only**. Mark the item done. A merge that changes code or configuration invalidates any open release candidate (stage 7's invalidation policy).

One feature per session. Offer `ecc:save-session` at the end.

## Gate: per feature

- [ ] Acceptance criteria are met and shown (tests, screenshots or a preview URL)
- [ ] CI is green and review findings are resolved
- [ ] Analytics events exist for the feature's metric, if analytics applies (stage 2's table); otherwise N/A
- [ ] The user explicitly approved merging this pull request (level B, logged); it deployed to staging only
