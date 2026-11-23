# ChairBook (eval fixture)

- Track: Startup
- Stage: 5 Engineering
- Next step: Add booking form (M2)
- Last updated: 2026-11-20
- Model policy: auto routing (haiku / sonnet / opus) · Fable: off
- Main-session model: sonnet
- Spec mode: native

## Gates
| # | Department | Status | Date | Artifact |
|---|---|---|---|---|
| K | Kickoff | approved | 2026-11-02 | docs/company/00-brief.md |
| 0 | Founder Office | approved (go) | 2026-11-04 | docs/company/00-validation.md |
| 1 | Product | approved | 2026-11-06 | docs/company/01-prd.md |
| 2 | Engineering Leadership | approved | 2026-11-09 | docs/company/02-architecture.md, 02-plan.md |
| 3 | Design | approved | 2026-11-12 | docs/company/03-design/ |
| 4 | Platform / DevOps | approved | 2026-11-15 | docs/company/04-platform.md |
| 5 | Engineering | ongoing (M1 merged, demo approved 2026-11-19) | | backlog below |

## Backlog
### Now (M2)
- [ ] Add booking form (T4, R3; acceptance: customer picks service, barber and slot; slot locked; booking saved; confirmation email)
- [ ] Deposits (T5, R4; acceptance: 20% deposit via Stripe Checkout; webhook verified; refundable up to 24h before)
- [ ] Stripe Connect payouts to barbers (T6, R5; depends on T5; acceptance: barber onboarding via Express; deposit split; platform fee 5%)
### Done
- [x] M1: shop page, service list, barber calendar (PR #4, 2026-11-19)

## Services
| Service | Status | Environments |
|---|---|---|
| GitHub repo | private, main protected | — |
| Vercel | staging on main; production protected | preview / staging / prod |
| Supabase | ready | staging / prod |
| Stripe | test | — |
| Sentry | ready | staging |
| PostHog | ready | staging |
