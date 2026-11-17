# Toolkit

Every tool pro-build uses, by department. If a skill is missing, give the user its install line and continue with a fallback (operating rule 7).

## Required

| Tool | Used in | Install (inside Claude Code) |
|:--|:--|:--|
| ECC: Everything Claude Code | Every stage | `/plugin marketplace add affaan-m/ECC` then `/plugin install ecc@ecc` |
| Git and the GitHub CLI (`gh`) | 4–9 | `brew install git gh`, then `gh auth login` (the user signs in) |

## Recommended: company services (official Claude plugin directory)

These plugins connect to hosted services; each needs the user to sign in once (run `/mcp` in Claude Code). Install with `/plugin install <name>@claude-plugins-official`.

| Plugin | Department | What it does | Account |
|:--|:--|:--|:--|
| `stripe` | 4, 8, 9 | Payments, subscriptions, billing best practices | Stripe (start in test mode) |
| `supabase` | 2, 4 | Postgres, auth, storage, row-level security | Supabase |
| `vercel` | 4, 7 | Deploys, previews, environments, Next.js | Vercel |
| `sentry` | 4, 5, 7, 9 | Error monitoring, releases, alerts | Sentry |
| `posthog` | 1, 4, 8, 9 | Product analytics, funnels, feature flags, experiments | PostHog |
| `semgrep` | 4, 6 | Security scanning while coding | Semgrep (free login) |
| `figma` | 3 | Design files and handoff (optional) | Figma |
| `cloudflare` | 4, 7 | Alternative hosting: Workers, Pages, R2, D1 | Cloudflare |

## Recommended: community skills

| Plugin | Department | Install |
|:--|:--|:--|
| marketingskills (53 growth skills) | 0, 8, 9 | `/plugin marketplace add coreyhaines31/marketingskills` then `/plugin install marketing-skills@marketingskills` |
| taste-skill (design taste) | 3 | `/plugin marketplace add Leonxlnx/taste-skill` then `/plugin install taste-skill@taste-skill` |
| claude-seo (SEO suite: audits, technical, local, clusters, AI search) | 4, 6, 8 | `/plugin marketplace add AgriciDaniel/claude-seo` then `/plugin install claude-seo@agricidaniel-claude-seo` |
| spec-kit (spec-driven mode for large features) | 4, 5 | Not a plugin: `uv tool install specify-cli` in the terminal, then pro-build runs `specify init` in the project during stage 4 |
| REA: reverse engineer anything (competitor teardown, release exposure audit, release diff, lost source) | 0, 6, 7, Existing | `/plugin marketplace add morluto/rea` then `/plugin install rea@rea` (needs Node 22.23.4+). Rules and commands: `references/reverse-engineering.md` |
| claudex-loop (cross-model plan review) | 2, 5 | `/plugin marketplace add chaseai-yt/claudex-loop` then `/plugin install claudex-loop@claudex-loop` (also needs the Codex CLI) |

## Fallbacks

| Missing | Do instead |
|:--|:--|
| claudex-loop or Codex | `ecc:council` or `ecc:santa-loop` for the independent review |
| taste-skill | `ecc:frontend-design-direction` alone, plus a strict "no generic AI look" self-check |
| marketingskills | `ecc:seo`, `ecc:brand-voice`, `ecc:content-engine` and `ecc:market-research` |
| claude-seo | `ecc:seo` and the marketingskills SEO skills |
| REA | Manual build-output checks (`*.map`, secret patterns) plus `ecc:security-scan`; public information only for competitors |
| spec-kit | Native mode: the stage 2 consistency check and the stage 5 convergence check |
| Fable off or unavailable | `opus` (see `references/model-routing.md`) |
| Vercel | Cloudflare (`cloudflare:wrangler`), or document a manual deploy |
| Supabase | Postgres via `ecc:postgres-patterns` and `ecc:database-migrations` |
| PostHog or Sentry not signed in | Add the SDKs with environment-variable placeholders; mark the gate check "blocked: sign-in needed" |

## Telemetry notes

Some vendor plugins send anonymous usage data by default; none send prompts or file contents:

- **Vercel:** daily ping plus Vercel skill names. Turn off with `VERCEL_PLUGIN_TELEMETRY=off`.
- **Semgrep:** hook timings and scanned file types. Turn off with `DO_NOT_TRACK=1`.
- **PostHog:** session analytics are off unless `POSTHOG_LLMA_CC_ENABLED=true` is set.
- **Stripe:** reports Stripe skill names through the Stripe CLI, if it is installed.
