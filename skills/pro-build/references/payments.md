# Payments: choose the provider by country and by what you sell

**Never assume Stripe.** Stripe only opens accounts for businesses registered in the countries it supports, and that list changes. The right provider depends on **where the business (the legal seller) is registered**, **where the customers are**, and **what is sold**. Kickoff asks; stage 2 decides and records the choice in the service applicability table (operating rule 14); every later stage uses the recorded provider.

## 1. Kickoff: ask these when there is a business model

Critical when money moves through the product (see `references/kickoff.md`):

1. **Business country:** where is the seller registered (a company, a sole trader, or "not yet")? This decides which providers can open an account.
2. **Customers and currency:** where are the customers, and in which currency do they pay?
3. **What is sold:** digital (subscriptions, features, content) or physical goods and real-world services (bookings, deliveries, classes)? One-off payments or subscriptions?
4. **Local needs:** local cards and wallets, instalments, tax invoices or receipts that local law requires.

## 2. Stage 2: decide, in this order

| # | Situation | Use |
|:--|:--|:--|
| 1 | **A mobile app that sells digital content or features** used inside the app (subscriptions, premium features, coins) | **Apple In-App Purchase and Google Play Billing are required** by store rules, wherever the business is. RevenueCat (or StoreKit and Play Billing directly) manages them. Store fees apply. See `references/app-stores.md` |
| 2 | **Physical goods or real-world services** (a barber booking, a delivery, a class), in an app or on the web | A normal payment provider (rows 3–6). Store in-app purchase must **not** be used for these |
| 3 | The seller's country is **on Stripe's supported list** (check Stripe's official page during stage 2) | **Stripe** (`stripe:stripe-best-practices`, `stripe:stripe-docs`) |
| 4 | **Not on Stripe's list**, selling **digital products or SaaS** internationally | A **merchant of record** that accepts sellers from that country, such as **Paddle** or **Polar**. They sell on your behalf and handle sales tax and VAT worldwide, for a higher fee. Digital products only. Confirm seller eligibility and payouts for the country during onboarding |
| 5 | **Not on Stripe's list**, selling **mostly to local customers**, or selling physical goods or services | A **local payment service provider** licensed in that country (local cards, local wallets, instalments, local currency, local invoices). Check that it has an API, hosted checkout or SDK, sandbox mode, webhooks and, if needed, recurring billing |
| 6 | Any country, as an extra option | **PayPal** (or Braintree), if it supports both the seller's and the customers' countries |
| 7 | The founder wants Stripe anyway | Register a company in a supported country (for example a US company through Stripe Atlas). That's a **legal and tax decision for the user and their accountant (level C)**, never a default |

Record in `02-architecture.md`: the chosen provider, why, the alternative, the fees, the payout currency, and the official page that confirmed country support (with the date checked). Rule 14 then makes every later stage use it.

## 3. Israel (example of a country Stripe doesn't support)

Stripe doesn't open accounts for businesses registered in Israel. Choose by what you sell:

| You sell | Recommended | Notes |
|:--|:--|:--|
| SaaS or digital products to international customers | **Paddle** or **Polar** (merchant of record) | They handle VAT and sales tax for buyers abroad. Confirm Israeli seller payouts when you sign up |
| To Israeli customers (bookings, shops, services, local subscriptions) | A **local Israeli provider**, such as **Tranzila**, **CardCom**, **PayPlus** or **Grow** (formerly Meshulam) | Supports Israeli cards, **Bit**, instalments (תשלומים) and ILS. Usually requires an Israeli merchant (acquiring) agreement. Many integrate with invoicing services that issue the tax invoices and receipts Israeli law requires |
| In-app digital purchases in a mobile app | **Apple IAP and Google Play Billing** (with RevenueCat) | Required by the stores. Apple and Google pay out to Israeli bank accounts |
| A simple start or international buyers | **PayPal** | Works for Israeli sellers; higher fees, weaker subscription tooling |

Compare current fees, monthly costs, recurring-billing support, API quality and payout times on each provider's own site before choosing. Tax registration, VAT and invoicing rules are for the user's accountant: pro-build records the decision but doesn't give tax advice.

## 4. The same safety rules for every provider

- **Sandbox or test mode first** (operating rule 4). Keys live in the secret store, never in git.
- **Webhooks are verified** (signature or shared secret, per the provider's docs) and processed idempotently (`references/project-types/system.md`).
- **Never store card numbers.** Use the provider's hosted checkout, payment page or tokenised fields, so card data never touches your servers.
- **Going live is level C** (`references/authorization.md`): the user creates the live account, completes verification, enters live keys and runs the first real payment and refund. pro-build prepares the checklist and verifies afterwards (stage 8).
- **Revenue metrics** in stage 9 come from the chosen provider's dashboard or API, whichever provider that is.

## 5. If the provider has no Claude Code plugin

Use its official API documentation and SDK. Say so in one line, and mark any step that needs a signed-in account as "blocked: connect <provider>" until the user connects it.
