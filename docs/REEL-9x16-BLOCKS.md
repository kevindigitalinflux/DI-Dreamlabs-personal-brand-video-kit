# Reel (9:16) motion-graphics blocks and lessons

These blocks came from a real 60-second sales reel for an online course, built from one phone recording of one presenter and approved by its owner. They work for any talking-head reel or Short. All geometry is for 1080x1920 at 30 fps. Colours and fonts come from `brand/brand.json`: this document says "background", "text" and "accent" colour; swap in your own.

The reel contained: a hook, a short "who I am" beat, a skill definition, a salary board, a tool list, an outcomes checklist, an honesty line, and an offer with a sale code and a call to action. If your video has different content, keep the structure and change the words.

## What the owner approved and rejected

Approved: the room extension instead of a flat colour at the top, five layout slides, the salary board, the offer card, low captions, plain audio with the comb-filter correction, a cover in the same look as the video.

Rejected: any zoom or punch-in ("not a fan of those zoom ins"), an EQ and compression audio chain, per-clip level matching, a flat colour block at the top of the frame, a blurred circle behind the presenter on the cover, stick figures.

## Blocks

**1. Presenter fill-frame crop.** A portrait phone picture can sit inside a 1920x1080 OBS canvas (for example 760x1080 centred). Crop to 9:16 (608x1080) and scale 1.776x to 1080x1920, with a light unsharp mask and fine temporal grain of 2 to 3 percent. The picture stays softer than a native portrait take. If your phone can record 9:16 natively, do that and skip the crop. Presenter scale is CONSTANT inside every layout: no punch-in, no push-in, no zoom keyframe. Check on encoded frames that face-box width is constant within 1 percent per segment.

**2. Room extension (replaces a flat colour at the top).** Moving the presenter down leaves a gap at the top. Fill it from their own wall: take wall and ceiling rows from the top of the crop (output y 0 to 260, above the hair), flip vertically, stretch to y 0 to D + 200, heavy Gaussian blur (sigma 32 to 40), saturation 0.9, darken by about 0.78 at y 0 easing to 1.0, then blend with a vertical alpha mask (opaque to y D, smoothstep to transparent at y D + 200). Apply the grain after compositing. Checks on encoded frames: adjacent-row luminance step at most 2 levels across y D - 40 to D + 240 (lengthen the blend if it fails), luminance range inside the extension at least 6 levels, no part of the head inside it. For a still (a cover), the same effect is a 12 px row stretched with `scaleY(66)` plus a backdrop blur.

**3. Layout slides (FULL and ROOM).** FULL is the presenter as recorded; ROOM is shifted down by D (about +144 to +319 px, clamped so the chin stays at or above y 1576) so the top has room for graphics. The move between them is 16 frames and the extension grows and shrinks with it. A slide starts 16 frames before the graphic it makes room for and finishes before any text that would cross the eyes appears. Five slides were enough for 60 seconds; do not add or speed up slides to fix pacing. Graphic area in ROOM: y 270 to (eye-box top - 40), x 80 to 890.

**4. Low captions band.** One fixed band y 1600 to 1700 in every layout (it does not move with the layout), centred on x 540 within 2 px on the encoded frame, width at most 700 px, 1 to 3 words switching every 0.2 to 0.4 s, body font in the text colour with keywords in the emphasis font and accent colour (3 px text-colour outline), caption top at least 24 px below the chin. Hidden while a giant caption shows. Known risk: the band sits in the bottom UI zone of TikTok, Instagram and Shorts. Check one private upload on a phone before posting.

**5. Hook giant on the extension.** Rows slam on their spoken words: for example DESIGNERS, / ONE SKILL / *away* / FROM OWNING THE PRODUCT. A condensed bold face in the text colour with a contour, plus one serif italic accent row in the accent colour. If a row's contrast falls below 4.5:1 with its contour, put the giant on a glass card.

