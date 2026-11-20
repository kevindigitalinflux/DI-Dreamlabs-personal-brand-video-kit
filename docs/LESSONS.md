# Lessons learned (real mistakes, real fixes)

Add yours at the bottom as you go. Each lesson: what happened, the fix, how to avoid it.

1. **Two microphones summed (hollow voice).** OBS recorded the laptop mic and a USB mic at once. The sum had a 9.75 ms comb filter and sounded hollow. Post fixes reduce it, never remove it. Fix at the source: one microphone source active in OBS; test 10 seconds, peak below -6 dBFS. Repair: `tools/audio/comb_detect.py` then `comb_fix.py`.
2. **Mono loudness reads 3 LU low.** Measure -14 LUFS on dual-mono stereo, or the limiter works far too hard.
3. **The limiter's auto-level.** FFmpeg `alimiter` pushes peaks to 0 dBFS unless `level=0`.
4. **Processed audio lost the A/B test.** An EQ plus compression chain and per-clip level matching sounded worse to the owner than plain audio with one gain. Offer A/B files; do not decide for them.
5. **Zoom keyframes.** A zoom expression whose first threshold is the outermost condition matches every later frame, so the zoom never releases. The owner disliked reel zooms anyway. Reels use constant scale.
6. **Silent edit failures.** A script that patches HTML or CSS with `replace` can change nothing if the text did not match. Assert the replacement count is 1.
7. **ASR word end times stretch.** Cut at silence boundaries from `silencedetect`, not at word ends.
8. **ASR mishears numbers.** "Thirty" came out as "thirteen" every time. Ask the speaker.
9. **Look-downs at the phone.** Trim at silence; if that clips a syllable, hide the glance behind a card.
10. **A cover from a soft frame looks soft.** Ask for a good phone photo before building the cover.
11. **Logos.** Some companies require written permission for public logo use. Use text when you do not have it.
12. **Posting-day facts expire.** Job ads close, codes change, places run out. Keep a posting-day list separate from the build.
13. **Disk fills with temporary files.** After delivery, list review and QA frames, caches and superseded masters, ask, then delete. Keep finals, the approved project, plans and raw recordings. Reports will keep dead links to deleted frames.
14. **Cheap sample before the expensive build.** Showing a small artefact early (a style frame, an A/B pair, one scene) saved more renders than any check script.
