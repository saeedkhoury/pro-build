# Architecture: ChairBook (approved 2026-11-09)
- Stack: Next.js 16 (App Router) + TypeScript · Supabase (Postgres, auth, RLS) · Stripe (Checkout, Connect Express) · Vercel.
- Configuration strategy: build-time for NEXT_PUBLIC_* (two builds per release: sandbox + production-configured).
- Data: shops, barbers, services, bookings, payments (stripe ids only); RLS on every table.
## Service applicability
| Capability | Decision | Stage 4 evidence |
|---|---|---|
| Hosting/deploys | Vercel | staging deploy from main |
| Database/auth | Supabase | migration applied in staging |
| Payments | Stripe (test mode until stage 8) | test checkout |
| Error monitoring | Sentry | staging test event |
| Product analytics | PostHog | staging test event |
| Email | Resend | staging test email |
## Operations profile
RPO 24h · RTO 4h · incident owner: the CEO · alerts: email + phone · SEV1–3.
