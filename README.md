<div align="center">

<img src="assets/banner.svg" alt="pro-build: your AI software company. From idea to paying users." width="100%">

<br>

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757?style=flat-square)](https://code.claude.com/docs/en/plugins)
[![Version](https://img.shields.io/badge/version-2.11.0-7c3aed?style=flat-square)](CHANGELOG.md)
[![Powered by ECC](https://img.shields.io/badge/powered%20by-ECC-0ea5e9?style=flat-square)](https://github.com/affaan-m/ECC)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-open%20standard-16a34a?style=flat-square)](#-works-with-your-ai-agent)

**Works with**

<table>
  <tr>
    <td align="center" width="96"><a href="https://code.claude.com"><img src="https://cdn.simpleicons.org/claude" width="48" height="48" alt="Claude Code logo"><br><sub><b>Claude Code</b></sub></a></td>
    <td align="center" width="96"><a href="https://github.com/openai/codex"><img src="https://github.com/openai.png?size=96" width="48" height="48" alt="Codex logo"><br><sub><b>Codex</b></sub></a></td>
    <td align="center" width="96"><a href="https://github.com/MoonshotAI/kimi-cli"><img src="https://cdn.simpleicons.org/kimi" width="48" height="48" alt="Kimi Code logo"><br><sub><b>Kimi Code</b></sub></a></td>
    <td align="center" width="96"><a href="https://github.com/google-gemini/gemini-cli"><img src="https://cdn.simpleicons.org/googlegemini" width="48" height="48" alt="Gemini CLI logo"><br><sub><b>Gemini CLI</b></sub></a></td>
    <td align="center" width="96"><a href="https://github.com/xai-org"><img src="https://github.com/xai-org.png?size=96" width="48" height="48" alt="Grok Build logo"><br><sub><b>Grok Build</b></sub></a></td>
    <td align="center" width="96"><a href="https://github.com/anomalyco/opencode"><img src="https://cdn.simpleicons.org/opencode" width="48" height="48" alt="OpenCode logo"><br><sub><b>OpenCode</b></sub></a></td>
    <td align="center" width="96"><a href="https://cursor.com"><img src="https://github.com/cursor.png?size=96" width="48" height="48" alt="Cursor logo"><br><sub><b>Cursor</b></sub></a></td>
  </tr>
</table>

**Run every project like a real software company.**<br>
Describe your idea. pro-build interviews you until it understands it, writes the docs, builds the MVP, then ships and grows it, with you as CEO approving every gate.

[Quick start](#-quick-start) · [Your AI agent](#-works-with-your-ai-agent) · [The flow](#-the-flow) · [The company](#-the-company) · [How it works](#-how-it-works) · [Tracks](#-tracks) · [Model routing](#-smart-model-routing) · [Usage](#-usage) · [Toolkit](#-toolkit) · [FAQ](#-faq)

</div>

---

Your agent can write code. pro-build gives it a **company**: it asks before it builds, writes the documents a real team writes, builds test-first through pull requests, checks its work with evidence, ships with a rollback plan, and measures what happens after launch. You are the CEO and approve every gate.

```text
interview → brief → validate → spec → architecture → design → pipeline → MVP → QA → release → launch → grow
```

Instead of explaining that process in every prompt, you install it once and start every project with one line.

## 📦 What's inside

**72 agents · 328 skills · 99 commands** from ECC, installed from the same marketplace, plus pro-build's own **11 departments**, **119 skills wired into the workflow** and **8 commands**.

| | 🤖 Agents | 🧩 Skills | ⌨️ Commands |
|:--|--:|--:|--:|
| **Built into pro-build** | **11** department agents (Kickoff + 10 departments), plus helper agents on 4 model tiers | **1** skill (`pro-build`) with **23** playbooks | **8** |
| **Used by the workflow** | Helper agents for self-contained work: search, builds, reviews, audits | **119** named skills from 13 plugins, each checked by CI | Spec-kit and plugin commands when enabled |
| **Comes with ECC** (same marketplace, required in Claude Code) | **72** | **328** | **99** |

<sub>ECC counts are from the latest ECC at the time of writing; ECC is installed from its official repository, so you get whatever it has now. The department agents are roles the AI plays in your main session, each with its own playbook and gate; self-contained work goes to helper agents (subagents) on the cheapest model that does it well.</sub>

| Included | Count | What it gives you |
|:--|--:|:--|
| **Agents** (from ECC) | 72 | Specialist agents for planning, architecture, code review, security, build repair, testing and documentation ([ECC](https://github.com/affaan-m/ECC)) |
| **Skills** (from ECC) | 328 | TDD, research, security, frontend, backend, data, DevOps, SEO, operations and more ([ECC](https://github.com/affaan-m/ECC)) |
| **Commands** (from ECC) | 99 | Entry points such as `/plan`, `/code-review`, `/feature-dev`, `/quality-gate` and `/security-scan` ([ECC](https://github.com/affaan-m/ECC)) |
| **Departments** (AI roles) | 11 | Kickoff plus 10 company departments. The AI plays each role in turn: discovery lead, founder advisor, Head of Product, CTO, Head of Design, platform engineer, engineering team, QA lead and security officer, release manager, Head of Growth, COO ([the company](#-the-company)) |
| **Approval gates** | 11 | One per department. Four are CEO decisions: **Brief**, **Go / no-go**, **Production go**, **Launch go** |
| **Helper agents** (model tiers) | 4 | Self-contained work goes to a helper agent on the cheapest model that does it well: Haiku, Sonnet, Opus, Fable (opt-in) ([model routing](#-smart-model-routing)) |
| **Skills wired into the workflow** | 119 | Named by pro-build's playbooks, from 13 plugins: ECC 68, marketing 22, Vercel 6, Claude SEO 5, PostHog 4, Sentry 3, Stripe, Supabase, Cloudflare and claudex-loop 2 each, Figma, REA and Taste 1 each. CI checks every name against the real skill list ([toolkit](#-toolkit)) |
| **pro-build commands** | 8 | Start, resume, status, jump to a stage, feature, release, launch, review ([usage](#-usage)) |
| **Playbooks** | 26 | 10 department playbooks, 3 project-type playbooks (web, system, app) and 13 shared guides: Kickoff, authorization, **Claude + Codex cross-review**, **payments by country**, **App Store and Google Play rules**, DevOps, model routing, toolkit, spec-kit, reverse engineering, project kit, build state, other agents |
| **Project types** | 3 | 🌐 Web · ⚙️ System · 📱 App, each with its default stack, quality bar and its own Kickoff questions |
| **Tracks** | 4 | Startup · Product · Client site · Existing project ([tracks](#-tracks)) |
| **Company documents** | up to 28 | Brief, validation, PRD, roadmap, architecture, decision records, plan, design, CI, runbook, launch readiness, release notes, go-to-market plan, weekly reviews… ([full list](skills/pro-build/references/project-kit.md)) |
| **Operating rules** | 16 | Always on: real gates, evidence over claims, test mode first, ask before assuming, nothing changes production unattended… |
| **Authorization levels** | 3 | **A** the agent may do it · **B** only after your yes for that exact action · **C** only you ([who may do what](#who-may-do-what)) |
| **AI agents supported** | 7 | Claude Code, Codex, Kimi Code, Gemini CLI, Grok Build, OpenCode, Cursor ([your AI agent](#-works-with-your-ai-agent)) |
| **Eval scenarios** | 34 | Behavioural tests run in an isolated, read-only session, plus a structural checker on every push ([`evals/`](evals)) |

---

## ✨ Why pro-build?

AI agents can write a lot of code fast. Real products also need everything around the code: checking the idea is worth building, a spec, an architecture, a design system, CI/CD, environments, monitoring, payments, a launch and a growth loop. That missing work is why most AI-built projects never earn a cent.

**pro-build gives Claude Code the structure of a startup.** Each department has a playbook, uses best-in-class tools, produces real artifacts and ends at a gate that only you can approve.

- 🎤 **Understands before it builds, and asks a lot.** A deep Kickoff interview: rounds of 3–5 clickable questions (typically 5–8 rounds), covering purpose, users, a measurable goal, scope, money, data, constraints, risks and trade-offs, plus questions specific to web, system or app projects. A coverage checklist makes sure every critical answer comes from **you**, never a guess. In a hurry? The fast lane asks only the critical items.
- 🧭 **Validates first.** Founder Office interviews you, researches the market and competitors, and recommends **go, pivot or stop** before any code is written.
- 📐 **Plans like a product team.** A PRD with success metrics, an architecture with decision records, and a final **readiness review by Codex** that tells you plainly: **ready to build, or not**.
- 🎨 **Designs with taste.** A visual direction and design system that don't look AI-generated.
- 🏭 **Builds the factory first.** Repository, CI, preview, staging and production environments, error monitoring, analytics and payments are wired up *before* the first feature.
- 🧪 **Ships safely.** Test-driven features through pull requests, QA and security gates, staged releases, rollback plans and canary monitoring.
- 💰 **Launches to earn.** Positioning, landing-page conversion, pricing and paywall, SEO, a funnel, lifecycle emails and a live-payments checklist.
- 🧠 **Routes every task to the right model.** Haiku for mechanical work, Sonnet for building, Opus for strategy and security, and Fable (opt-in) for the hardest reviews. Top quality where it matters, fewer tokens everywhere else.
- 📏 **Spec-driven when it matters.** Every plan gets a consistency check (requirement → task traceability), every milestone runs until it converges with the spec, and large features can use [GitHub spec-kit](https://github.com/github/spec-kit) mode.
- 🧯 **Production-grade safety.** One authorization matrix, protected production deploys, approvals tied to an exact build, required QA evidence per release class, real secret scanning with key rotation, tested backups, and an incident runbook.
- ♾️ **Full DevOps loop.** Reliability targets (SLOs) with error budgets, DORA delivery metrics in every weekly review, optional infrastructure as code (Terraform or Pulumi) and container paths, always-on watching (an uptime monitor, scheduled read-only CI checks, an optional daily AI health report) and on-call paging. Automation watches and pages; it never changes production unattended.
- 🔬 **Audits what you actually ship.** With [REA](https://github.com/morluto/rea), QA scans your production build for leaked secrets and source maps, Release diffs each build against the last, and Founder Office can study how competitors' public apps work (to learn, never to copy).
- 🔎 **SEO from day one.** Site structure in Design, technical SEO in the scaffold, an SEO and AI-search audit in QA, and a content and ranking engine at launch.
- 📈 **Runs on numbers.** Weekly operating reviews of metrics, revenue and errors, which decide what to build next.
- 🛡️ **Keeps you in charge.** Live payments, production deploys, purchases and publishing always stay with you.

---

## 🚀 Quick start

> Using **Codex, Kimi, Gemini, Grok, OpenCode or Cursor**? Jump to [Works with your AI agent](#-works-with-your-ai-agent). The steps below are for **Claude Code**, where pro-build has the most automation.

**1. Add the pro-build marketplace and install both plugins.** Inside Claude Code:

```text
/plugin marketplace add saeedkhoury/pro-build
/plugin install ecc@pro-build
/plugin install pro-build@pro-build
```

One marketplace gives you everything: **pro-build** plus **ECC** (72 agents, 328 skills, 99 commands, hooks and rules), which pro-build runs on. ECC is installed from [its official repository](https://github.com/affaan-m/ECC), so you always get the latest version, with its MIT license and its author's credit.

> [!IMPORTANT]
> Already have ECC from its own marketplace (`ecc@ecc`)? Skip `ecc@pro-build`: installing both gives you every ECC tool twice.

**2. Add the company services you want** (recommended, from the official plugin directory):

```text
/plugin install stripe@claude-plugins-official      # only if Stripe supports your business's country
/plugin install supabase@claude-plugins-official
/plugin install vercel@claude-plugins-official
/plugin install sentry@claude-plugins-official
/plugin install posthog@claude-plugins-official
/plugin install semgrep@claude-plugins-official
```

**3. Open a new session and found your company:**

```text
/pro-build:pro-build "a SaaS that turns meeting recordings into action items"
```

> [!TIP]
> Services such as Stripe and Vercel need a one-time sign-in through `/mcp`. pro-build tells you when a stage needs one, and works around anything that isn't connected yet.

---

## 🎬 Walkthrough: from one sentence to a live app

What actually happens after you type one line. The example is a barber booking app; websites and systems follow the same path with their own questions.

### Step 1 · Kickoff: it asks before it builds anything

```text
You:  /pro-build:pro-build "I wanna build barber app"

pro-build:  I understand: an app for barbers and their customers. It looks like an App (mobile)
            plus a System (a backend for bookings).
            Known: booking for barbers. Unknown: who it's for, how it earns money, which platforms.

            1. Who is it for?   a) one barbershop  b) many shops (a platform)  c) customers looking for a barber
            2. What's the goal, as a number?   (for example: 200 bookings a month within 3 months)
            3. How does it earn money?   a) monthly subscription for shops  b) fee per booking  c) a client project
            4. iPhone, Android or both? Through the app stores, or as a web app (PWA)?
            5. Do customers pay in the app, or at the shop?

            More rounds will follow. I'll write a Project Brief before any documents or code.
```

- **You answer.** A vague answer ("everyone", "not sure") gets a follow-up question with options. It is never taken as final.
- **Rounds 2–4** cover the budget and deadline, who maintains the app, the data you store and how sensitive it is, languages, offline use, notifications, cancellation rules, and what is out of scope for version 1.
- **Critical items are never defaulted**: the users, a numeric goal, the business model, budget and deadline, and who maintains it. Non-critical items can use the AI's recommendations, listed as **assumptions**.
- The AI shows a one-page **Project Brief** with a coverage checklist. You reply `approved` → ✅ **Gate: Brief approved**.
- It recommends a **track** (Startup for your own product, Client site for a client's website) and asks your **model policy**, including whether to allow Fable.

### Step 2 · The company stages, one after another

| Stage | AI plays | What it produces for the barber app | Your gate |
|:--|:--|:--|:--|
| **0 Founder Office** | Founder advisor | Market and competitors (Booksy, Fresha), pricing, risks: is it worth building? | ✅ **Go / no-go** |
| **1 Product** | Head of Product | The **PRD**: R1 sign-up, R2 barber profile and services, R3 book a slot, R4 reminders, R5 payments, each with acceptance criteria; a milestone plan | ✅ Spec |
| **2 Engineering Leadership** | CTO | **Architecture**: for example Expo (iOS and Android), Supabase (database and login), a payment provider for your country (Stripe where it's supported; in Israel a local provider with Bit), push notifications, hosting, monthly cost, and which services aren't needed. Then Codex reviews the whole package (PRD, roadmap, architecture, plan) and the briefing says **READY TO BUILD** or **NOT READY** | ✅ Architecture + readiness verdict |
| **3 Design** | Head of Design | Screens: home, barber list, service, time, confirm, my bookings, barber dashboard; platform design rules and accessibility | ✅ Design |
| **4 Platform / DevOps** | Platform engineer | GitHub repository, CI that tests every change, staging and production, secrets, error monitoring | ✅ Pipeline green |
| **5 Engineering** | Engineering team | Feature by feature: tests first, then code, then a **dual review** (Claude reviews, Codex inspects), pull request | ✅ **Your yes for each merge** |
| **6 QA & Security** | QA lead + security officer | End-to-end tests, a double-booking test, security scan, secret scan, real devices | ✅ No blocking findings |
| **7 Release** | Release manager | Builds and signs the app, runs QA on **those exact files**; **you** submit them to the stores; phased rollout and a halt plan | ✅ **Production go** |
| **8 Go-to-Market** | Head of Growth | Store listing, screenshots, landing page, launch messages for barbershops | ✅ **Launch go** |
| **9 Operate & Grow** | COO / analyst | Weekly review: bookings, crashes, uptime, delivery metrics, the next thing to build | ✅ Next-cycle plan |

### Step 3 · A normal working day (stage 5)

```text
You:  /pro-build:pro-build

pro-build:  We're on stage 5, task T4 "Booking screen" (R3).
            Acceptance: a customer picks a service and a time, and can't double-book.
            Branch feat/booking: tests first, then the code.
            …
            PR #7 is ready: CI ✅ · Claude review ✅ · Codex inspection ✅ (2 findings fixed).
            Merging deploys to staging only. Merge PR #7?

You:  yes, merge PR #7
```

A vague reply such as "looks good" is not enough: it asks you to confirm clearly.

### Step 4 · What the AI never does by itself

| Action | Who does it |
|:--|:--|
| Write code, tests and documents | The AI |
| Merge a pull request | The AI, only after your clear yes for that pull request |
| Deploy to production, submit to the stores, email users | **You**: the AI gives copy-ready steps, then verifies |
| Spend money, rotate keys, accept terms, create accounts | **You** |
| Change production automatically on a schedule | Nobody: automation only watches and pages |

**In short:** you give the idea and answer the questions; the AI writes the documents and the code; you approve every gate and do the production steps yourself.

---

## 🤖 Works with your AI agent

pro-build is a standard **[Agent Skill](https://agentskills.io)**: one `SKILL.md` folder that any agent supporting the open standard can load. Its process (the deep Kickoff interview, ten departments, gates, authorization matrix, evidence rules and playbooks) is plain Markdown and works the same in every agent. Only some mechanics differ, and pro-build adapts them itself ([`references/agents.md`](skills/pro-build/references/agents.md)).

### Install in one command (any agent)

```bash
npx skills add saeedkhoury/pro-build                 # pick your agent(s) interactively
npx skills add saeedkhoury/pro-build -a codex        # or name one: claude-code, codex, kimi-code-cli,
                                                     # gemini-cli, grok, opencode, cursor, …
```

[`skills`](https://github.com/vercel-labs/skills) installs into the right folder for 80+ agents. Or clone this repository and run `./install.sh <agent>`.

### Agent by agent

| Agent | Install | Start a project | Status |
|:--|:--|:--|:--|
| <img src="https://cdn.simpleicons.org/claude" width="20" height="20" alt="Claude Code logo"> **Claude Code** | Plugin: `/plugin marketplace add saeedkhoury/pro-build` then `/plugin install pro-build@pro-build`, or `./install.sh claude` | `/pro-build:pro-build "idea"` (plugin) or `/pro-build "idea"` | ✅ **Tested**: full automation |
| <img src="https://github.com/openai.png?size=40" width="20" height="20" alt="Codex logo"> **Codex** (OpenAI) | `npx skills add saeedkhoury/pro-build -a codex`, or `./install.sh codex` (`~/.agents/skills`). A `.codex-plugin/plugin.json` is included for Codex plugin packaging | `$pro-build`, or "Use the pro-build skill: idea" | ✅ **Tested**: loads the skill and runs Kickoff |
| <img src="https://cdn.simpleicons.org/kimi" width="20" height="20" alt="Kimi Code logo"> **Kimi Code CLI** (Moonshot) | `npx skills add saeedkhoury/pro-build -a kimi-code-cli`, or `./install.sh kimi` (`~/.agents/skills`) | "Use the pro-build skill: idea" | 📘 Supported by the standard; not yet tested |
| <img src="https://cdn.simpleicons.org/googlegemini" width="20" height="20" alt="Gemini CLI logo"> **Gemini CLI** (Google) | `npx skills add saeedkhoury/pro-build -a gemini-cli`, or `./install.sh gemini` (`~/.gemini/skills`) | "Use the pro-build skill: idea" | 📘 Supported by the standard; not yet tested |
| <img src="https://github.com/xai-org.png?size=40" width="20" height="20" alt="Grok Build logo"> **Grok Build** (xAI) | `npx skills add saeedkhoury/pro-build -a grok`, or `./install.sh grok` (`~/.grok/skills`) | "Use the pro-build skill: idea" | 📘 Supported by the standard; not yet tested |
| <img src="https://cdn.simpleicons.org/opencode" width="20" height="20" alt="OpenCode logo"> **OpenCode** | `npx skills add saeedkhoury/pro-build -a opencode`, or `./install.sh opencode` (`~/.config/opencode/skills`) | "Use the pro-build skill: idea" | 📘 Supported by the standard; not yet tested |
| <img src="https://github.com/cursor.png?size=40" width="20" height="20" alt="Cursor logo"> **Cursor** | `npx skills add saeedkhoury/pro-build -a cursor`, or `./install.sh cursor` (`~/.cursor/skills`) | "Use the pro-build skill: idea" | 📘 Supported by the standard; not yet tested |

For a single project instead of every project, put the skill in the project's `.agents/skills/pro-build/` folder (or `.claude/skills/` for Claude Code, `.grok/skills/` for Grok).

### What's the same, and what adapts

| | <img src="https://cdn.simpleicons.org/claude" width="18" height="18" alt="Claude Code logo"> Claude Code | Other agents |
|:--|:--|:--|
| Deep Kickoff interview and critical questions | ✅ Clickable options | ✅ Numbered questions with lettered options |
| Ten departments, gates and CEO briefings | ✅ | ✅ Identical |
| Authorization matrix (what only you may do) | ✅ | ✅ Identical, even in auto-approve modes |
| `BUILD-STATE.md` and `docs/company/**` | ✅ | ✅ Identical, so you can switch agents mid-project |
| Named workflow skills (ECC and others) | ✅ Through plugins | Used when installed for your agent; otherwise the step is done directly |
| Model routing | ✅ Haiku, Sonnet, Opus, Fable (opt-in) | Mapped to your agent's own cheap, default and strongest tiers |
| Stripe, Supabase, Vercel, Sentry, PostHog | ✅ Official plugins | Through the vendor's MCP server or CLI if configured |
| Readiness review and dual code review | ✅ Codex reviews the plan and inspects every pull request (claudex-loop) | The other provider reviews (in Codex: Claude), if available; otherwise labelled same-provider |

> [!NOTE]
> "Tested" means a fresh session found pro-build in the agent's skills folder, ran the Kickoff interview and wrote no files before the brief was approved. Kimi, Gemini, Grok, OpenCode and Cursor follow the same Agent Skills standard and folder conventions; reports from users of those agents are welcome.

---

## 🧭 The flow

```text
You:  /pro-build:pro-build "an app that helps gyms manage memberships"

1. Kickoff        → asks 3–5 questions per round: purpose, goal, users, must-haves,
                    platform, business model, data, constraints, references
                  → "Here's what I understood" → a Project Brief you approve
                  → recommends a track (Startup / Product / Client site / Existing)
2. Documents      → validation · PRD · roadmap · architecture · decision records
                    · implementation plan (M1 = MVP) · design system
3. Factory        → repository · README · CLAUDE.md · .env.example · CI/CD
                    · preview / staging / production · monitoring · analytics · payments
4. MVP            → builds milestone M1 test-first, checks it against the spec
                    until nothing is missing ("converged"), then shows you the running app
5. Ship           → QA and security gate → staged release → canary watch
6. Sell and grow  → landing page, pricing, SEO, launch → weekly metrics reviews
```

### Every project gets

| Docs | Engineering | Operations |
|:--|:--|:--|
| Project Brief | `README.md` | `BUILD-STATE.md` (the company's memory) |
| Market validation | `CLAUDE.md` (rules for future AI sessions) | Platform runbook (deploy and rollback) |
| PRD and roadmap | `.env.example` | Launch-readiness report |
| Architecture and decision records | CI workflow and pull-request template | Release notes and `CHANGELOG.md` |
| **Implementation plan (M1 = MVP)** | Test suite | Go-to-market plan |
| Design system | | Weekly operating reviews |

The full list, and which stage creates each file: [`references/project-kit.md`](skills/pro-build/references/project-kit.md).

---

## 🧩 Built for every kind of project

Kickoff identifies what you're building, and every later stage follows the matching playbook: the best default stack, how to choose alternatives, the tools for each stage, a quality bar, and its own Kickoff questions.

| Type | Best default | Playbook |
|:--|:--|:--|
| 🌐 **Web**: sites, e-commerce, SaaS, portals | Astro for content sites · Next.js + Supabase + a payment provider for your country on Vercel for apps · Shopify for standard stores | [`web.md`](skills/pro-build/references/project-types/web.md) |
| ⚙️ **System**: APIs, backends, workers, data, integrations | Contract-first TypeScript or FastAPI + Postgres; a modular monolith first; Go for high throughput | [`system.md`](skills/pro-build/references/project-types/system.md) |
| 📱 **App**: iOS, Android, desktop | Expo (React Native) cross-platform; SwiftUI or Kotlin/Compose when native features demand it; Tauri for desktop | [`app.md`](skills/pro-build/references/project-types/app.md) |


### 💳 Payments that work in your country

Stripe isn't available everywhere (for example, not for businesses registered in **Israel**). Kickoff asks **where the business is registered, where the customers are, and what you sell**, and stage 2 picks the provider ([`payments.md`](skills/pro-build/references/payments.md)):

| You sell | pro-build recommends |
|:--|:--|
| Digital features inside a mobile app | **Apple In-App Purchase and Google Play Billing** (required by the stores), managed with RevenueCat |
| Physical goods or real-world services (bookings, deliveries) | A normal payment provider. Never store in-app purchase |
| Anything, from a country Stripe supports | **Stripe** |
| SaaS or digital products, from a country Stripe doesn't support | A merchant of record such as **Paddle** or **Polar** (they also handle VAT) |
| To local customers, from a country Stripe doesn't support | A **local provider**. In Israel: Tranzila, CardCom, PayPlus or Grow (Bit, Israeli cards, instalments, ILS, invoices) |

It records the choice, the alternative and the official page it checked, and every later stage uses it. Going live stays your action.

### 🤝 Claude + Codex check each other

With [claudex-loop](https://github.com/chaseai-yt/claudex-loop) and a signed-in Codex CLI, two AI providers review the work ([`cross-review.md`](skills/pro-build/references/cross-review.md)):

| When | What happens | What you get |
|:--|:--|:--|
| **End of stage 2** | Codex reviews the complete package (PRD, roadmap, architecture and plan) for up to 3 rounds; Claude fixes or answers each finding | A plain verdict: ✅ **READY TO BUILD**, ⏳ **NOT READY** (with the open findings), ⚠️ **UNREVIEWED** (your override) or 🚫 **REVIEW BLOCKED**. The approval is tied to the exact documents: change one, and it must be re-checked before building |
| **Every pull request** (stage 5) | Claude reviews the code (`ecc:code-review`), and a fresh Codex session inspects the same branch | One findings table, fixes, a fresh re-inspection, then the merge question with both results. Without Codex, the PR is labelled *single review*, and risky changes (auth, payments, migrations, security) wait for Codex or your explicit override |

In Codex, the roles swap: Codex builds, and Claude reviews. Set `Dual review: risky only` in `BUILD-STATE.md` to save Codex credits.

### 📱 App Store and Google Play rules

For mobile apps, [`app-stores.md`](skills/pro-build/references/app-stores.md) covers what gets apps rejected or blocked: developer accounts (personal or organization, D-U-N-S), Google's **12-tester, 14-day closed test** for new personal accounts, the current upload floors (**Xcode 26 and the iOS 26 SDK; target API 36**), in-app purchase rules, **account deletion**, Sign in with Apple, privacy labels and the Data safety form, user-generated content, and review notes with a demo account. Stage 6 runs its checklist, stage 7 prepares the store package, and you submit. Before each submission it re-checks the official pages, because the rules change every year.

---

## 🏢 The company

| # | Department | Role | What it delivers | Gate |
|:--:|:--|:--|:--|:--|
| K | **Kickoff** | Discovery lead | Adaptive interview, Project Brief, track recommendation | **Brief approved** |
| 0 | **Founder Office** | Founder advisor | Customer interview, market and competitors, pricing hypothesis, risks, demand test | **Go / pivot / stop** |
| 1 | **Product** | Head of Product | PRD, MVP scope, North Star and input metrics, roadmap and backlog | Spec approved |
| 2 | **Engineering Leadership** | CTO | Stack, data and auth model, decision records, cost estimate, implementation plan, Codex **readiness review** (ready to build or not) | Architecture and plan approved |
| 3 | **Design** | Head of Design | Visual direction, design tokens, components, key screens | Design approved |
| 4 | **Platform / DevOps** | Platform engineer | Repository, README, CLAUDE.md, CI, preview, staging and production, Supabase, Sentry, PostHog, payments in test mode (provider chosen by country) | Pipeline green |
| 5 | **Engineering** | Engineering team | MVP (milestone M1), then test-driven features, one pull request at a time | MVP demo, then each merge |
| 6 | **QA & Security** | QA lead + security officer | End-to-end, browser, accessibility, security, performance, coverage, privacy | No blocking findings |
| 7 | **Release** | Release manager | Versioning, release notes, staging smoke test, rollback plan, canary watch | **Production go** |
| 8 | **Go-to-Market** | Head of Growth | Positioning, landing page, pricing and paywall, SEO, funnel, emails, launch plan, live payments | **Launch go** |
| 9 | **Operate & Grow** | COO / analyst | Weekly metrics, revenue and error review, retro, experiments, roadmap | Next cycle approved |

Each department has its own playbook in [`skills/pro-build/references/departments/`](skills/pro-build/references/departments), which Claude loads only when that stage starts.

---

## 🔄 How it works

```mermaid
flowchart LR
    Idea([💡 Idea]) --> K[K · Kickoff interview]
    K --> GK{Brief OK?}
    GK -- revise --> K
    GK -- yes --> D0[0 · Founder Office]
    D0 --> G0{Go?}
    G0 -- stop --> X([Saved you months])
    G0 -- pivot --> D0
    G0 -- go --> D1[1 · Product]
    D1 --> D2[2 · Eng Leadership]
    D2 --> D3[3 · Design]
    D3 --> D4[4 · Platform / DevOps]
    D4 --> D5[5 · Engineering]
    D5 --> D6[6 · QA & Security]
    D6 --> D7[7 · Release]
    D7 --> G7{Prod go?}
    G7 -- yes --> D8[8 · Go-to-Market]
    D8 --> G8{Launch go?}
    G8 -- yes --> D9[9 · Operate & Grow]
    D9 -- next feature --> D5
    D9 -- big change --> D1
```

Every department ends at a gate: Claude shows the artifacts, the checklist and the risks, then asks you to **approve, revise or stop**.

### CEO briefings

Every gate is presented as a one-minute CEO briefing: **decision needed · what we produced · key numbers · top risks · recommendation · approve / revise / stop.**

### Who may do what

One [authorization matrix](skills/pro-build/references/authorization.md) governs every stage. **A:** the agent may do it (code, tests, pull requests, preview and staging deploys). **B:** the agent may do it only after your specific yes for that exact action, which is logged (merging a pull request, promoting a named build to production, a pre-approved rollback). **C:** only you do it; the agent prepares the steps, waits and verifies (see below). Merges deploy to **staging only**, so nothing reaches production without a release-specific approval.

### What stays with you (the CEO)

pro-build prepares these and explains each one, but never does them for you:

- Switching payments to **live mode** or entering live keys
- The **first production deploy** and production database migrations
- **Buying** domains or plans, and accepting terms
- **Publishing**, posting, emailing customers, app-store submissions and pushing public repositories
- **DNS** changes, **rotating** leaked credentials, and deleting production data
- **Creating accounts** and signing in to services

---

## 🛤️ Tracks

Not every project needs the whole company. Pick a track at the start:

| Track | Best for | Departments |
|:--|:--|:--|
| 🚀 **Startup** | SaaS, apps or marketplaces meant to make money | All, 0 → 9 |
| 🧰 **Product** | Internal tools, portfolio projects, non-commercial apps | 1 → 7, then 9 |
| 🌐 **Client site** | Professional websites for businesses and people | Brief → 1 → 3 → 4 → 5 → 6 → 7 → SEO and conversion |
| 🏗️ **Existing project** | A codebase that already exists | Audit, then join at Engineering or Operate & Grow |

---

## 🧠 Smart model routing

The main conversation (your `/model`) talks with you and runs the gates. Self-contained work is handed to helper agents on the **cheapest model that does it well**:

| Model | Gets | Examples |
|:--|:--|:--|
| ⚡ **Haiku** | Mechanical, low-risk work | Codebase search, summaries, formatting, boilerplate, changelogs, status reports, meta tags |
| 🛠️ **Sonnet** (default) | Building and writing | Features, tests, refactors, CI/CD, PRD drafts, copy, SEO implementation |
| 🧠 **Opus** | Decisions where mistakes are expensive | Strategy, pricing, architecture, security review, hard bugs, risky reviews |
| 💎 **Fable** (opt-in) | The hardest reasoning | Deciding the readiness review's findings, major-release review. Off by default, because it may use paid credits |

Rules: start cheap and escalate one tier on failure; never below Sonnet for payments, auth, security or data migrations; delegate only big chunks (each helper has a start-up cost); and run the main session on Sonnet day to day. That last one is the biggest saving. Full table per department: [`references/model-routing.md`](skills/pro-build/references/model-routing.md).

> [!NOTE]
> Verified in a live test: given a mechanical task, a fresh session handed it to a helper agent, and Claude Code's usage report showed it ran on Haiku.

---

## 📏 Spec-kit mode

For large features, pro-build can hand the feature-level work to [GitHub spec-kit](https://github.com/github/spec-kit), while keeping the company docs, branches and gates:

```text
feat/<name> branch → /speckit-specify (from the PRD) → /speckit-clarify → /speckit-plan (within the architecture)
→ /speckit-tasks → /speckit-analyze → /speckit-implement ⇄ /speckit-converge → pull request → your approval
```

Turn it on during Platform setup (stage 4) if `specify` is installed (`uv tool install specify-cli`). Without it, pro-build runs the same checks natively. Details: [`references/spec-kit.md`](skills/pro-build/references/spec-kit.md).

---

## 🕹️ Usage

| Command | What it does |
|:--|:--|
| `/pro-build:pro-build "<idea>"` | Found a new company project: pick a track, start the first stage |
| `/pro-build:pro-build` | Resume from `BUILD-STATE.md` |
| `/pro-build:pro-build status` | Stage, gates, services, metrics, risks and next step |
| `/pro-build:pro-build stage=<0-9>` | Jump to a department (warns about unapproved gates) |
| `/pro-build:pro-build feature "<what>"` | One Engineering cycle: branch, tests, code, review, pull request |
| `/pro-build:pro-build release` | Staging, smoke tests, rollback plan, production go, canary watch |
| `/pro-build:pro-build launch` | Run Go-to-Market |
| `/pro-build:pro-build review` | The weekly operating review |

Or just ask: *"Let's build this like a real company."*

> [!NOTE]
> Plugin skills are namespaced, so the command is `/pro-build:pro-build`. With the [manual install](#manual-install) it's `/pro-build`.

### Example

The full step-by-step example, from one sentence to a live app: [Walkthrough](#-walkthrough-from-one-sentence-to-a-live-app).

---

## 📒 BUILD-STATE.md and company docs

pro-build keeps the company's memory in your repository:

```text
BUILD-STATE.md                 # track, stage, gates, backlog, services, metrics, risks
docs/company/
  00-validation.md             # problem, market, competitors, pricing, go/no-go
  01-prd.md                    # spec, scope, success metrics, roadmap
  02-architecture.md  adr/     # stack, data model, decisions
  03-design/                   # direction, tokens, components, screens
  04-platform.md               # CI/CD, environments, services, secrets map, runbook
  06-launch-readiness.md       # QA and security report
  07-releases/                 # release notes and rollback plans
  08-gtm.md                    # positioning, pricing, funnel, launch plan
  09-reviews/                  # weekly operating reviews
```

Open any session, run `/pro-build:pro-build`, and it continues exactly where the company left off.

---

## 🧰 Toolkit

pro-build orchestrates other tools; it doesn't reinvent them.

| Layer | Tools |
|:--|:--|
| **Engine** (required) | [ECC](https://github.com/affaan-m/ECC): planning, test-driven development, orchestrated feature workflows, reviews, security, DevOps patterns, SEO, sessions |
| **DevOps** (optional) | [Terraform](https://github.com/hashicorp/terraform-mcp-server), PagerDuty or incident.io, Datadog or Grafana, an uptime monitor such as Better Stack ([`references/devops.md`](skills/pro-build/references/devops.md)) |
| **Payments** | [Stripe](https://github.com/stripe/ai) where it supports your country; otherwise Paddle or Polar (merchant of record), a local provider, or PayPal ([`payments.md`](skills/pro-build/references/payments.md)). Apple IAP and Google Play Billing for digital goods in mobile apps |
| **Backend** | [Supabase](https://github.com/supabase-community/supabase-plugin) |
| **Deploys** | [Vercel](https://github.com/vercel/vercel-plugin) or [Cloudflare](https://github.com/cloudflare/skills) |
| **Errors** | [Sentry](https://github.com/getsentry/plugin-claude) |
| **Analytics and experiments** | [PostHog](https://github.com/PostHog/ai-plugin) |
| **Security scanning** | [Semgrep](https://github.com/semgrep/mcp-marketplace) |
| **SEO** (optional) | [claude-seo](https://github.com/AgriciDaniel/claude-seo): audits, technical, local, clusters and AI search |
| **Growth** | [marketingskills](https://github.com/coreyhaines31/marketingskills): 53 skills for conversion, pricing, launch, SEO and retention |
| **Design taste** | [taste-skill](https://github.com/Leonxlnx/taste-skill) |
| **Reverse engineering** (optional) | [REA](https://github.com/morluto/rea): competitor teardowns, a release exposure audit of your own build, release diffs, and projects with lost source |
| **Spec-driven features** (optional) | [spec-kit](https://github.com/github/spec-kit) by GitHub: specify → clarify → plan → tasks → analyze → implement → converge |
| **Cross-review** | [claudex-loop](https://github.com/chaseai-yt/claudex-loop) (Claude ⇄ Codex): readiness review of the plan, and Codex inspection of every pull request ([`cross-review.md`](skills/pro-build/references/cross-review.md)) |

Only ECC is required. For anything missing, pro-build names the install command and uses a fallback; see [`references/toolkit.md`](skills/pro-build/references/toolkit.md).

> [!IMPORTANT]
> **Telemetry:** some vendor plugins send anonymous usage data by default. None of them send prompts or code. Turn it off with `VERCEL_PLUGIN_TELEMETRY=off` and `DO_NOT_TRACK=1` (Semgrep). Details are in the [toolkit notes](skills/pro-build/references/toolkit.md#telemetry-notes).

---

## ❓ FAQ

<details>
<summary><strong>Will this make my project earn money?</strong></summary>
<br>
No tool can promise that. What pro-build does is stack the odds: Founder Office tests demand <em>before</em> you build, Go-to-Market sets up the funnel and payments properly, and Operate & Grow measures what's actually happening every week. Many good outcomes are a "stop" at Gate 0 that saves you months.
</details>

<details>
<summary><strong>Isn't this too heavy for a small website?</strong></summary>
<br>
Use the <strong>Client site</strong> or <strong>Product</strong> track. pro-build compresses or skips departments and tells you exactly which ones and why.
</details>

<details>
<summary><strong>Can I use it on an existing project?</strong></summary>
<br>
Yes: choose the <strong>Existing project</strong> track. It audits the codebase, writes <code>BUILD-STATE.md</code>, and joins at Engineering or Operate & Grow.
</details>

<details>
<summary><strong>Do I need accounts for Stripe, Vercel, Sentry and the rest?</strong></summary>
<br>
Only for the services you use. Most have free tiers. pro-build starts everything in test mode and tells you when a sign-in is needed. You always do the sign-in yourself.
</details>

<details>
<summary><strong>Can I customise the departments?</strong></summary>
<br>
Yes. Each department is one readable Markdown playbook. Fork the repo, edit <a href="skills/pro-build/references/departments"><code>references/departments/</code></a> and install your fork.
</details>

---

## 🔧 Install options

### Plugin (recommended)

```text
/plugin marketplace add saeedkhoury/pro-build
/plugin install ecc@pro-build        # skip if you already have ecc@ecc
/plugin install pro-build@pro-build
```

Update with `/plugin marketplace update pro-build`. Remove with `/plugin uninstall pro-build@pro-build` (and `/plugin uninstall ecc@pro-build`).

### Any agent (`skills` CLI)

```bash
npx skills add saeedkhoury/pro-build -a <agent>
```

### Manual install

```bash
git clone https://github.com/saeedkhoury/pro-build.git
cd pro-build && ./install.sh <agent>     # claude (default), codex, kimi, gemini, grok, opencode, cursor
```

This copies the skill into that agent's global skills folder. In Claude Code the command becomes `/pro-build`; use the plugin **or** the manual install, not both.

---

## 🤝 Contributing

Ideas, playbook improvements and bug reports are welcome. Please open an issue first. Keep each department in one playbook file, and make sure every skill it names exists in a published plugin.

**Checks before a pull request:**

```bash
python3 evals/check.py                   # structure, references, contradiction rules (also runs in CI)
python3 evals/check.py --refresh-known   # after adding a skill reference (needs the plugins installed)
evals/run-behavioral.sh S05 S06 S07      # behavioural scenarios: isolated headless Claude Code (this checkout only, no plugins or MCP, read-only)
```

Grade the behavioural outputs against the **Expect** and **Never** columns in [`evals/scenarios.md`](evals/scenarios.md). Scenarios that need a realistic project use the fixtures in [`evals/fixtures/`](evals/fixtures) (`fixture:<name>` in the Setup column). Run all 30 scenarios before a release that changes `SKILL.md`, the authorization matrix or a gate.

## 🙏 Credits

pro-build stands on the shoulders of:

- [ECC (Everything Claude Code)](https://github.com/affaan-m/ECC) by Affaan Mustafa: the engine behind every department.
- [marketingskills](https://github.com/coreyhaines31/marketingskills) by Corey Haines, [taste-skill](https://github.com/Leonxlnx/taste-skill), and [claudex-loop](https://github.com/chaseai-yt/claudex-loop) by Chase AI.
- Official plugins from Stripe, Supabase, Vercel, Sentry, PostHog and Semgrep.
- [spec-kit](https://github.com/github/spec-kit) by GitHub: spec-driven development for large features, and the inspiration for the consistency and convergence checks.
- Ideas borrowed from [gstack](https://github.com/garrytan/gstack) (founder office hours, role-based reviews) and [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) (agile roles).

## 📄 License

[MIT](LICENSE) © 2026 Saeed Khoury