**6. Salary board (counting rows).** For job-pay facts. A title ("Just some examples of job postings") and a permanent footer saying what the figures are and are not. One row at a time slides in on its spoken word and the figure counts up from zero. A tag says ADVERTISED PAY (job-ad figures) or TYPICAL PAY (survey figures: dashed border plus a survey sub-line). The next row collapses the previous one. The footer stays at least 40 px above the eye box on every frame (assert it per frame). Shrink row gaps first, then the role line, never the tags or the footer. Use company logos only with permission; otherwise text. Every figure needs a source in the script file and a re-check on posting day. Never imply earnings are guaranteed.

**7. Tool logo row.** Tiles on a light background pop 3 frames before each tool word (`back.out`), settle, hold at least 1.5 s and exit together. A rule line can sit above ("6 WEEKS, NO CODING BACKGROUND NEEDED"). Logos only with an approved file and a provenance note; some companies require written permission for public use of their logo.

**8. Checklist with ticks.** Three rows (for example REAL CLIENT BRIEF, LIVE PRODUCT, CERTIFICATE), each on its spoken word, a tick 8 frames later, the whole card exiting together. Partner marks pop on their names.

**9. Honesty line.** Short text cards on the key phrases of an honest statement ("NOT AN ENGINEER OVERNIGHT", "A DESIGNER WHO SHIPS"), with the last word in the accent colour and a small icon. Used in the FULL layout.

**10. Offer card (sale, code, places, deadline, call to action).** A glass card builds line by line on the spoken words: brand line, sale name, end date, code chip, big CODE, discount, number of places, then the spoken call to action and the URL line. The URL card holds, settled and fully visible, to the last frame (no fade). Never add a call to action that was not spoken. Never fade the last spoken word.

**11. Cover (a still; 9:16 and 1:1).** Built as an HTML page and rendered by headless Chrome (`chrome --headless=new --window-size=1080,1920 --screenshot=out.png page.html`; the Chrome path differs by OS), not by a video render. Pieces: the presenter frame at the bottom with a masked top fade, the room extension above it (block 2) so it looks taken from the video, a tint over the top, the logos on light or dark tiles, a pill (the sale name), the hook rows in the giant style, a very large discount, and a chip (code, places, end date). Build both sizes from one script. Check by looking at the PNG: headline clear of hair and forehead, nothing blurry behind the presenter, same look as the video. Quality is limited by the source frame: ask for a good phone photo of the presenter before building the cover.

## Cutting a reel (the workflow that worked)

1. Transcribe locally; mark dead air and abandoned takes; keep the last clean take per beat; write a cut-decisions file for the owner (wrong figures, words the ASR heard differently, openings like "So that").
2. Words that were not said but must be shown become on-screen text, not retakes, when the owner agrees.
3. Look-downs (the glance at the phone to stop recording): trim only at silence; if a syllable would clip, hide the glance behind a card.
4. Plan first (scene table, trigger frames, geometry, QA list), then a brief with the owner's decisions quoted, then a 540x960 draft before the 1080x1920 final. At most two finals.
5. Final QA on the delivered file: ffprobe (1080x1920, 30 fps, planned duration), loudness, cut strips at every join, black/solid/freeze scan, first 2.5 s frame by frame, last 10 frames, face-box constancy, caption centring and clearance, extension seam, a fresh transcript against the script, lip sync at five joins, hashes of protected files.
6. A posting-day list kept separate from the build: re-check ads and figures, the code and places on the website, logo permission, owner approval, one private phone upload.

## Audio

See `skills/pb-edit-pipeline/SKILL.md` ("Audio") and `tools/audio/`.

## Status of the code

This repo ships the specifications, the audio tools and the plan templates. The original Hyperframes generators for these blocks contain one brand's content, so they are not included yet. Ask your planner model to turn each block above into a parameterised Hyperframes component that reads `brand/brand.json`, and build them one at a time with a sample gate after each.
