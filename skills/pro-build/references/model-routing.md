# Model routing: the right model for each task

Goal: top quality where it matters, and the fewest tokens everywhere else.

## How routing works in Claude Code

- The **main conversation** runs on the model the user chose (`/model`). A skill cannot switch it. The main thread handles the conversation: the Kickoff interview, gates, CEO briefings, coordination and final decisions.
- **Routing happens through delegation.** Give each self-contained task to a subagent with the **Agent tool**, and set its `model` parameter to `haiku`, `sonnet`, `opus` or `fable`. Give it a complete brief: goal, file paths, constraints, the expected output, and which skill to use (for example, "use the `ecc:orch-add-feature` skill"). It returns a result for you to check.
- Subagents cannot talk to the user. Anything that needs the user's answer stays in the main thread.
- Recommend that the user runs the main session on **Sonnet** day to day (`/model sonnet`). Suggest switching the main session to **Opus** (`/model opus`) for Kickoff and stages 0–2 on large or high-stakes projects, and back to Sonnet for stage 4 onwards.

## Where the savings come from

1. **The main-session model:** this is the biggest lever. Sonnet in the main thread instead of Opus cuts the cost of every turn. Switch to Opus only for Kickoff and stages 0–2 on big projects.
2. **Delegating heavy mechanical work to haiku:** codebase mapping, log triage, bulk edits, reports.
3. **Saving opus (and fable) for decisions** where a mistake costs more than the tokens.

## Tiers

| Tier | Use for | Examples |
|:--|:--|:--|
| **haiku**: fast, cheapest | Mechanical, low-risk, well-specified work with an obvious right answer | Searching and mapping the codebase, summarising files and logs, formatting, renames, lint and type fixes, boilerplate, test fixtures, translations, changelog and release-note drafts, `BUILD-STATE.md` updates, status reports, bulk meta tags and alt text, CI log triage |
| **sonnet**: the default | Most real engineering and writing | Implementing features and fixes, writing tests, refactors, UI from a design, CI/CD and infrastructure config, PRD and README drafts, marketing copy, standard code reviews, SEO implementation |
| **opus**: deep reasoning | Ambiguous, high-stakes or cross-cutting decisions where a mistake is expensive | Founder Office strategy and go/no-go analysis, pricing, architecture and data model, implementation-plan review, security review (auth, payments, personal data), hard debugging after one failed attempt, reviews of risky or large changes, launch-readiness judgement |
| **fable**: top tier, **opt-in only** | The hardest reasoning, when the user has enabled it | Independent plan review, final review of a major release, a deep security audit. **Fable needs usage credits on many accounts: never use it unless `BUILD-STATE.md` says `Fable: on`.** If it's off or unavailable, use Opus |

## Default routing by stage

| Stage | Main thread (user's model) | Delegate to |
|:--|:--|:--|
| K Kickoff | Interview and Project Brief | haiku: read existing files or links the user gives |
| 0 Founder Office | Office-hours questions, go/no-go briefing | opus: market, competitor and pricing analysis · haiku: collect and summarise sources |
| 1 Product | Clarifying questions, approval | sonnet: PRD and roadmap drafts · opus: review of scope and metrics |
| 2 Eng Leadership | Decisions with the user | opus: architecture, data model, ADRs, implementation plan · fable (if on) or opus: independent plan review |
| 3 Design | Direction choices with the user | sonnet: design system, components, mockups · haiku: token and asset bookkeeping |
| 4 Platform/DevOps | Sign-in hand-offs | sonnet: scaffold, CI, environments, service setup · haiku: `.env.example`, README, PR template, docs index |
| 5 Engineering | Merge approvals, MVP demo | sonnet: each feature or fix cycle · haiku: codebase search, lint and build fixes, test fixtures · opus: hard bugs after one failed attempt, review of risky pull requests |
| 6 QA & Security | Findings briefing | opus: security review and REA findings triage · sonnet: REA release exposure audit · sonnet: end-to-end, browser, accessibility and performance checks · haiku: collect results into the report |
| 7 Release | Production go | haiku: version bump, changelog, release notes · sonnet: staging deploy and smoke tests, canary watch · opus: rollback decision on unclear signals |
| 8 Go-to-Market | Launch go, live-payments hand-off | sonnet: copy, landing page, pricing page, emails, SEO implementation · opus: positioning and pricing strategy · haiku: meta tags, schema, sitemap, directory submissions |
| 9 Operate & Grow | Weekly decisions | haiku: pull and tabulate metrics, Sentry and Stripe summaries · opus: analysis and next-focus recommendation |

## Rules

1. **Start low, escalate on evidence.** Use the cheapest tier that fits. If a subagent fails or its result doesn't pass review, retry **one tier up** once, then bring it to the main thread. Never downgrade security, payments, auth or data-migration work below sonnet.
2. **Batch small tasks.** One haiku subagent doing five mechanical tasks beats five separate calls.
3. **Delegate only when it pays off.** Each subagent loads the full tool and skill context before doing any work. In a setup with many plugins that can be 100k+ tokens, mostly cached but not free. Delegate big chunks: roughly 10+ tool calls, many files, or long outputs. Do anything that takes a few tool calls in the main thread, and batch small tasks into one subagent.
4. **Write tight briefs.** Subagents start cold: give exact paths, the acceptance criteria and the output format, so they don't re-explore the codebase.
5. **Verify before trusting.** Check a subagent's result (tests, a diff, a file) before reporting it as done.
6. **Log costs at gates.** Note which tiers did the stage's main work in `BUILD-STATE.md` under "Model log", and run `ecc:cost-report` when the user asks about spend.
7. **Respect the user's choice.** If the user says "use opus for everything" or "keep it cheap", record it in `BUILD-STATE.md` under "Model policy" and follow it.
