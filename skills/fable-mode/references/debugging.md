# Pack: debugging

Use with superpowers:systematic-debugging; this adds only the habits that were missing.

- **Reproduce first.** Get the failure to happen on demand and write down the exact steps and output. No fix before a reproduction, unless reproduction is impossible, in which case say so.
- **Evidence over theory.** Read the actual error, logs and data rows. Quote them. Do not reason from what the code "should" do.
- **One cause, stated.** Name the root cause in a sentence and the evidence that distinguishes it from the next most likely cause. If you cannot distinguish them, you have not found it.
- **Check the newest truth.** Later migrations, later deploys and live configuration override what the repository's older files say. Confirm what is actually running.
- **Do the arithmetic across limits.** When the symptom involves timing, budgets, quotas or rate limits, list every constant on the path (timeouts, totals, spacing, caps, concurrency) with its file and line, then work out together how many operations can actually fit. Each constant can look reasonable alone while the combination allows almost nothing. In the 2026-11-15 proof run both models found the gate and spacing faults but under-weighted a 36 s total against a 33 s per-check window, which on its own stopped any second check.
- **Fix the cause, then prove it.** Show the reproduction now passes, and check the nearby cases the fix could have broken.
- **After one failed fix, stop.** Do not try a variation. Re-read the evidence, list what the failed fix taught you, and consider escalating with the exact question.
- **Report** cause, evidence, fix, proof, and what else shares the same weakness.
