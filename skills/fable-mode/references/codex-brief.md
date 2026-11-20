# Pack: briefs for Codex

Codex has none of this conversation. It builds what the brief says, to the letter. Every gap becomes a guess, and guesses are where "matches but misses the point" comes from.

Start the brief with the exact heading `# Build brief: <task>`. The heading marks the file as a build brief for any hook or reader that looks for it.

## Template

```
# Build brief: <task>

Project / worktree / branch / base commit:
Role and limits: (what Codex may and may not do: push, deploy, migrations, spending)

## Purpose
Why the user wants this, in two or three sentences.

## The point
What would make this technically correct and still wrong.

## Result and acceptance
Numbered. Each item is something observable, with how to check it
(command, query, screen and what must be visible, frame number).

## Current state (read, not assumed)
Facts with file:line or command for each. Mark anything unverified.

## Surface
Every file, table, policy, job and screen affected. Callers to recheck.

## Do not change
Files, behaviours and data that must stay as they are.

## Steps
Ordered, each with its own check. Mark gates where Codex must stop for the user.

## Stop and ask if
Conditions under which Codex stops instead of guessing.

## Report back
Use the report format in `templates/BUILD-BRIEF.md` (files written, verified with evidence, not verified, deviations, risks, open questions, next step).
```

## Check before sending

- Could a capable builder who has never seen this project finish without asking a question? Reread it as that person.
- Is every acceptance item checkable by Codex itself, without the user?
- Does each "current state" fact have a citation from this session?
- Are outside gates resolved, or explicitly marked as the user's step?
- Is there a cheap sample gate before the full build?
- Is the brief the smallest task that delivers the result? Split it if it holds two independent results.

## When Codex reports back

Do not accept "done". Check each acceptance item against its evidence, open the real output yourself, and record independent review as pending if you could not. A review covers one exact commit; recheck after changes.
