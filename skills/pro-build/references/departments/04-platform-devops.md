# Stage 4: Platform / DevOps

**Model routing:** sign-in hand-offs in the main thread · `sonnet` for the scaffold, CI, environments and services · `haiku` for `.env.example`, README, PR template and the docs index.

**Role:** platform engineer. Before the first feature, set up the factory: repository, pipeline, environments and production services. Everything later depends on this.

## Steps

1. **Repository.** `git init` if needed, a `main` branch, a `.gitignore`, a `.env.example` with variable names only, a `README.md` (what it is, how to run, test and deploy it), and a pull request template. Offer to create a **private** GitHub repository; the user approves.
2. **Project `CLAUDE.md`.** The rules every future AI session follows: the stack and versions, the run, test, lint and build commands, coding conventions, folder structure, where the docs live (`docs/README.md`), what never to commit, and "use `/pro-build` to continue; read `BUILD-STATE.md` first".
3. **Scaffold.** Generate the app skeleton for the chosen stack (for Vercel and Next.js, `vercel:bootstrap` or `vercel:nextjs`), then run `ecc:project-init`.
4. **CI pipeline.** GitHub Actions on every pull request: install, lint, type-check, test, build, and a security scan (Semgrep runs locally through its plugin hooks; add the Semgrep or CodeQL action in CI if wanted). Use `ecc:github-ops` and `ecc:deployment-patterns`. Protect `main`: CI must pass before merging.
5. **Environments.** Preview deploys per pull request, staging, and production. Vercel: `vercel:deployments-cicd` and `vercel:env-vars`. Cloudflare: `cloudflare:wrangler`. Secrets go in the platform's secret store; map every variable per environment in `04-platform.md`.
6. **Backend services.** Supabase: `supabase:supabase` and `supabase:supabase-postgres-best-practices`. Migrations are in the repository (`ecc:database-migrations`), with row-level security on by default.
7. **Observability from day one.**
   - Errors: `sentry:sentry-get-started`, then `sentry:sentry-setup-releases` so errors map to deploys.
   - Product analytics: `posthog:instrument-product-analytics` and `posthog:instrument-feature-flags`. Track the metrics defined in the PRD.
8. **SEO foundations in the scaffold** (public sites): a unique title and description per page, canonical URLs, Open Graph and Twitter cards, `robots.txt`, an auto-generated `sitemap.xml`, structured data (`marketing-skills:schema`), semantic HTML, image alt text and fast loading. If the claude-seo plugin is installed, use `claude-seo:seo-technical` to check it.
9. **Spec mode (optional).** If spec-kit's `specify` command-line tool is installed (`command -v specify`), offer **spec-kit mode** for large features (see `references/spec-kit.md`). On yes, run `specify init --here --integration claude --script sh --non-interactive --force` (the user approves; review `git status` first), write the constitution from `CLAUDE.md`, and commit the result. Record `Spec mode: spec-kit` or `Spec mode: native` in `BUILD-STATE.md`. If it isn't installed, mention `uv tool install specify-cli` once, and continue in native mode.
10. **Payments (Startup track).** Stripe in **test mode**: `stripe:stripe-best-practices` and `stripe:stripe-docs`. Products and prices from the pricing hypothesis, checkout, customer portal and webhooks. The user switches to live mode in stage 8.

Each service needs the user to sign in or create an account. Prepare the exact step, then hand over (operating rule 2).

## Output

`docs/company/04-platform.md` covering the repository, CI, environments, the service list, the secrets map (names only) and a runbook for deploying and rolling back.

## Gate: pipeline green

- [ ] `README.md`, `CLAUDE.md` and `.env.example` exist and are accurate
- [ ] A pull request triggers CI, and CI passes
- [ ] A preview deploy works
- [ ] Sentry receives a test error from staging
- [ ] PostHog receives a test event
- [ ] Stripe test checkout works (Startup track)
- [ ] No secret is committed (`git log -p | grep -iE "sk_live|secret|password"` is clean)
