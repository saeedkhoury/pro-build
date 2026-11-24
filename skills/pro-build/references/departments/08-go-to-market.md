# Stage 8: Go-to-Market

**Model routing:** launch decisions in the main thread · `opus` for positioning and pricing strategy · `sonnet` for copy, pages, emails and SEO work · `haiku` for meta tags, schema, sitemaps and directory submissions.

**Role:** Head of Growth. Turn a working product into one that people find, trust and pay for.

## Steps

1. **Positioning and messaging.** `marketing-skills:product-marketing` and `ecc:brand-voice`: who it's for, the main promise, proof points and objections.
2. **Landing page and conversion.** `marketing-skills:copywriting` and `marketing-skills:cro`: headline, social proof, a clear call to action. Then `marketing-skills:signup` and `marketing-skills:onboarding` so new users reach value fast.
3. **Pricing page and paywall.** `marketing-skills:pricing` and `marketing-skills:paywalls`, connected to the payment provider's prices (or the store's in-app products for mobile digital goods).
4. **SEO growth engine.** Foundations should already exist from stage 4. Now grow:
   - Keyword research and a content plan: `marketing-skills:content-strategy`, or `claude-seo:seo-plan` and `claude-seo:seo-cluster` if installed.
   - Audit and fix: `ecc:seo`, `marketing-skills:seo-audit` or `claude-seo:seo-audit`.
   - Pages that rank: `marketing-skills:programmatic-seo` (for template pages at scale) and `marketing-skills:competitor-profiling` (for comparison pages).
   - AI search visibility (ChatGPT, Perplexity, AI Overviews): `marketing-skills:ai-seo`.
   - Local businesses: `claude-seo:seo-local` if installed.
   - Submit the sitemap to Google Search Console and Bing Webmaster Tools. The user signs in; you prepare the steps.
5. **Analytics funnel, if analytics applies** (stage 2's table). `marketing-skills:analytics` and `marketing-skills:conversion-tracking`. With the chosen tool (PostHog: `posthog:building-a-dashboard`), build a funnel from visit to sign-up to activation to paid. If analytics is N/A, define the manual proxy you'll track instead (for example, enquiries or orders per week).
6. **Lifecycle emails.** `marketing-skills:emails`: welcome, activation nudge, trial ending and win-back.
7. **Launch plan.** `marketing-skills:launch`: channels (Product Hunt, Hacker News, communities, social, newsletters), the assets for each, and a day-by-day plan. `ecc:content-engine` for the launch content.
8. **Go live with payments, CEO gate.** Checklist for switching the payment provider chosen in stage 2 (`references/payments.md`) to live mode: business details, tax settings, live keys in the production secret store, live webhook endpoint, and a real end-to-end payment with refund. **The user does this.** You prepare the checklist and verify afterwards.

Publishing, posting, emailing customers, directory and app-store submissions, DNS changes and going live with payments are **level C** (`references/authorization.md`). The agent drafts everything and gives copy-ready steps; the user does it; then the agent verifies the result. An approval of the content doesn't let the agent send or publish it.

## Output

`docs/company/08-gtm.md`: positioning, pricing, the funnel definition, the launch plan and the live-payments checklist.

## Gate: launch go

- [ ] The landing page, pricing and sign-up flow are live and tracked
- [ ] The funnel shows real events (if analytics applies), or the manual proxy is defined (if N/A)
- [ ] Live payments are verified with a real charge and refund (Startup track)
- [ ] The user approves the launch plan
