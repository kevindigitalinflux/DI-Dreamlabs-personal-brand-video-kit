---
name: pb-video-style
description: Use for planning, briefing, building or reviewing the look of any personal-brand video: reels, Shorts, TikToks and long educational videos. Covers the motion-graphics building blocks (room extension, layout slides, captions band, pay board, logo row, checklist, offer card, cover), brand tokens, the plan-first rule and the style checks. Trigger on "motion graphics", "make the Reel", "cover", "captions", "overlay", "style", "build/plan/review the video".
---

# Personal-brand video style

The look comes from `brand/brand.json`; the structure and rules below stay the same for every brand. Full component specs: `docs/REEL-9x16-BLOCKS.md`. Plan with `templates/PLAN.md`. Load `fable-mode` for any build.

## Rules that never bend

- No video starts without a written plan the owner approved. Plan first, then a brief, then a draft, then at most two finals.
- Every effect starts on its spoken word (logos up to 3 frames early, everything else within 3 frames), from a trigger file made from the transcript with word timings.
- Real design, not clip-art: no stick figures, outline doodles, emoji art, generic gradients, music or sound effects. Realistic UI mockups, real photos and footage, icons, diagrams and (with the owner's yes) AI-generated media are all fine.
- Exact brand colours and fonts. Logos on the background or text colour only, never on the accent colour. No logo without an approved file; otherwise text.
- Reels have no zooms or punch-ins and constant presenter scale.
- Cards and graphics never cover the mouth or sit where captions go.
- At most two full final renders per video. No uploads, publishing, logins or spending without an explicit yes.
- Never claim to have watched or listened to a video; say which frames you inspected.

## Building blocks (summary; specs in docs/REEL-9x16-BLOCKS.md)

| Block | Use it when |
|---|---|
| Presenter fill-frame crop | A portrait phone picture sits inside a landscape canvas |
| Room extension | The presenter moves down and the top needs filling: blur and flip the presenter's own wall instead of a flat colour |
| Layout slides (FULL and ROOM) | Graphics need room at the top; 16-frame moves; no more than five in 60 s |
| Low captions band | Short captions in a fixed band, centred, never over the mouth |
| Hook giant | The first spoken line as large rows that slam on their words |
| Pay board | A counting list of job-ad or survey figures with a permanent honesty footer |
| Tool logo row | A list of tools said together, each tile popping on its word |
| Checklist with ticks | Three outcomes, each on its word |
| Offer card | Sale, code, places, deadline, call to action, URL held to the last frame |
| Cover (9:16 and 1:1) | One HTML page rendered to PNG by headless Chrome, same look as the video |

## Plan, then gates

1. Words and cuts as a list the owner can mark.
2. Audio decisions as short A/B clips.
3. Style frames or stills for each new visual idea (side by side with the reference frame).
4. One scene built fully before the rest.
5. Draft at 540x960, then the final at 1080x1920.

At each gate, stop and record the owner's reply word for word. "Looks pretty good" with notes is a change list, not approval to render.

## Review checklist

Compare against the plan scene by scene; run Hyperframes `lint` and `check` with zero errors; look at stills of every scene; list what was not verified. Findings first, with file paths and frames.
