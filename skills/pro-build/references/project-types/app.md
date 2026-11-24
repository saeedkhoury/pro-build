# Project type: App (mobile and desktop)

Use it for iOS and Android apps, cross-platform mobile apps, tablet apps and desktop apps. Combine it with any track. Most apps also need a backend; use `system.md` for it.

**Three release branches. Pick the one that matches the shape below:**
- **Mobile** (iOS, Android): stage 7 → **Mobile apps** (store builds, user-run submission, phased rollout).
- **Desktop** (Windows, macOS, Linux): stage 7 → **Desktop apps** (signed installers, notarization, signed auto-updates, user-run publication).
- **PWA**: it's a web project. Use `web.md` and stage 7's normal web release path.

## Pick the shape first

| Shape | Signs | Default stack | Alternatives, and when to use them |
|:--|:--|:--|:--|
| **Cross-platform mobile** (most apps) | iOS and Android, standard UI, a small team | **Expo (React Native)** + TypeScript (`ecc:react-native-patterns`; the official `expo` plugin: `/plugin install expo@claude-plugins-official`), EAS Build and Submit, Expo Router; backend on Supabase or a `system.md` API | **Flutter** (`ecc:dart-flutter-patterns`) for heavily custom UI or a team that knows Dart |
| **Native iOS** | Apple-only, deep OS features (widgets, HealthKit, ARKit, on-device AI), top polish | **SwiftUI** (`ecc:swiftui-patterns`, `ecc:liquid-glass-design`, `ecc:foundation-models-on-device`); the official `xcode` plugin; test in the iOS Simulator | UIKit for legacy codebases |
| **Native Android** | Android-only or Android-first, deep OS features | **Kotlin + Jetpack Compose** (`ecc:kotlin-patterns`, `ecc:android-clean-architecture`) | Compose Multiplatform (`ecc:compose-multiplatform-patterns`) to share UI with iOS |
| **Desktop** | Windows, macOS or Linux tools | **Tauri** (small, secure) with a web frontend | Electron, when Node APIs or a mature plugin ecosystem are needed; native SwiftUI for Mac-only apps |
| **PWA instead of an app** | Simple, content-led, no store presence needed | Use `web.md` with installable PWA features | — |

**Decision rules:**
- **Cross-platform first.** Go native only when a must-have feature needs it.
- **Ask early whether the stores are required.** A PWA avoids review delays and the 15–30% store fee on digital goods.
- **Design for older app versions from day one** (API versioning, minimum supported version).

## Tools by stage

| Stage | Use |
|:--|:--|
| 2 Architecture | The stack above, the backend from `system.md`, offline and sync strategy, push notifications (APNs or FCM via Expo Notifications), deep links, payments by the store rules (StoreKit or Play Billing, or RevenueCat, **only for digital goods**; physical goods and real-world services use the provider from `references/payments.md`), a design that meets `references/app-stores.md` §3, and an analytics and crash SDK |
| 3 Design | Platform conventions (Apple HIG, Material 3), `ecc:design-system`, `ecc:accessibility` (Dynamic Type, screen readers, 44pt targets), dark mode, small and large screens |
| 4 Platform | **Mobile:** EAS or fastlane; signing in the build service's secret store; sandbox and production build profiles; TestFlight and Play internal and closed tracks (start the Google 12-tester, 14-day closed test early for new personal accounts); crash reporting. **Desktop:** a CI build matrix per OS (Tauri's bundler or electron-builder); code-signing certificates in the CI secret store; a signed update channel (for example, the Tauri updater with its own signing key) |
| 5 Engineering | `ecc:orch-add-feature`; Expo development builds; Detox or Maestro end-to-end tests; the iOS Simulator and Android emulator |
| 6 QA | **Mobile:** real-device smoke tests (an older and a newer phone), offline and poor-network tests, permission prompts, the store checklist in `references/app-stores.md` §5, privacy manifest and data-safety answers. **Desktop:** install, launch, update and uninstall on each target OS from the exact signed installers; check that the OS trusts the signature (no SmartScreen or Gatekeeper block) |
| 7 Release | **Mobile:** stage 7's mobile path. **Desktop:** stage 7's desktop path. **PWA:** the web path |

## Quality bar (stage 6 checks against it)

- **Start-up:** cold start under 2s on a mid-range device; 60fps scrolling; app size justified.
- **Stability:** crash-free sessions of 99.5% or more in beta before release.
- **Offline:** clear offline states; no data loss when the connection drops mid-action.
- **Accessibility:** screen reader labels, Dynamic Type or font scaling, contrast, 44pt (iOS) or 48dp (Android) targets.
- **Store compliance:** everything in `references/app-stores.md` §5: current SDK and target API floors, permission prompts that explain why, account deletion in the app if accounts exist, privacy labels and data safety that match real data use, purchases that follow store rules, and a demo account for review.
- **Compatibility:** the minimum OS versions are stated; the backend supports the oldest app version still in use.

## Kickoff questions for apps (on top of the universal ones)

1. iOS, Android, or both? Phones, tablets, desktop? The minimum OS versions?
2. Must it be in the App Store or Google Play, or is a web app (PWA) enough?
3. Which device features does it need: camera, location, notifications, Bluetooth, health data, contacts, background tasks?
4. Must it work offline? What happens to changes made offline?
5. Accounts: sign-in method (Apple, Google, email, phone)? Is account deletion handled?
6. How does it make money: paid app, subscriptions, in-app purchases, ads, or none? Is it digital (must use store billing; stores take 15–30%) or physical goods and real-world services (must not)? Where is the business registered (`references/payments.md`)?
7. Push notifications: what triggers them, and how often?
8. Is there an existing backend, website or brand to match?
9. The core screens: list them, even roughly.
10. Who has the Apple Developer and Google Play accounts: personal or organization (organizations need a D-U-N-S number), and in which country? (Creating them is your action; see `references/app-stores.md` §1.)
11. Expected users at launch? Any regions or languages?
12. Sensitive data (health, kids, finance), which triggers extra store review?
