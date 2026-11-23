# Running pro-build in other agents

pro-build is a standard **Agent Skill** (a `SKILL.md` folder), so any agent that supports Agent Skills can load it: Claude Code, Codex, Kimi Code CLI, Gemini CLI, Grok Build, OpenCode, Cursor and others. Its **process** (Kickoff, the ten departments, gates, the authorization matrix, evidence rules, the invalidation policy and the playbooks) is plain Markdown and works the same everywhere. A few **mechanics** are named after Claude Code's tools; adapt them as below.

## What changes outside Claude Code

| In the playbooks | In Claude Code | In other agents |
|:--|:--|:--|
| "Use `ecc:plan-prd`" (any `plugin:skill` name) | The Skill tool | If a skill with that name (or the part after the colon) is installed for your agent, use it. Otherwise do the step directly, following the playbook's intent (operating rule 7). Never invent a tool |
| AskUserQuestion (clickable options) | Built in | Ask the same rounds as numbered questions with lettered options; the user replies like `1a 2c 3b` |
| Model routing (`haiku`, `sonnet`, `opus`, `fable`) | The Agent tool's `model` parameter | Map the tiers to your agent's own: **cheap and fast** for mechanical work, **default** for building, **strongest or highest reasoning** for strategy, architecture and security. Delegate only if your agent supports subagents; otherwise work in the main session and change the reasoning effort when supported. Never go below the default tier for payments, auth or security |
| Vendor plugins (Stripe, Supabase, Vercel, Sentry, PostHog, Semgrep) | Claude Code plugins with MCP servers | Use the vendor's MCP server or CLI if your agent is configured for it (the user signs in; level C). Otherwise use the official docs, and mark steps that need the service as "blocked: connect <service>" |
| Independent plan review (`claudex-loop`) | Codex reviews Claude's plan | Use a **different** model or provider than the one that wrote the plan, if available (for example, in Codex, claudex-loop uses Claude as the reviewer). Otherwise run a structured self-review and say it wasn't independent |
| Scheduled AI watch (`/schedule`) | Claude Code routines | Your agent's scheduler, if it has one, or skip that layer. The uptime monitor and scheduled CI checks don't depend on the agent |
| `/pro-build "<idea>"` | A slash command | Use your agent's skill syntax (for example `$pro-build` in Codex), or just say: "Use the pro-build skill: <idea>" |

## What never changes

- **The authorization matrix** (`references/authorization.md`): level C stays with the user in every agent. If your agent runs in an auto-approve or "yolo" mode, pro-build's gates and level B and C rules still apply. The agent asks, waits, and doesn't treat the mode as approval.
- **Kickoff's critical questions,** the gates and CEO briefings, the evidence and invalidation rules, and rule 15 (automation never changes production unattended).
- **The files it writes:** `BUILD-STATE.md` and `docs/company/**` are the same, so a project can move between agents and continue with `pro-build`.

## Companion tools in other agents

- **ECC** (the engine behind many named skills) supports several agents, including Codex. See its README for install paths.
- **spec-kit:** `specify init --integration <agent>` (for example `codex`, `gemini` or `claude`); the `/speckit-*` names may differ per agent, so use the command names spec-kit installed.
- **REA:** `npx rea-agents setup` registers it for Claude Code, Codex, Cursor, Gemini CLI, Grok Build and others.
- **marketingskills and taste-skill** are Agent Skills too: `npx skills add coreyhaines31/marketingskills` or `npx skills add Leonxlnx/taste-skill`.
