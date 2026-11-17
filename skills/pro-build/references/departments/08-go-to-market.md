# Stage 8: Go-to-Market

**Role:** Head of Growth. Turn a working product into one that people find, trust and pay for.

## Steps

1. **Positioning and messaging.** `marketing-skills:product-marketing` and `ecc:brand-voice`: who it's for, the main promise, proof points and objections.
2. **Landing page and conversion.** `marketing-skills:copywriting` and `marketing-skills:cro`: headline, social proof, a clear call to action. Then `marketing-skills:signup` and `marketing-skills:onboarding` so new users reach value fast.
3. **Pricing page and paywall.** `marketing-skills:pricing` and `marketing-skills:paywalls`, connected to Stripe prices.
4. **SEO foundations.** `ecc:seo` or `marketing-skills:seo-audit`, plus `marketing-skills:schema` and `marketing-skills:site-architecture`: titles, meta tags, sitemap, structured data and page speed.
5. **Analytics funnel.** `marketing-skills:analytics` and `marketing-skills:conversion-tracking`. In PostHog, build a funnel from visit to sign-up to activation to paid (`posthog:building-a-dashboard`).
6. **Lifecycle emails.** `marketing-skills:emails`: welcome, activation nudge, trial ending and win-back.
7. **Launch plan.** `marketing-skills:launch`: channels (Product Hunt, Hacker News, communities, social, newsletters), the assets for each, and a day-by-day plan. `ecc:content-engine` for the launch content.
8. **Go live with payments, CEO gate.** Checklist for switching Stripe to live mode: business details, tax settings, live keys in the production secret store, live webhook endpoint, and a real end-to-end payment with refund. **The user does this.** You prepare the checklist and verify afterwards.

Publishing, posting and emailing are always done or approved by the user.

## Output

`docs/company/08-gtm.md`: positioning, pricing, the funnel definition, the launch plan and the live-payments checklist.

## Gate: launch go

- [ ] The landing page, pricing and sign-up flow are live and tracked
- [ ] The funnel dashboard shows real events
- [ ] Live payments are verified with a real charge and refund (Startup track)
- [ ] The user approves the launch plan
