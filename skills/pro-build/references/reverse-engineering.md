# Reverse engineering with REA

[REA](https://github.com/morluto/rea) ("Reverse Engineer Anything") inspects shipped software (websites, JavaScript and Electron apps, .NET assemblies, desktop apps and native binaries) and returns findings with evidence. pro-build uses it as an **optional** tool in four places.

Use the skill `rea:reverse-engineer-anything`; it drives REA's MCP tools. If the MCP server isn't connected, the CLI works without it: `npx -y rea-agents@<version> <command> --json`, where `<version>` is the one in the installed plugin's manifest.

## Rules: what may be analysed

1. **Only targets the user owns, or is authorised to analyse,** or that are publicly shipped and legitimately obtained (a public website, an app the user installed).
2. **Understand, don't copy.** Use findings to learn how something works and design your own version. Never copy a competitor's code, assets, text or design, and never reuse their API keys or private endpoints.
3. **No bypassing protections.** No breaking DRM, licence checks, paywalls, authentication, rate limits or anti-tamper measures. Respect terms of service and local law. If unsure, ask the user before analysing.
4. **Your own builds, freely.** Analysing your own release artifacts is always fine, and is the most valuable use.
5. **Evidence and limits.** Report REA's evidence and its stated limitations. Never present an inference as fact.

## Where it's used

| Stage | Use | REA commands | Model |
|:--|:--|:--|:--|
| **0 Founder Office** | **Competitor teardown** (optional): how a competitor's public web app or installed desktop app implements the feature that matters most, such as onboarding, pricing logic or main flows. Summarise the patterns, then design your own | `analyze-web-bundle` (public site), `capture-browser-scenario` (a public flow), `analyze-javascript-application` (an installed Electron app) | sonnet runs it · opus draws the conclusions |
| **6 QA & Security** | **Release exposure audit** (recommended when available): scan your own built app or site for what an attacker could recover, such as source maps, credential markers, debug companions, internal routes and endpoints | `audit-release-exposure` on the build output (`.next`, `dist`, `.app`, ASAR, executable); `analyze-web-bundle` on the staging URL; `compare-static-and-observed-endpoints` with a HAR from staging | sonnet runs it · opus triages findings |
| **7 Release** | **Release diff**: confirm only the intended changes shipped between the previous and new build | `compare-application-versions` (JavaScript and Electron), `compare-artifacts` (other artifacts) | haiku runs it · sonnet reviews |
| **Existing project track** | **Lost or missing source**: understand an app when the source is gone or incomplete before rebuilding it, or check that the deployed bundle matches the repository | `analyze-javascript-application`, `compare-source-to-bundle`; native binaries need Ghidra, Hopper, IDA or Kuna | opus |

## Results

- Stage 0 findings go in `docs/company/00-validation.md` under "Competitor teardown": patterns and evidence, no copied code.
- Stage 6 findings go in `docs/company/06-launch-readiness.md` under "Release exposure". **Blocking** when a check is `exposed`: `text.credential_markers` (a key or secret pattern in the shipped files) and `javascript.source_map_sources` (original source recoverable from source maps). Other `exposed` checks are advisory unless they reveal internal endpoints or data. `unknown` and `not_assessed` checks stay in the report as they are; they don't mean the app is secure.
- Stage 7 diffs go in `docs/company/07-releases/<version>.md`.

## Requirements and fallbacks

| Needs | Notes |
|:--|:--|
| The REA plugin | `/plugin marketplace add morluto/rea` then `/plugin install rea@rea` |
| Node.js 22.23.4+, 24.22.1+ or 26.12.1+ | REA refuses older versions |
| Native analysis | Ghidra, Hopper, IDA or Kuna installed separately. Websites, JavaScript and Electron apps, and .NET work without them |
| **If REA isn't available** | Stage 6: check the build output by hand (`find . -name "*.map"`, grep for key prefixes) and use `ecc:security-scan`. Stage 0: use public information only. Stage 7: compare git tags and changelogs. Mark the step "REA not available" |
