# Kickoff: understand the project before anything else

Every new project starts here, on every track. The goal: you understand **what** we are building, **why**, **for whom**, and **what success means**, and the user confirms it, before any document or code is written.

## 1. Read the idea

Take the user's idea as given. If `/pro-build` was called with no idea, ask: "What do you want to build? Describe it in a few sentences: what it is, who it's for, and why."

## 2. Discovery interview

Rules:

- Ask in **rounds of 2–4 questions**. Use the AskUserQuestion tool when it is available: offer concrete options with a recommended one first, so the user can click instead of type. Otherwise ask in plain text and number the questions.
- **Skip anything the idea already answers.** Never ask a question just to fill the list.
- **Adapt** each round to the previous answers. Stop when you could explain the project to an engineer and a designer without guessing: usually 2–4 rounds, never more than 6.
- If the user says "you decide", choose the sensible default, say what you chose, and record it as an assumption.

Question bank. Choose what is still unknown, in roughly this order:

| Area | Questions |
|:--|:--|
| **Purpose** | What problem does this solve? What happens today without it? |
| **Goal** | What does success look like in 3 months: users, revenue, a launch, a portfolio piece, a client handover? |
| **Users** | Who exactly uses it? Who pays, if that's someone else? How technical are they? |
| **Core value** | What is the one thing a user must be able to do in the first version? |
| **Scope** | Which features are must-have for v1, and which can wait? |
| **Platform** | Web app, mobile app, website, API, desktop, internal tool? Which devices? |
| **Business** | Will it make money? How: subscription, one-off, ads, client fee, none? |
| **Content and data** | What data does it store? Any personal, payment or sensitive data? Any existing content, brand or design? |
| **Integrations** | Payments, email, maps, AI models, login with Google, existing systems? |
| **Constraints** | Deadline, budget for hosting and services, preferred tech, team size (just the user, or others)? |
| **Language and market** | Languages, regions, right-to-left text, legal or compliance needs (GDPR, health, finance)? |
| **References** | Products or sites it should feel like? Ones it must not look like? |

## 3. Confirm understanding

Write back a short **Project Brief** and ask: "Is this right? Correct anything, or say approved."

```markdown
# Project Brief: <name>

- **One-liner:** <what it is, for whom, and why>
- **Problem:** <the pain today>
- **Goal (3 months):** <a measurable outcome>
- **Users:** <primary users> · **Buyer:** <who pays, if different>
- **Core value (v1 must-do):** <the one job>
- **Must-have features:** <short list>
- **Later:** <short list>
- **Platform:** <web, mobile, …> · **Languages:** <…>
- **Business model:** <…>
- **Data and integrations:** <…>
- **Constraints:** <deadline, budget, tech, team>
- **References:** <like X, not like Y>
- **Assumptions:** <choices made for the user>
- **Open questions:** <anything still unknown, and who decides>
```

Revise until the user approves it. Save it as `docs/company/00-brief.md`.

## 4. Recommend a track

Based on the brief, recommend **one** track from `SKILL.md`, list the stages it runs and the ones it skips, and ask the user to confirm. Then create `BUILD-STATE.md` from `references/build-state-template.md`, record the track, and start the first stage.

## 5. Model policy

In the same message as the track recommendation, set the model policy (see `references/model-routing.md`):

- Recommend the main-session model: Sonnet for most projects (`/model sonnet`), Opus for Kickoff and stages 0–2 of large or high-stakes ones.
- Ask once: **"Enable Fable for the hardest reviews? It may use paid usage credits."** The default is **off**.
- Record `Model policy` and `Fable: on/off` in `BUILD-STATE.md`.

## Gate K: brief approved

- [ ] The purpose, goal, users and v1 core value are clear
- [ ] Assumptions and open questions are written down
- [ ] The user approved the brief and the track
- [ ] The model policy is recorded (Fable on/off)
