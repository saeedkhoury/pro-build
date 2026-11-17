# Stage 2: Engineering Leadership

**Role:** CTO and architect. Choose a stack the team can ship and operate, and record the decisions.

## Steps

1. **Architecture.** Use `ecc:blueprint` with the PRD. Decide the stack, data model, API shape (`ecc:api-design`), authentication, integrations (payments, email, analytics, error monitoring), environments (local, preview, staging, production) and hosting.
2. **Boring, proven defaults** unless the PRD demands otherwise. Recommend one option and say why:
   - Web app or SaaS: Next.js + TypeScript, Supabase (Postgres, auth, storage), Stripe, hosted on Vercel or Cloudflare.
   - Marketing or client site: Astro or Next.js, static-first, a form handled by email or the CRM.
   - Mobile: Expo (React Native) with the same backend.
   - Backend system: TypeScript or Python service, Postgres, Docker (`ecc:docker-patterns`).
3. **Decision records.** Use `ecc:architecture-decision-records`: one record per major choice, in `docs/company/adr/`.
4. **Security and privacy by design.** Data classification, auth model, secrets handling, personal-data handling and backups. Use `ecc:security-review` on the design itself.
5. **Independent plan review.** Run `claudex-loop:claudex-loop` with `mode=review` on the PRD and architecture so Codex challenges them. Without Codex, run `ecc:council`. Log each finding as accepted or rejected, with the reason.
6. **Cost estimate.** The monthly cost at 0, 100 and 1,000 users across hosting, database, email and monitoring.

## Output

`docs/company/02-architecture.md` and `docs/company/adr/*.md`.

## Gate: architecture approved

- [ ] The stack and hosting are chosen, with reasons
- [ ] The data model and auth model are defined
- [ ] There are decision records for the major choices
- [ ] The plan review is done and findings are resolved
- [ ] The cost estimate is accepted by the user
