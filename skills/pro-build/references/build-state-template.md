# BUILD-STATE.md template

Copy to the project root as `BUILD-STATE.md` and keep it current at every gate.

```markdown
# <Company / product name>

- Track: Startup | Product | Client site | Existing project
- Stage: <0-9> <department>
- Next step: <one line>
- Last updated: <yyyy-mm-dd>

## Gates
| # | Department | Status | Date | Artifact |
|---|---|---|---|---|
| 0 | Founder Office | approved / pending / skipped (reason) | | docs/company/00-validation.md |
| 1 | Product | | | docs/company/01-prd.md |
| 2 | Engineering Leadership | | | docs/company/02-architecture.md |
| 3 | Design | | | docs/company/03-design/ |
| 4 | Platform / DevOps | | | docs/company/04-platform.md |
| 5 | Engineering | ongoing | | backlog below |
| 6 | QA & Security | | | docs/company/06-launch-readiness.md |
| 7 | Release | | | docs/company/07-releases/ |
| 8 | Go-to-Market | | | docs/company/08-gtm.md |
| 9 | Operate & Grow | | | docs/company/09-reviews/ |

## Decisions
- <date>: <decision> (<why>; ADR link if any)

## Backlog
### Now
- [ ] <feature> (acceptance: <one line>)
### Next
- [ ] <feature>
### Later
- <idea>
### Done
- [x] <feature> (PR #<n>, <date>)

## Services
| Service | Status | Environments |
|---|---|---|
| GitHub repo | | |
| Hosting (Vercel/Cloudflare) | | preview / staging / prod |
| Supabase | | |
| Stripe | test / live | |
| Sentry | | |
| PostHog | | |

## Metrics (latest review)
| Metric | Target | Last week | This week |
|---|---|---|---|
| North Star: <name> | | | |

## Risks and blockers
- <risk> (owner, mitigation)
```
