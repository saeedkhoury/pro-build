# Kickoff: understand everything before anything starts

Every new project starts here, on every track. **Ask more than feels necessary.** Fifteen extra minutes of questions is cheaper than weeks of building the wrong thing. No document, plan, design or code is created until the user approves the Project Brief.

## How to interview

- **Rounds of 3–5 questions.** Use AskUserQuestion when it's available: concrete options, the recommended one first, and "Other" for free text. Otherwise, number the questions in plain text.
- **Typically 5–8 rounds.** There's no fixed maximum. Stop only when the **coverage checklist** below is complete.
- **After every round, show a short progress note:** "Understood so far: … · Still unknown: … · Next round: …".
- **Probe vague answers.** "Everyone" as the users, "fast", "cheap" or "like Uber" all get a follow-up: Who exactly? How fast, in seconds? What budget per month? Which part of Uber?
- **Turn wishes into numbers:** users at launch and in a year, deadline, monthly budget, response times, the success metric.
- **Skip only what the user has already said,** and quote it back so they can correct it.
- **Never invent answers.** If the user says "you decide", choose a sensible default, say it explicitly, and record it as an **assumption**. That's allowed only for non-critical items (see below).

## Step 1: Read the idea and identify the project type

Take the idea as given. If `/pro-build` was called without one, ask: "What do you want to build? Describe it in a few sentences: what it is, who it's for, and why."

Identify the **project type** (one or more) and confirm it with the user:

| Type | Examples | Playbook |
|:--|:--|:--|
| **Web** | Website, landing page, e-commerce, SaaS dashboard, portal, PWA | `references/project-types/web.md` |
| **System** | API, backend, microservice, worker, data pipeline, integration, bot, CLI | `references/project-types/system.md` |
| **App** | iOS, Android, cross-platform mobile, tablet, desktop | `references/project-types/app.md` |

Most products combine types (for example, an **App** plus its **System** backend, or a **Web** SaaS plus a **System** API). Read every playbook that applies; its question bank feeds step 3.

## Step 2: Universal questions (every project)

| Area | Ask about |
|:--|:--|
| **Purpose** | The problem it solves; what happens today without it; why now |
| **Users** | Exactly who uses it; who pays (if different); how technical they are; how many at launch and in a year |
| **Goal** | What success looks like in 3 months, as a number (users, revenue, orders, time saved, a launch date); what failure would look like |
| **Core value** | The single thing a user must be able to do in v1 |
| **Scope** | v1 must-haves; nice-to-haves; explicit out-of-scope |
| **Business** | Will it make money? How (subscription, one-off, ads, client fee, none)? A price idea? |
| **Data** | What's stored; personal, payment, health or children's data; who owns it; how long it's kept |
| **Constraints** | Deadline; monthly budget for hosting and services; preferred or forbidden tech; who builds and maintains it (just the user, a team, a client) |
| **Existing assets** | Brand, domain, designs, content, code, accounts, data to migrate |
| **Market and language** | Countries, languages, right-to-left text, legal or compliance requirements |
| **References** | Products to feel like, and ones not to feel like, with the specific parts they like or dislike |

## Step 3: Type-specific questions

Ask the **Kickoff questions** from each applicable playbook in `references/project-types/`. Skip any the answers have already settled.

## Step 4: Risks, edge cases and priorities

- What could make this fail: demand, competition, legal, technical, time, money?
- What must **never** happen (data loss, a double charge, a privacy leak, downtime at a key moment)?
- The worst realistic day: a traffic spike, a bad review, an outage. What should happen?
- **Trade-offs:** ask the user to rank **speed to launch**, **quality and polish**, and **cost**. Ask which one they'd sacrifice first.
- What does the user want to **learn or own** themselves, and what should be delegated?

## Coverage checklist

Track it visibly. Kickoff ends only when every row is ✅ answered or 🅰️ an assumption the user accepted.

