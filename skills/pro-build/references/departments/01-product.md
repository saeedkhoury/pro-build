# Stage 1: Product

**Model routing:** questions in the main thread · `sonnet` drafts the PRD and roadmap · `opus` reviews scope and metrics.

**Role:** Head of Product. Turn the validated idea into a precise, buildable spec with measurable success.

## Steps

Input: `00-brief.md` (and `00-validation.md` on the Startup track).

1. **PRD.** Use `ecc:plan-prd` (or `ecc:prp-prd` when requirements are still vague) with the brief and validation as input. If something the PRD needs is still unknown, ask the user. Never invent requirements. It must include users and personas, jobs to be done, the core user flows, functional requirements, non-functional requirements (performance, security, accessibility, privacy), out of scope, and acceptance criteria.
2. **MVP scope.** Cut ruthlessly to the smallest product that delivers the core value and can take a payment if the track is Startup. List everything else under "Later".
3. **Success metrics.** Define a North Star metric plus 3 to 5 input metrics (for example activation rate, week-1 retention, trial-to-paid conversion), with how each will be measured in PostHog.
4. **Roadmap.** Now, Next, Later, in `docs/company/01-roadmap.md`. Turn Now into the feature backlog in `BUILD-STATE.md`, as small, independently shippable items.

## Output

`docs/company/01-prd.md`, `docs/company/01-roadmap.md`, and the backlog in `BUILD-STATE.md`. Add both to `docs/README.md`.

## Gate: spec approved

- [ ] Every MVP feature has acceptance criteria
- [ ] There is a North Star metric and input metrics, with how each is measured
- [ ] Out-of-scope items are written down
- [ ] The backlog is ordered and each item is small
