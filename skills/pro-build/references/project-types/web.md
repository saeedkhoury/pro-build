# Project type: Web (websites and web apps)

Use it for marketing and client sites, landing pages, e-commerce, SaaS dashboards, portals, internal web tools and PWAs. Combine it with any track. Stage 2 records the choices below in `02-architecture.md`.

## Pick the shape first

| Shape | Signs | Default stack | Alternatives, and when to use them |
|:--|:--|:--|:--|
| **Content site** (brochure, blog, landing, client site) | Mostly static pages, a form, SEO matters, little login | **Astro** + TypeScript, Tailwind, deployed to Cloudflare Pages or Vercel; content in Markdown or a headless CMS | Next.js, if it will grow into an app; WordPress or Webflow, if the client must edit everything themselves (say so, because pro-build's code workflow then applies only partly) |
| **Web app / SaaS** | Accounts, data, dashboards, payments | **Next.js** (App Router) + TypeScript, Tailwind + shadcn/ui (`vercel:shadcn`), Supabase (Postgres, auth, storage, RLS), Stripe, Vercel (`vercel:nextjs`) | Nuxt (Vue teams: `ecc:nuxt4-patterns`); Remix or React Router; Neon + Prisma (`ecc:prisma-patterns`) instead of Supabase; Cloudflare Workers (`cloudflare:frameworks-on-cloudflare`) for edge or low cost |
| **E-commerce** | Catalogue, cart, checkout, inventory | **Shopify** (hosted) for standard stores; **Next.js + Stripe** for custom flows | Medusa (open source); don't build your own cart unless the flow is truly unusual |
| **Internal tool** | Staff only, data-heavy, few users | Next.js + Supabase with role-based access, or a Vite SPA (`ecc:vite-patterns`) over an existing API | Retool or Appsmith, if speed matters more than custom UX |

**Decision rules:** choose the least complex shape that meets the must-haves; prefer managed services over self-hosting; one language (TypeScript) end to end, unless the team already knows another stack.

## Tools by stage

| Stage | Use |
|:--|:--|
| 2 Architecture | `ecc:frontend-patterns`, `ecc:react-patterns` or `ecc:vue-patterns`, `ecc:api-design`; rendering strategy (static, server or client) per page; configuration strategy (`NEXT_PUBLIC_*` is build-time) |
| 3 Design | `taste-skill:design-taste-frontend`, `ecc:frontend-design-direction`, `ecc:design-system`, `ecc:accessibility`; mobile-first layouts at 360, 768 and 1280px |
| 4 Platform | `vercel:bootstrap` or `cloudflare:frameworks-on-cloudflare`, `supabase:supabase`; SEO foundations (stage 4 step 8) |
| 5 Engineering | `ecc:orch-add-feature`; `vercel:react-best-practices` or `ecc:react-performance`; Playwright for end-to-end tests (`ecc:e2e-testing`) |
| 6 QA | `ecc:browser-qa`, `ecc:accessibility`, `ecc:production-audit` (Core Web Vitals), `claude-seo:seo-audit` or `ecc:seo` |

## Quality bar (stage 6 checks against it)

- **Performance:** LCP under 2.5s, INP under 200ms and CLS under 0.1 on mid-range mobile over 4G; JavaScript per page under about 200 KB (compressed) unless justified.
- **Accessibility:** WCAG 2.2 AA; full keyboard navigation; visible focus; reduced motion respected.
- **SEO** (public pages): unique titles and descriptions, sitemap, structured data, no orphan pages, server-rendered content for pages that must rank.
- **Security:** OWASP Top 10 basics, CSP headers, auth on every server route, RLS on every table, rate limits on forms and auth.
- **Internationalisation**, if needed: translations outside the code, right-to-left layouts tested, and locale-aware dates and currency.

## Kickoff questions for web (on top of the universal ones)

1. Is it mainly **content** (people read and contact you) or an **application** (people log in and do things)?
2. Who updates the content after launch, and how technical are they? Do they need a CMS?
3. Which pages or screens exist? List them, even roughly.
4. Do users need accounts? Roles (admin, staff, customer)? Login with Google or Apple?
5. Does it take money? One-off payments, subscriptions, marketplace payouts?
6. Which devices matter most: phones, desktops, or both? Any need to work offline (a PWA)?
7. Languages and regions? Any right-to-left languages?
8. How important is Google search traffic? Target keywords or locations?
9. Existing brand, domain, hosting, content or a site to migrate (and URLs to preserve)?
10. Integrations: email, maps, booking, CRM, analytics, chat, AI features?
11. Expected traffic at launch and in a year?
12. Legal: cookies and consent, privacy policy, accessibility law in the target country?
