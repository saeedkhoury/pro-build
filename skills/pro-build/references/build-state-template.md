# BUILD-STATE.md template

Copy to the project root as `BUILD-STATE.md` and keep it current at every gate.

```markdown
# <Company / product name>

- Project type(s): Web / System / App, with the shape (for example "Web: SaaS app + System: API")
- Track: Startup | Product | Client site | Existing project
- Stage: <0-9> <department>
- Next step: <one line>
- Last updated: <yyyy-mm-dd>
- Model policy: auto routing (haiku / sonnet / opus) · Fable: off
- Main-session model: <sonnet | opus>
- Spec mode: native | spec-kit

## Gates
| # | Department | Status | Date | Artifact |
|---|---|---|---|---|
| K | Kickoff | approved / pending | | docs/company/00-brief.md |
| 0 | Founder Office | approved / pending / skipped (reason) | | docs/company/00-validation.md |
| 1 | Product | | | docs/company/01-prd.md |
| 2 | Engineering Leadership | | | docs/company/02-architecture.md, 02-plan.md |
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
| Payments (<provider>) | test / live / N/A | |

The full list of services, with chosen, alternative and N/A decisions, lives in `docs/company/02-architecture.md` → Service applicability.
| Sentry | | |
| PostHog | | |

## Metrics (latest review)
| Metric | Target | Last week | This week |
|---|---|---|---|
| North Star: <name> | | | |

## Approvals log (level B, from `references/authorization.md`)
| Date | Action | Scope (PR, commit SHA, build ID) | User's words |
|---|---|---|---|
| | | | |

## Release candidate (stage 7)
- Version: · Class: Major / Minor / Patch / Hotfix
- Commit SHA: · Artifact or build ID: · Configuration profile: runtime / build-time production
- Mobile: iOS build and checksum · Android build and checksum
- Stage 6 report SHA: (must match) · Status: valid / invalidated by <change>
- Rollback target (or first-launch halt plan): · Trigger: · Owner:
- Production deployment ID (after release):
- Hotfix follow-ups due: <checks and date>

## Operations
- Recovery objectives: RPO · RTO · Incident owner · Alert route
- Backups: on/off · Last restore test: <date, duration, result>
- Secret scanner: <tool> · Last scan: <date, result>

## Reliability and delivery (references/devops.md)
- SLOs: <journey: target, error budget left>
- Infrastructure approach: platform-managed / infrastructure as code (<tool>) / containers (<runtime>)
- Watch layers: uptime monitor <tool or N/A> · scheduled CI check <workflow or N/A> · AI watch routine <name or N/A>
- Paging: <tool and route> · last test page <date>

## Deploy log (for DORA)
| ID | Version | Platform | SHA | Included PRs (merged at) | Exposed to production | Class | Outcome |
|---|---|---|---|---|---|---|---|
| D-001 | | web / ios / android | | #12 (2026-11-17 10:00), #13 (…) | | | healthy / rolled back / halted / hotfixed / failed (I-…) |

## Incident log
| ID | SEV | Started | Recovered | Caused by deployment | Cause | Review |
|---|---|---|---|---|---|---|
| I-001 | | | | D-… / not deploy-related | | link |

## Model log
| Stage | Main work done by | Notes |
|---|---|---|
| | | |

## Risks and blockers
- <risk> (owner, mitigation)
```
