# Cross-review: Claude and Codex check each other (claudex-loop)

Two AI providers catch more than one. pro-build uses [claudex-loop](https://github.com/chaseai-yt/claudex-loop) at two points:

1. **Readiness review** at the end of stage 2: Codex reviews the complete plan package, and you get a clear answer: **ready to build, or not**.
2. **Dual code review** in stage 5: every pull request that changes code is reviewed by **Claude** and inspected by **Codex** before you're asked to merge.

**Roles follow the host.** In Claude Code, Claude plans and builds; Codex reviews and inspects. In Codex, the roles swap: Codex plans and builds; Claude reviews and inspects. A provider never counts as independent reviewer of its own work.

**Requirements:** the `claudex-loop` plugin and a signed-in Codex CLI (or Claude CLI, when the host is Codex); see `references/toolkit.md`. Reviews are read-only: the reviewer can read the repository but not change it. Run diagnostics stay outside the repository.

## 1. Readiness review (stage 2, after the consistency check)

**What is reviewed:** the whole package, through `docs/company/02-plan.md` as the plan file. Before the review, make sure `02-plan.md` links the brief, `01-prd.md`, `01-roadmap.md`, `02-architecture.md` and the ADRs, so the reviewer reads them all.

**How:** run `claudex-loop:claudex-loop` with `mode=review`, `plan=docs/company/02-plan.md`, `log=docs/company/02-review-log.md` and `rounds=3` (2 in compact mode). Ask the reviewer to check:

- every PRD requirement and acceptance criterion is covered by a plan task, and M1 matches the roadmap's "Now";
- the architecture can deliver every requirement (data, APIs, integrations, non-functional requirements);
- acceptance criteria are testable, and each task is small enough for one pull request;
- risks, security, privacy, payments (`references/payments.md`) and, for apps, store rules (`references/app-stores.md`) are handled;
- nothing is missing that would stop M1 from shipping.

**Each round:** you (the coordinating agent) decide each finding: accept and fix the documents, or reject with a reason. Log every disposition. When a fix changes behaviour, update every document that states the old behaviour. Re-review the changed package in the same reviewer session.

**The answer to the user.** The stage 2 CEO briefing starts with one of these:

| Verdict | When | What it means |
|:--|:--|:--|
| ✅ **READY TO BUILD** | The reviewer returned **APPROVED** on the final plan | Stage 5 can start after your approval at the gate. Low-priority advice and the reviewer's stated limitations are listed |
| ⏳ **NOT READY** | Findings are still open after the round limit, or the plan changed after approval | The open findings, our position on each, and the options: fix them, revise the scope, or override |
| ⚠️ **UNREVIEWED** (your override) | You chose to build without an approved review | Recorded in `BUILD-STATE.md` → Approvals as an override. It's never called "approved" |
| 🚫 **REVIEW BLOCKED** | Codex isn't installed or signed in, it's out of quota, or the result was malformed | Not an approval. Say what's missing. Offer to fix it, wait, run `ecc:council` as a **same-provider** review (labelled as such), or override |

A completed run is not an approval: only an **APPROVED** verdict on the final plan counts. Zero findings is valid, but it isn't proof that the plan is perfect: say so.

**Bind the approval.** Record in `BUILD-STATE.md` → Approvals: the verdict, the date, the review result path, and the SHA-256 of `01-prd.md`, `01-roadmap.md`, `02-architecture.md` and `02-plan.md` at approval time.

**Before stage 5 starts, and before each new milestone:** recompute those hashes. If any changed, run claudex-loop's approval `check` or a new review round on the changed package. A stale approval is **NOT READY**, never ready.

The AI's verdict is advice. Approving the stage 2 gate is still your decision.

## 2. Dual code review (stage 5, every pull request)

**Policy** (in `BUILD-STATE.md` → `Dual review:`): `every PR` by default. The user can set `risky only` (auth, payments, data migrations, security, infrastructure). Docs-only pull requests get Claude's review only.

For each pull request, after CI passes:

1. **Claude review:** `ecc:code-review` in a fresh context (a separate reviewer agent). It's the same provider that wrote the code, so it's a self-check, not an independent review.
2. **Codex inspection:** claudex-loop's `inspect` on the branch, against the commit the branch started from (`--base`) and the plan or feature spec (`--plan`). It runs in a **fresh** Codex session and sees the whole diff, including new files. When Codex built the code (`claudex-loop:codex-build`), Claude inspects instead.
3. **One findings table** in the pull request: source (Claude or Codex), severity, file, finding, and decision (fixed, or rejected with a reason).
4. **Fix and re-inspect:** fix the accepted findings, rerun the tests, then run a **fresh** inspection of the new snapshot. Use at most 2 inspection rounds; report what's still open instead of looping. An inspection covers only the snapshot it saw: any later commit needs a new one before merging.
5. **The merge question** shows both results, for example: "Claude review ✅ · Codex inspection ✅ (snapshot `abc1234`) · 2 findings fixed, 1 rejected (reason). Merge PR #12?" Merging is still level B: your explicit yes for that pull request.

**If Codex isn't available:** say so before asking to merge, and label the pull request **single review**. For an ordinary change, you may merge on an explicit yes that acknowledges the single review. For a **risky** change (auth, payments, data migrations, security), wait for the Codex inspection, or for your explicit, logged override.

## 3. Costs

Each Codex review or inspection uses the reviewer's own quota or credits, not Claude's. The readiness review runs once per plan (plus re-checks after changes). Dual review runs once or twice per pull request. If the cost is too high, set `Dual review: risky only`.
