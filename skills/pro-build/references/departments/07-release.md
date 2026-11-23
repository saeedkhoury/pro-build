# Stage 7: Release

**Model routing:** the production go in the main thread · `haiku` for the version bump, changelog and release notes · `sonnet` for the staging deploy, smoke tests and canary watch · `opus` for rollback decisions on unclear signals.

**Role:** release manager. Get **one exact, verified artifact with production configuration** to production safely, observably and reversibly. All actions follow `references/authorization.md`.

## Release classes

Choose the class at step 1 and record it. It decides which stage 6 evidence is required (see the profiles in `06-qa-security.md`).

| Class | When | Stage 6 profile |
|:--|:--|:--|
| **Major** | First launch, new product area, auth or payment changes, data-model or migration changes, new external integrations | Full |
| **Minor** | New features without auth, payment or data-model changes | Standard |
| **Patch** | Bug fixes and copy or styling changes with no new behaviour | Light |
| **Hotfix** | An urgent production fix | Light now, the missing Standard checks within 48 hours (tracked in `BUILD-STATE.md`) |

## Invalidation policy (shared by stages 5, 6 and 7)

This is the single rule for when release evidence stops counting. Stages 5 and 6 refer to it.

| Change after the candidate is frozen | Effect |
|:--|:--|
| **Release records only:** `BUILD-STATE.md`, `docs/company/06-launch-readiness.md`, `docs/company/07-releases/**`, `docs/company/09-reviews/**` | **No effect.** These are bookkeeping about the release, not part of what ships. Write them during the release and commit them afterwards in a docs-only pull request (`docs: record release v<version>`) |
| **Requirements or decisions:** the PRD, roadmap, architecture, ADRs, plan, service applicability or operations profile (`docs/company/01-*`, `02-*`, `adr/**`) | **Invalidates the evidence that depends on them.** Re-evaluate the affected checks against the new baseline, and freeze a new candidate if any code or configuration has to change |
| **Code, dependencies, build or deploy configuration, environment variables, feature-flag defaults** | **Invalidates** the candidate and its stage 6 evidence. Start again at step 1 |

The stage 6 report records the **requirements baseline** it tested against: the commit SHA of the latest change to `docs/company/01-*`, `02-*` and `adr/**`.

## Configuration strategy

Recorded in stage 2's operations profile and set up in stage 4:

