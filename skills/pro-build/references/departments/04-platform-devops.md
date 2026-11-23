# Stage 4: Platform / DevOps

**Model routing:** sign-in hand-offs in the main thread · `sonnet` for the scaffold, CI, environments, services, backups and runbooks · `haiku` for `.env.example`, README, PR template and the docs index.

**Role:** platform engineer. Before the first feature, build the factory: repository, pipeline, protected environments, the services chosen in stage 2, backups and the operations runbook. Every service listed in stage 2's **service applicability table** is set up, replaced by its alternative, or marked N/A, exactly as recorded there. All actions follow `references/authorization.md`.

## Steps

1. **Repository.** `git init` if needed, a `main` branch, a `.gitignore`, a `.env.example` with variable names only, a `README.md` (what it is, how to run, test and deploy it), and a pull request template. Offer to create a **private** GitHub repository; the user approves.
2. **Project `CLAUDE.md`.** The rules every future AI session follows: the stack and versions, the run, test, lint and build commands, coding conventions, folder structure, where the docs live (`docs/README.md`), what never to commit, and "use `/pro-build` to continue; read `BUILD-STATE.md` first".
3. **Scaffold.** Generate the app skeleton for the chosen stack (for Vercel and Next.js, `vercel:bootstrap` or `vercel:nextjs`), then run `ecc:project-init`.
4. **CI pipeline.** GitHub Actions on every pull request: install, lint, type-check, test, build, a dependency audit and a **secret scan** (step 11). Use `ecc:github-ops` and `ecc:deployment-patterns`. Turn on branch protection for `main` (CI must pass, no direct pushes) and enable Dependabot or Renovate for dependency updates.
5. **Environments and production protection.** Preview deploys per pull request, a **staging** environment, and **production**.
   - **Merging to `main` must not deploy to production.** Configure it so `main` deploys to staging only, and production changes only by promoting a specific, already-built staging deployment (stage 7). On Vercel, turn off auto-assigning the production domain on merge, or deploy from a separate production branch that only gets promoted builds. On Cloudflare and others, use a manual or protected production environment. GitHub environments with required reviewers work for custom pipelines.
   - Apply stage 2's **configuration strategy**. For runtime configuration, prove once that a promoted staging artifact picks up production settings. For build-time configuration, set up a protected, non-public production-configured preview or pre-production environment, where stage 7 builds and tests the candidate.
   - Use `vercel:deployments-cicd` and `vercel:env-vars`, or `cloudflare:wrangler`, as applicable. Secrets go in the platform's secret store; map every variable per environment in `04-platform.md`.
6. **Backend services.** As chosen in stage 2 (for example Supabase: `supabase:supabase` and `supabase:supabase-postgres-best-practices`). Migrations live in the repository (`ecc:database-migrations`), are backward-compatible (expand, then contract), and have row-level security on by default.
7. **Observability, as applicable.**
   - Errors: Sentry (`sentry:sentry-get-started`, then `sentry:sentry-setup-releases`), or the alternative chosen in stage 2.
   - Product analytics: PostHog (`posthog:instrument-product-analytics`, `posthog:instrument-feature-flags`), or the alternative. Track the metrics defined in the PRD.
   - Uptime or alerting to the alert channel from stage 2.
8. **SEO foundations in the scaffold** (public sites): a unique title and description per page, canonical URLs, Open Graph and Twitter cards, `robots.txt`, an auto-generated `sitemap.xml`, structured data (`marketing-skills:schema`), semantic HTML, image alt text and fast loading. If claude-seo is installed, check it with `claude-seo:seo-technical`.
9. **Spec mode (optional).** If spec-kit's `specify` command-line tool is installed (`command -v specify`), offer **spec-kit mode** for large features (see `references/spec-kit.md`). On yes, run `specify init --here --integration claude --script sh --non-interactive --force` (the user approves; review `git status` first), write the constitution from `CLAUDE.md`, and commit the result. Record `Spec mode: spec-kit` or `Spec mode: native` in `BUILD-STATE.md`. If it isn't installed, mention `uv tool install specify-cli` once, and continue in native mode.
10. **Payments (Startup track, if applicable).** Stripe in **test mode**: `stripe:stripe-best-practices` and `stripe:stripe-docs`. Products and prices from the pricing hypothesis, checkout, customer portal and webhooks (with signature checks). The user switches to live mode in stage 8 (level C).
11. **Secret scanning.** Use a real credential scanner, not a keyword grep. Use one of: Semgrep's secrets scanning (the semgrep plugin, after a free login), `gitleaks` (`gitleaks git` for the history plus `gitleaks dir` for the working tree), or `trufflehog`. Also enable GitHub secret scanning and push protection where available.
    - Run it on the **full git history** and the **build output**, in CI on every pull request, and here at the gate.
    - Report findings **redacted**: rule, file, line and commit, never the secret value.
    - Review false positives and record them in the scanner's allowlist, with a reason.
    - **A real exposed credential:** it's compromised. The user **rotates or revokes it (level C)**; the agent updates the code to the new secret, then records whether to rewrite git history. On a private repo, rotation is mandatory and a history rewrite is optional. Once a repo is public, assume the secret has been copied.
12. **Backups and restore (stateful products).** Turn on automated backups or point-in-time recovery that meets the RPO from stage 2, with enough retention. Then **test a restore** into staging or a scratch database, and record the date, the duration (against the RTO) and the result. Repeat at least every 90 days.
13. **Operations runbook.** In `04-platform.md`: deploy, promote and roll back; the restore procedure; and **incident response**:
    - severity levels (SEV1–3) and the incident owner, from stage 2;
    - the alert route, so alerts reach the owner;
    - first steps per severity (acknowledge, roll back or mitigate, communicate, fix);
    - a status-update template for users;
    - a short post-incident review, recorded in `docs/company/09-reviews/`.

Each service needs the user to sign in or create an account (level C). Prepare the exact step, then hand over.

## Output

`docs/company/04-platform.md`: the repository and CI, environments and production protection, the services (matching stage 2's table), the secrets map (names only), the secret-scanning setup, the backup policy and last restore test, and the operations runbook.

## Gate: pipeline green

- [ ] `README.md`, `CLAUDE.md` and `.env.example` exist and are accurate
- [ ] A pull request triggers CI (including the secret scan and dependency audit), and CI passes; `main` is protected
- [ ] The configuration strategy is set up: runtime promotion proven, or a protected production-configured pre-production environment exists
- [ ] **Production protection is verified:** a merge to `main` produced a staging deployment and did **not** change production. Show the deployment list or settings as evidence
- [ ] Every row of stage 2's service applicability table has its evidence: chosen service working, alternative working, or N/A with the accepted reason. For example: a Sentry or alternative test event, an analytics test event, Stripe test checkout
- [ ] The secret scan of the history and working tree has no unresolved findings; any real exposure was rotated by the user
- [ ] Backups are on and a restore test succeeded within the RTO (stateful products), or N/A with a reason
- [ ] The operations runbook exists, with an alert route reaching the incident owner
