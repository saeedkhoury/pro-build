# Stage 6: QA & Security

**Model routing:** the findings briefing in the main thread · `opus` for the security review and triage of REA findings · `sonnet` for end-to-end, browser, accessibility, SEO and performance checks · `haiku` to compile the report.

**Role:** QA lead and security officer. Prove that **one exact build** works and is safe. Stage 6 runs **for every release**, using the profile for its class (`07-release.md`). Results are bound to the commit SHA under test.

## Evidence rules

- Each check ends with exactly one status:
  - **pass:** run, with evidence attached (a command and its output, a report link, screenshots);
  - **fail:** findings exist;
  - **blocked:** it couldn't run (a missing tool, service or access);
  - **N/A:** it doesn't apply to this product, with a written reason, accepted by the user at the gate;
  - **accepted risk:** a required check that's blocked or failed, which the user knowingly accepts. The original status and findings stay in the report next to it.
- **"No findings" isn't "pass".** A pass needs evidence that the check actually ran on this SHA.
- **A required check that's blocked, failed or missing blocks the release,** unless it becomes **accepted risk**:
  - **Eligible:** checks 3, 7, 8, 9, 10, 12 and 13 (browser, accessibility, performance, SEO, coverage, restore test, final review), and check 2 when the failing flow isn't payment, auth or data-loss related.
  - **Never eligible:** check 1 (CI), 4 (security review) and 5 (secret scan); check 6 (exposure audit) and check 11 (privacy) for Major releases; and any open blocking security or payment finding.
  - **How:** the user approves it in the conversation (level B), scoped to this check and this release SHA, with a reason, an owner and an expiry (at most 30 days, or the next release, whichever comes first). It's logged in `BUILD-STATE.md` → Approvals and in the report.
- Unknown or not-assessed results from scanners stay in the report; they're never counted as passes.
- **When results stop counting:** follow the **invalidation policy** in `07-release.md` (release records don't invalidate; requirement changes invalidate the dependent checks; code or configuration changes invalidate everything). Rerun at least the affected checks, and the full profile for Major releases.
- **No live effects:** mutating tests (sign-ups, payments, data changes) never run against production services. For build-time configuration, they run on the sandbox build of the same SHA (see `07-release.md` → Configuration strategy).

## Profiles

| Check | Full (Major) | Standard (Minor) | Light (Patch, Hotfix) |
|:--|:--:|:--:|:--:|
| 1. CI green on the SHA (lint, types, tests, build) | Required | Required | Required |
| 2. End-to-end core flows (`ecc:e2e-testing`): sign-up, core value, payment, cancellation | Required | Required for changed flows | Smoke only |
| 3. Real browser (`ecc:browser-qa`), desktop and mobile widths | Required | Required for changed pages | Optional |
| 4. Security review (`ecc:security-scan`, `ecc:security-review`), plus Semgrep findings, for auth, payments, webhooks, input handling, RLS | Required | Required if auth, payments or data access changed | Required if security-relevant |
| 5. Secret scan of the repository and build output (see stage 4) | Required | Required | Required |
| 6. Release exposure audit (REA `audit-release-exposure`; see `references/reverse-engineering.md`). Without REA: manual `*.map` and secret checks on the build output | Required | Required | Optional |
| 7. Accessibility, WCAG 2.2 AA (`ecc:accessibility`) | Required (UI) | Changed UI | Optional |
| 8. Performance: Core Web Vitals and API latency (`ecc:production-audit`) | Required | Optional | Optional |
| 9. SEO and AI-search readiness (`ecc:seo`, `claude-seo:seo-audit`, `marketing-skills:ai-seo`) | Required (public sites) | Changed pages | Optional |
| 10. Coverage at the project target (`ecc:test-coverage`) | Required | Required | Optional |
| 11. Privacy and legal (policy, terms, cookies, data export and deletion), drafted for user review | Required when personal data or payments exist | If data use changed | Optional |
| 12. Backups and restore (stateful products): last restore test within 90 days | Required | Optional | Optional |
| 13. Final adversarial review (`ecc:santa-loop`) | Required | Optional | Optional |

REA blocking rules: an exposed `text.credential_markers` or `javascript.source_map_sources` check is a **fail** for check 6.

## Output

`docs/company/06-launch-readiness.md`, headed with the **commit SHA**, the **artifact or build ID**, the **configuration profile** (see stage 7), the **requirements baseline** (the commit SHA of the latest change to `docs/company/01-*`, `02-*` and `adr/**`), the release class and the date. It's a record about the build, not part of it: writing or committing it doesn't invalidate the candidate (see stage 7's records policy). For each check: its status, evidence, and findings (blocking or advisory, with an owner), plus any N/A reasons and risk acceptances.

## Gate: release evidence complete

- [ ] The report names the exact SHA and build under release
- [ ] Every required check for the class is **pass**, **N/A** (with a reason the user accepted), or **accepted risk** (eligible, scoped to this SHA, unexpired, logged with its original status)
- [ ] No blocking findings are open, except those in an eligible accepted-risk check; fixed checks were rerun on the new SHA
- [ ] Advisory findings have an owner, or the user accepted them