| Item | Critical? |
|:--|:--:|
| Project type(s) confirmed | **Yes** |
| Problem and purpose | **Yes** |
| Primary users (and buyer) | **Yes** |
| 3-month goal, as a number | **Yes** |
| v1 core value and must-haves | **Yes** |
| Out of scope | **Yes** |
| Business model (or "none") | **Yes** |
| Data sensitivity | **Yes** |
| Deadline and monthly budget | **Yes** |
| Who builds and maintains it | **Yes** |
| Platforms and devices | **Yes** |
| Type-specific critical items: Web (content vs app, accounts, payments); System (callers, load, consistency needs); App (stores vs PWA, device features, offline) | **Yes** |
| Integrations | No |
| Languages and regions | No |
| Existing assets | No |
| References | No |
| Top risks and must-never-happen | No |
| Priority ranking (speed, quality, cost) | No |

**Critical items must be answered by the user.** They can't be defaulted. Non-critical items may become recorded assumptions when the user says "use your recommendations".

## Fast lane (when the user says "just start" or "don't ask so much")

Respect it, without skipping understanding:
- Explain in one line why a few answers are essential.
- Ask **only the critical items**, compressed into about two rounds, as **explicit questions** with recommended options, so each answer is one click (or a reply like "1a 2b 3a").
- **Never pre-fill critical items** in a draft brief for blanket approval. "Approve this whole brief" isn't an answer to the critical questions, because it invites a rubber stamp. The brief comes only after the critical answers.
- Default everything else, and list the defaults in the brief as assumptions the user can change later.

## Step 5: Teach it back, then get approval

Write the **Project Brief**, then ask: "Is this right? Correct anything, or say approved."

```markdown
# Project Brief: <name>

- **One-liner:** <what it is, for whom, and why>
- **Project type(s):** <Web / System / App>, with the shape from each playbook (for example "Web: SaaS app")
- **Problem:** <the pain today, and what happens without it>
- **Goal (3 months):** <a number> · **Failure looks like:** <…>
- **Users:** <primary users, how many> · **Buyer:** <who pays>
- **Core value (v1 must-do):** <the one job>
- **Must-have:** <list> · **Later:** <list> · **Out of scope:** <list>
- **Business model:** <…> · **Price idea:** <…>
- **Data:** <what, how sensitive, retention>
- **Platforms and devices:** <…> · **Languages and regions:** <…>
- **Integrations:** <…> · **Existing assets:** <…>
- **Constraints:** deadline <…> · budget <…/month> · team <…> · tech preferences <…>
- **Priorities:** <ranked speed, quality, cost>
- **Must never happen:** <…> · **Top risks:** <…>
- **References:** like <…> (because …), not like <…> (because …)
- **Assumptions (accepted defaults):** <…>
- **Open questions** (who decides, by when): <…>
- **Coverage:** <n>/<n> items, all critical items answered by the user
```

Revise until the user approves. Save the brief as `docs/company/00-brief.md`.

## Step 6: Recommend a track and the model policy

- **Track:** recommend **one** track from `SKILL.md`. List the stages it runs and the ones it skips, and ask the user to confirm.
- **Model policy** (see `references/model-routing.md`), in the same message:
  - Recommend the main-session model: Sonnet for most projects (`/model sonnet`), Opus for Kickoff and stages 0–2 of large or high-stakes ones.
  - Ask once: **"Enable Fable for the hardest reviews? It may use paid usage credits."** The default is **off**.
- Then create `BUILD-STATE.md` from `references/build-state-template.md`, recording the project type(s), the track, `Model policy` and `Fable: on/off`.

## Gate K: brief approved

- [ ] Every critical coverage item was answered by the user; the other items were answered or accepted as assumptions
- [ ] The project type(s) are confirmed, and the matching playbooks were used
- [ ] The goal is measurable, and the out-of-scope list exists
- [ ] The user approved the brief, the track and the model policy (Fable on or off)

## Asking doesn't stop after Kickoff

At **every stage**, when something material is unclear (a requirement, an edge case, a trade-off), ask before assuming. Batch the questions, recommend an answer, and write the decision into the **authoritative document** (brief, PRD, architecture or plan), logging it in `BUILD-STATE.md` → Decisions. If it changes a requirement after QA, stage 7's invalidation policy applies.
