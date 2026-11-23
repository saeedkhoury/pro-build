# PRD: ChairBook (approved 2026-11-06)
## Requirements
- R1 Shop page lists services and barbers. AC: public URL per shop; loads under 2s.
- R2 Barber calendar. AC: barber sets working hours; booked slots blocked.
- R3 Booking form. AC: customer picks service, barber and slot; booking saved; confirmation email within 1 min.
- R4 Deposits. AC: 20% deposit via Stripe Checkout; refundable up to 24h before.
- R5 Barber payouts via Stripe Connect Express. AC: onboarding link; deposit minus 5% platform fee transferred to the barber.
## Metrics
North Star: completed bookings per week (PostHog). Inputs: booking conversion, barber activation, deposit no-show rate.
