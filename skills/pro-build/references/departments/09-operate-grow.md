# Stage 9: Operate & Grow

**Model routing:** decisions in the main thread · `haiku` to pull and tabulate metrics, errors and revenue · `opus` for the analysis and the next-focus recommendation.

**Role:** COO and analyst. Run the company on numbers, and decide what to build next. Repeat weekly, through `/pro-build review`.

## Weekly operating review

1. **Metrics.** From the analytics tool chosen in stage 2 (PostHog by default), or the manual proxy if analytics is N/A: the North Star and input metrics against last week, funnel conversion, retention, and feature-flag or experiment results (`posthog:diagnosing-experiment-results`).
2. **Revenue.** From Stripe: new MRR, churned MRR, failed payments and refunds. Use `ecc:customer-billing-ops` for billing issues and `marketing-skills:churn-prevention` for churn.
3. **Reliability.** From the error monitoring chosen in stage 2 (Sentry by default), or from logs and user reports if it's N/A: new and regressed issues, the error rate, and affected users. Turn the top issues into backlog items (`sentry:sentry-debug-issue`).
3b. **Incidents and data safety.** Review any incidents since the last review: severity, time to recover, root cause, follow-ups, and whether the post-incident review was written. Check that the backups ran and that the last restore test is less than 90 days old; if it isn't, add a restore test to next week. Check any hotfix follow-up checks that are due (stage 7).
4. **Customer voice.** Support messages, feedback and reviews. Note the top requests and complaints.
5. **Retro.** What shipped, what slipped, what we learned. Capture reusable lessons with `ecc:learn-eval`.
6. **Decide.** Choose one focus for next week: fix, improve conversion, build a feature, or grow a channel. Propose experiments (`marketing-skills:ab-testing`) with a hypothesis and a success metric.
7. **Roadmap update.** Reorder the backlog in `BUILD-STATE.md`. New features go to stage 5; big changes go back to stage 1.

## Output

`docs/company/09-reviews/<yyyy-mm-dd>.md` with the metrics table, the decisions and next week's plan.

## Gate: next-cycle plan approved

- [ ] Metrics are reported with real numbers (or marked as missing, with the reason)
- [ ] One focus is chosen, with a measurable goal
- [ ] The backlog is updated
