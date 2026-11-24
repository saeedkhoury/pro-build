# App Store and Google Play: publishing rules

Use this for every mobile app (`references/project-types/app.md`). Kickoff asks the account questions (§1), stage 2 designs for the rules (§3), stage 4 sets up the accounts and tracks, stage 6 runs the checklist (§5), and stage 7 submits (§4).

> **Rules change every year.** The dates below were checked in November 2026. At stage 2 and again before each submission, open the official pages in §6 and confirm the current numbers. If they differ, follow the official page and update `02-architecture.md`.

## 1. Developer accounts (level C: the user creates them)

| | Apple App Store | Google Play |
|:--|:--|:--|
| Program | Apple Developer Program | Google Play Console |
| Fee | Yearly membership | One-time registration fee |
| Individual or organization | Individual (your name shows as the seller) or organization (the company's name; needs a **D-U-N-S number**) | Personal or organization (organizations need a **D-U-N-S number**); identity verification for both |
| First release | TestFlight beta, then review | **Personal accounts created after 13 November 2023:** a **closed test with at least 12 testers opted in for 14 days in a row** before you can apply for production access. Recruit extra testers in case some drop out |
| Payouts | To the bank account in the agreements section, after tax forms | To a Google payments profile and bank account |

Kickoff asks: who owns the accounts, **personal or organization**, and the **country** (it affects tax forms, payouts and the seller name). Start the Google closed test early: it adds at least two weeks to the first Android launch.

## 2. Technical floors for uploads (checked November 2026)

| Store | Requirement |
|:--|:--|
| **Apple** | Since **28 April 2026**, uploads must be built with **Xcode 26 or later** and the **iOS 26 SDK** (or the matching iPadOS, tvOS, visionOS or watchOS 26 SDK). Older builds are rejected at upload. Every third-party SDK that Apple lists must ship a **privacy manifest**, and the app declares its required-reason APIs |
| **Google** | Since **31 August 2026**, new apps and updates must **target Android 16 (API level 36)**. Existing apps must target at least Android 15 (API 35) to stay visible to users on newer devices. New apps are uploaded as an **Android App Bundle (AAB)**. Native libraries must support **16 KB memory pages** |

Expo and Flutter projects: use the SDK version that meets these floors (`eas build` with the current Expo SDK, or the current Flutter stable).

## 3. Policies that decide the design (stage 2)

| Topic | Apple (App Review Guidelines) | Google Play (Developer Program Policies) |
|:--|:--|:--|
| **Payments** | **Digital goods and features used in the app must use In-App Purchase** (3.1.1). **Physical goods and real-world services** (bookings, deliveries, rides) must **not** use IAP; use a normal payment provider (3.1.3(e)). Some regions allow links to outside purchases: check the current rules per storefront | Same split: **Google Play Billing** for digital goods; physical goods and services use another provider. Alternative billing exists only in some regions |
| **Accounts** | If users can create an account, they must be able to **delete it from inside the app** (5.1.1(v)) | Account deletion **in the app and through a web link** listed in the Play Console |
| **Sign-in** | If you offer third-party sign-in (Google, Facebook), also offer a privacy-focused option such as **Sign in with Apple** (4.8) | No equivalent requirement |
| **Privacy** | **Privacy nutrition labels** in App Store Connect must match what the app and its SDKs really collect. Clear permission strings (why you need the camera or location). App Tracking Transparency before tracking | The **Data safety form** must match the app and its SDKs. Sensitive permissions (location in the background, SMS, call log, all photos, accessibility) need a declaration and a real core use |
| **Content** | Apps with user-generated content need reporting, blocking and moderation (1.2). Kids, health, finance and gambling categories have extra rules | Same for user-generated content. Apps for children follow the **Families policy**. Content rating through the IARC questionnaire |
| **Quality** | Complete and working, no placeholders (2.1); real value beyond a website wrapper (4.2); accurate screenshots and description (2.3) | No broken features or misleading listings; the app must work for the reviewer |

Stage 2 records how the app meets each row in `02-architecture.md`. A rule that changes the plan (for example "bookings must not use IAP") goes into the architecture before any code.

## 4. Submission (stage 7, level C)

The user submits; pro-build prepares everything:

- **Store listing:** name, subtitle, description, keywords (Apple) or short description (Google), category, support URL, **privacy policy URL**, screenshots for the required device sizes, app icon, and, if needed, a preview video.
- **Review notes:** a **working demo account** (or sign-in instructions), how to reach every feature, and anything the reviewer can't test (hardware, region, paid content). Missing demo accounts are a top rejection reason.
- **Age rating** (Apple questionnaire; Google IARC), **export compliance** (encryption), **content rights**, and any **sensitive-permission declarations**.
- **Pricing and availability:** the countries, the price tier, and in-app products created and **approved together with the build** that uses them.
- **Review time:** plan for 1–3 days for Apple and up to a week for Google, longer for new accounts or sensitive categories. Use phased release (Apple) and staged rollout (Google) as in stage 7.
- **Rejections:** read the exact guideline cited, fix the cause, reply in the review center if it's a misunderstanding, and resubmit. Record each rejection and its fix in `BUILD-STATE.md`.

## 5. Pre-submission checklist (stage 6, check 11 for apps)

- [ ] Current SDK and target API floors met (§2), confirmed against the official pages today
- [ ] Payments follow §3 (IAP or Play Billing only for digital goods); in-app products created and in review with the build
- [ ] Account deletion in the app (and, for Google, a web link)
- [ ] Sign in with Apple or an equivalent option, if third-party sign-in exists
- [ ] Privacy labels and the Data safety form match the real data use of the app **and** its SDKs; privacy manifests present
- [ ] Every permission prompt explains why; no unused permissions in the manifest or Info.plist
- [ ] Privacy policy URL works; terms of use if there are subscriptions
- [ ] Demo account and review notes ready; every feature reachable by the reviewer
- [ ] User-generated content: report, block and moderation in place
- [ ] Screenshots and description match the build; no "beta" or placeholder content
- [ ] Google personal account: the 12-tester, 14-day closed test is complete
- [ ] Age rating, export compliance and content rights answered

## 6. Official sources (open them before each submission)

- Apple App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- Apple upcoming requirements: https://developer.apple.com/news/upcoming-requirements/
- Google Play Developer Program Policies: https://play.google/developer-content-policy/
- Google Play target API level: https://support.google.com/googleplay/android-developer/answer/11926878
- Google Play testing requirements for new personal accounts: https://support.google.com/googleplay/android-developer/answer/14151465
