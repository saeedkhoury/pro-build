# Stage 2: Engineering Leadership

**Model routing:** decisions in the main thread · `opus` for the architecture, data model, ADRs and implementation plan · `fable` (only if `Fable: on`) or `opus` for the independent plan review.

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
7. **Implementation plan.** Use `ecc:plan` with the PRD and architecture to write `docs/company/02-plan.md`:
   - **Milestones.** M1 is the MVP: the smallest end-to-end version that delivers the core value from the brief. Then M2, M3, … from the roadmap.
   - For each milestone: its goal, the tasks (each small enough for one pull request), dependencies, acceptance criteria, risks, and the proof that it's done.
   - A definition of done that applies to every task: tests pass, CI is green, it's reviewed, docs are updated.
8. **Consistency check** (like spec-kit's `analyze`; it does not modify files). Before the gate, cross-check the PRD, architecture and plan, and add a **Traceability** table to `02-plan.md`:
   - Every PRD requirement and acceptance criterion maps to at least one plan task, and every task maps back to a requirement. Flag orphans either way.
   - Each data entity, API and integration the PRD needs exists in the architecture.
   - Terms, names and numbers (limits, prices, roles) are the same in all three documents.
   - Every acceptance criterion is testable, and every non-functional requirement (performance, security, accessibility) has a task.
   Fix the gaps, or list them as open questions for the CEO briefing. Use `opus` for this check.

## Output

`docs/company/02-architecture.md`, `docs/company/adr/*.md` and `docs/company/02-plan.md`. Add them to `docs/README.md`.

## Gate: architecture approved

- [ ] The stack and hosting are chosen, with reasons
- [ ] The data model and auth model are defined
- [ ] There are decision records for the major choices
- [ ] The plan review is done and findings are resolved
- [ ] The cost estimate is accepted by the user
- [ ] The implementation plan defines M1 (the MVP), with tasks and acceptance criteria
- [ ] The consistency check passes: every requirement traces to tasks, with no orphans or contradictions
