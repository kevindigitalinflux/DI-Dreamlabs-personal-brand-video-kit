# Pack: reviewing work

- **Review against the result, not the diff.** Start from the brief's purpose, point and acceptance items. Code that is clean but does not reach the result fails review.
- **Pin the revision.** Name the exact commit or diff reviewed. Recheck if it changes.
- **Open the real thing.** Run it, load the screen, look at the frames, query the rows. Reading the diff alone is a partial review; say so.
- **Check every acceptance item** and mark each: met with evidence, not met, or could not verify.
- **Hunt for what is missing**, not only what is wrong: screens not updated, cases not handled, existing data not migrated, checks claimed but not shown.
- **Verify the builder's claims** rather than trusting the report. Spot-check at least the two that matter most.
- **Findings first**, most serious first, each with file and line, what happens, and why it matters to the user. Then what you did not review.
- You reviewing your own work is not an independent review. Record independent review as pending.