- **Runtime configuration** (the environment is read when the app starts or serves a request): you can promote the exact staging artifact, and it picks up production settings. Stage 4 must have verified this once.
- **Build-time configuration** (values baked in at build time; for example `NEXT_PUBLIC_*` variables, mobile apps, static sites): you need **two builds of the same SHA**, and the evidence is split between them:
  - **Sandbox build** (test keys, staging backend): stage 6's **functional and mutating tests** run here: sign-up, payments in test mode, cancellation, data changes. Never run them against production services.
  - **Production-configured candidate** (built in a protected, non-public environment): **non-mutating verification only**:
    - the embedded configuration values are the production ones (API URL, live publishable key, analytics key);
    - read-only smoke checks (pages load, GET health and status endpoints, no sign-ups, writes or payments);
    - a diff against the sandbox build shows only configuration differences (`compare-artifacts` with REA, or a file diff).
  - Any check that would cause a **live effect** (a real payment, real records or emails) is **level C**: the user runs it after launch (for example, stage 8's real payment and refund).
  - Promote **the production-configured candidate**, and bind both sets of evidence to the same SHA. Never assume a staging build can be promoted unchanged.

## Steps

1. **Release content first.** On a release branch, bump the version, add the `CHANGELOG.md` entry, and write user-facing notes in `docs/company/07-releases/<version>.md`. Open a pull request and merge it (level B). Now `main` holds everything that will ship.
2. **Build and freeze the candidate.** Build it from that `main` SHA, following the configuration strategy. Record it in `BUILD-STATE.md` → Release candidate:
   - the version and class;
   - the **commit SHA**;
   - the **artifact or build ID** (a deployment ID, image digest or file checksum);
   - the **configuration profile** (runtime, or build-time production);
   - the merged pull requests.

   Later changes are handled by the **invalidation policy** above.
3. **Evidence check.** `06-launch-readiness.md` must name the **same SHA, artifact and configuration profile**, and pass the profile for this class. If it doesn't, run stage 6 on this candidate first.
4. **Candidate verification.**
   - **Runtime configuration:** on staging, run the smoke tests (core flow, plus payment in test mode where it applies) on the artifact that will be promoted.
   - **Build-time configuration:** smoke tests with mutations run on the **sandbox build**; the **production-configured candidate** gets only the non-mutating checks from the configuration strategy.
   - Check error monitoring, if it applies;
   - release diff (if REA is installed): compare with the previous release using `compare-application-versions` or `compare-artifacts` (`references/reverse-engineering.md`).
5. **Recovery plan.**
   - **Later releases:** the **rollback target** (the previous production deployment ID), the **trigger** (for example, error rate above 2× baseline for 10 minutes, a failing payment flow, or a broken core flow) and the procedure.
   - **First launch** (no previous deployment): a **halt plan** instead, such as switching to a maintenance page, disabling public traffic or the domain alias, or unpublishing. Record its owner and trigger. If a step is level C (for example DNS), the user does it.
   - Migrations must be backward-compatible (expand, then contract), so a code rollback is safe without a database down-migration.
6. **Data safety** (stateful products): confirm a fresh backup or snapshot of production, and when the last restore test was (stage 4). Production migrations are **level C**: prepare the exact commands, and the user runs them as planned.
7. **Production go: CEO briefing.** Show the candidate (SHA, artifact ID, configuration profile, class), the evidence summary, the risks, and the rollback target or halt plan with its trigger. Then:
   - **First production deploy (level C):** the user promotes or deploys the exact artifact. Give copy-ready steps (for example, Vercel → Deployments → the candidate deployment → Promote to Production, or the exact CLI command).
   - **Later releases (level B):** ask "Promote artifact `<id>` (`<sha>`) to production, with rollback to `<target>` pre-authorized on `<trigger>`?" Only an explicit yes for that artifact counts. Log it.
8. **Promote** the exact candidate artifact. Never rebuild at this point.
9. **Watch.** `ecc:canary-watch` for the first hour: errors, key events and uptime, for the services that apply. If the trigger fires, run the pre-authorized rollback (or the halt plan, if its steps are level A or B) and tell the user immediately. Anything outside the pre-authorized scope goes back to the user.
10. **Tag and record.** Tag `v<version>` on the release SHA once it's healthy, record the production deployment ID, then commit the release records in a docs-only pull request.

## Mobile apps (iOS and Android)

Store releases replace steps 2–10 above with this path. Step 1 (release content first) still applies.

1. **Build and sign first.** From the release SHA, with production configuration, build the store binaries (for example with EAS Build or fastlane). Signing keys and keystores live in the build service's or the platform's secret store, never in the repository. Record each platform's **build number and artifact checksum** as the candidate.
2. **QA on those exact binaries.** Distribute them to TestFlight or a Play internal track, and run the stage 6 profile on them: device smoke tests, plus the security, privacy and data-safety checks. Production binaries point at production services, so **mutating tests (sign-ups, purchases, data changes, notifications) run on a sandbox build of the same SHA** with a staging backend. Store sandbox accounts (App Store sandbox testers, Play test accounts) only isolate the **payment provider**. The app's backend writes, emails and entitlement fulfilment still hit production, so they're never a substitute for the sandbox build. On production binaries, only non-mutating checks run; any unavoidable production-effect check is level C, run by the user. The evidence names the build numbers and checksums.
3. **Store package:** the agent prepares the listing, screenshots, privacy and data-safety answers, and release notes.
4. **Production go and submission (level C).** After the CEO briefing, the user submits **the same binaries** in App Store Connect or the Play Console. Plan for review delays of a day or more.
5. **Phased rollout:** start small (for example, 1–10%) and widen while crash-free sessions stay healthy.
6. **Halt plan instead of rollback:** you can't roll back store releases. Pause the phased rollout (Play: halt rollout; App Store: pause phased release), then ship a fixed build or a server-side flag. Pausing is level C unless the user pre-authorized it with this release.
7. **Backend compatibility:** older app versions stay in use for weeks. Keep APIs backward-compatible, and use a minimum-supported-version check or force-update for breaking changes.
8. Watch crash reporting (if it applies), then tag the release and commit the records.

## Gate: production go

**Web and server releases:**
- [ ] The release content (version, changelog, notes) was merged **before** the candidate was frozen
- [ ] The candidate is recorded (SHA, artifact ID, configuration profile, class) and still valid under the invalidation policy
- [ ] The stage 6 evidence names the same SHA, artifact and profile, and passes this class's profile
- [ ] Candidate verification passed: functional tests on the sandbox build, non-mutating checks on the production-configured candidate (for build-time configuration); no live effects were triggered by the agent
- [ ] There's a rollback target and trigger (later releases) or a halt plan with owner and trigger (first launch); migrations are backward-compatible; there's a fresh backup (stateful products)
- [ ] The user executed (level C) or approved (level B) this exact promotion, and it's logged
- [ ] No new error spike after deploy, or the rollback or halt was done and reported

**Mobile releases:**
- [ ] The store binaries were built and signed before QA; their build numbers and checksums are recorded
- [ ] The stage 6 evidence names those exact binaries
- [ ] The user submitted those same binaries (level C); a phased rollout and halt plan are in place
- [ ] Backend compatibility with older app versions is confirmed
