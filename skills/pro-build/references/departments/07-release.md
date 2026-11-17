# Stage 7: Release

**Model routing:** the production go in the main thread · `haiku` for the version bump, changelog and release notes · `sonnet` for the staging deploy, smoke tests and canary watch · `opus` for rollback decisions on unclear signals.

**Role:** release manager. Get changes to production safely, observably and reversibly.

## Steps

1. **Release candidate.** Everything merged to `main`; CI is green and stage 6 has passed for this release.
2. **Version and notes.** Semantic version, a changelog entry, and user-facing release notes in `docs/company/07-releases/<version>.md`.
3. **Staging.** Deploy to staging (`vercel:deployments-cicd`, `vercel:deploy` or `cloudflare:wrangler`), run the smoke tests (core flow, payment in test mode) and check Sentry for new errors.
3b. **Release diff** (if REA is installed): compare the previous and new build with `compare-application-versions` or `compare-artifacts` (`references/reverse-engineering.md`), to confirm that only the intended changes shipped. Note the result in the release notes.
4. **Rollback plan.** The previous good deployment, how to roll back (instant rollback or redeploy), and how to handle database migrations.
5. **Production, CEO gate.** Present the release summary, the risks and the rollback plan. **The user approves the production deploy.** The first production deploy and any production migration are done by the user or with their explicit go.
6. **Watch.** `ecc:canary-watch` for the first hour: error rate (Sentry), key events (PostHog) and uptime. Roll back on a clear regression and tell the user.
7. **Tag** the release in git after it is confirmed healthy.

## Gate: production go

- [ ] Smoke tests pass on staging
- [ ] A rollback plan is written
- [ ] The user said go
- [ ] There are no new error spikes after deploy (or a rollback was done and reported)
