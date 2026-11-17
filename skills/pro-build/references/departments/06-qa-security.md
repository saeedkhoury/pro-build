# Stage 6: QA & Security

**Model routing:** the findings briefing in the main thread · `opus` for the security review · `sonnet` for end-to-end, browser, accessibility, SEO and performance checks · `haiku` to compile the report.

**Role:** QA lead and security officer. Prove the product works and is safe before real users touch it. Run this before the first production release, then before every major release.

## Checks

1. **End-to-end:** `ecc:e2e-testing` covering sign-up, the core value flow, payment and cancellation.
2. **Real browser:** `ecc:browser-qa` on the main pages and flows, desktop and mobile widths.
3. **Accessibility:** `ecc:accessibility`, WCAG 2.2 AA.
4. **Security:** `ecc:security-scan` plus `ecc:security-review` on auth, payments, webhooks, input handling and row-level security policies. Review Semgrep findings. For deeper audits, ask the `security-reviewer` agent.
4b. **Release exposure audit** (if REA is installed): run `audit-release-exposure` on the production build output, and `analyze-web-bundle` on the staging URL, through `rea:reverse-engineer-anything` (see `references/reverse-engineering.md`). Exposed credentials or production source maps are **blocking**. Without REA, check for `*.map` files and secret patterns in the build output by hand.
5. **Performance:** Core Web Vitals and API latency (`ecc:production-audit`); fix the obvious problems.
6. **SEO and AI-search readiness** (public sites): `ecc:seo` or `claude-seo:seo-audit` if installed. Check crawlability, indexability, metadata, structured data, Core Web Vitals, and visibility in AI search (`marketing-skills:ai-seo`). Fix the blocking issues.
7. **Coverage:** `ecc:test-coverage` against the project target.
8. **Privacy and legal basics:** a privacy policy, terms, cookie consent where required, data export and deletion if personal data is stored. Draft them; the user has them reviewed if needed.
9. **Final review:** `ecc:santa-loop` (adversarial dual review) on the release candidate.

## Output

`docs/company/06-launch-readiness.md`: each check with pass, fail or not run, findings ranked as blocking or advisory, and evidence.

## Gate: no blocking findings

- [ ] All blocking findings are fixed (through stage 5 cycles) and the failed checks were rerun
- [ ] Advisory findings are logged with an owner or accepted by the user
