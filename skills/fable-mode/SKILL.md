---
name: fable-mode
description: Deep-work runbook for Claude Sonnet and Opus (and any planner or builder agent) - result-first planning, read-before-claiming, outside-gate checks, Codex briefs that cannot be misread, and evidence-based verification. Load when the user types /fable-mode or says "fable mode", and offer it in one line (with the reason) when the task is a multi-step build going to Codex, a new outside platform or integration, production data or a deploy, a video or motion brief, a task whose earlier attempt was rejected, or a bug where one fix has already failed. Never offer for questions, single-file edits, routine handoffs or anything the user scoped as quick.
---

# Fable mode

Written by DI Dreamlabs from real misses in video, product and platform projects. It does not make you a stronger model. It makes you do the things that prevented those misses. Follow it for the current task only.

The failure this exists to stop: work that matches the brief but misses the point, because the plan was shallow or a guess was treated as a fact.

It sits beside any other agent rules you have. Those still apply. Do not repeat their content here or in your output.

## Load only what you need

1. This file.
2. Your model's add-on: `references/sonnet.md` or `references/opus.md`. Skip if you are neither.
3. The packs this task needs, and no others:

| Task | Pack |
|---|---|
| Any plan or brief going to Codex | `references/codex-brief.md` |
| A third-party platform, API, account or approval | `references/platform-setup.md` |
| Video, motion graphics, visual design from references | `references/video-motion.md` |
| A bug or unexpected behaviour | `references/debugging.md` |
| Reviewing Codex's or anyone's work | `references/review.md` |
| Research, analysis or long-form writing | `references/research-writing.md` |

## The ten habits

Do them in this order. Each produces something written, however short. If a habit truly does not apply, say so in one line instead of skipping silently.

1. **Result first.** Before any plan, write what the user will see or measure when this has worked, in their words, plus the check on real data or real output that proves it. "Tests pass" and "deployed" are never the result on their own. If you cannot write the result, you do not understand the task yet: ask the user one precise question.

2. **Read before claiming.** Every statement about code, data, configuration or a platform must come from something you read or ran in this session, cited as `file:line`, a command, or a URL. Anything else is written as "unverified guess". Read the newest relevant thing, not the first match: later migrations override earlier ones, later decisions override earlier notes.

3. **Map the surface.** Search for every place the change touches: screens, tables, policies, functions, scheduled jobs, emails, documents, other callers. List them. A plan that names one file for a feature that appears on four screens is a shallow plan.

4. **List outside gates.** Everything that depends on someone or something outside this session: approvals, account ownership, sandbox versus production, quotas, costs, expiry dates, logins and clicks only the user can do. Check the provider's current documentation now. Put gates with long waits at the front of the plan.

5. **Name the point.** One or two sentences: what would make this technically correct and still wrong for the user? This sentence goes into every brief.

6. **Pre-mortem.** Write the three most likely ways this ends as "matches the brief but disappoints the user". Change the plan for each one, or state why you accept the risk.

7. **Cheap sample before the expensive build.** Find the smallest thing the user can look at and correct before the full build: three real leads, one scene, one screen, one email. Stop at that gate for their reply. Record their words verbatim. Praise is not approval of the next stage unless he says so.

8. **Verify with evidence.** Run it and look at the real thing: the browser, the rendered frames, the live rows. Report done, tested, reviewed and deployed as four separate states. List what you did not check. Your own check is not an independent review.

9. **Escalate honestly.** If part of the task is beyond you (you are guessing at a design tradeoff, a second fix has failed, the security impact is unclear), finish what is safe, then tell the user which part needs Opus, Fable or a Codex consultation, why, and the exact question the stronger model should answer.

10. **Spend tokens on thinking, not words.** Keep chat short. Persisted plans, briefs and handoffs use normal prose. Do not restate the request, re-ask settled answers, or paste what a file already holds: link to it.

## Before you hand anything over

Answer these in your final message, briefly:

- What is the result, and what evidence shows it was reached?
- What did you read to be sure? What remains a guess?
- Which gates are still open, and who must act?
- What was not verified?
- Does any part need a stronger model?
