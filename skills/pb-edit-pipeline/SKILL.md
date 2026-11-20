---
name: pb-edit-pipeline
description: Use for any personal-brand video edit (Reel, TikTok, Short, long educational video) built with Hyperframes: cutting silences and mistakes, transcribing locally, audio and loudness, captions, rendering, and the checks before the owner sees a draft. Trigger on "edit this video", "cut the pauses", "build the video", "make the Reel", "fix the audio", "motion graphics".
---

# Personal-brand edit pipeline

Overlay on the Herk Edit Kit skills (MIT, https://github.com/nateherkai/herk-edit-kit, commit 10511e5) that SETUP.md installs. Upstream wins on editing craft. THIS file wins on brand, tools, spending, audio and approvals. Read `brand/brand.json` first. Load `fable-mode` for any multi-step build.

## Where things live

- Video projects: the folder chosen in setup, one folder per video: `raw/` (never edited), `edit/` (plans, cut lists, briefs, QA), `hf/` (the Hyperframes project), `out/` (finals).
- Hyperframes is run through the plugin's pinned launcher (`<plugin root>/skills/hyperframes/scripts/plugin-cli.mjs`, tested with 0.8.162), with `HYPERFRAMES_NO_TELEMETRY=1`. Never upgrade mid-video.
- Audio tools: `tools/audio/` in this kit (comb_detect.py, comb_fix.py, build_voice.py).

## Rules that win over upstream

1. Brand tokens, fonts and logo rules come from `brand/brand.json`. Logos sit on the background or text colour, never on the accent colour. Use a tool or company logo only with an approved file; otherwise write the name as text.
2. Captions: 1 to 3 words, body font in the text colour, keywords in the emphasis font and accent colour with an outline, centred on x = 540 on 1080x1920 (measure the encoded frame to within 2 px), never over the mouth or chin. For reels, a fixed low band (y 1600 to 1700) worked, but it sits in the platforms' bottom UI zone: test one private upload on a phone before posting.
3. Transcription: local Parakeet through Hyperframes (`transcribe --engine parakeet`). No paid transcription (ElevenLabs, Whisper APIs and the like) without the owner naming the service and the spend in advance. ASR mishears names and numbers: ask the speaker what they said (it once heard "thirteen" for "thirty").
4. Music and sound effects: none unless the owner decides. No AI voice. Never fake a real person's likeness or voice.
5. Images: free-licence stills (Pexels, Pixabay, Unsplash) shown to the owner BEFORE download and logged with URL, author, licence and date; AI-generated assets only with the owner's yes, logged (tool, prompt, date).
6. Delivery: 1080x1920 30 fps H.264 AAC for reels; 1920x1080 for long videos. About -14 LUFS integrated, true peak at or below -1.5 dBTP, measured on the delivered stereo file. Never fade the last spoken word.
7. Approvals: the owner directs. No uploads, publishing, logins or paid calls without an explicit yes. A cloud listen (for example Gemini) is a separate yes per file.
8. Content: never invent numbers or results. Never add a call to action the speaker did not say. Health, pay and income claims stay plain and sourced, with a footer saying what the figures are and are not.

## Audio (approved method for talking heads)

1. Record with ONE microphone source active in OBS. Two sources summed (for example the laptop mic and a USB mic) cause a comb filter and a hollow voice that cannot be fully fixed in post. Test 10 seconds; the peak should stay below -6 dBFS.
2. If a take is already hollow: `python tools/audio/comb_detect.py audio16k.wav` finds the delay; `python tools/audio/comb_fix.py source.mkv fixed.wav --delay-ms <delay>` reduces it on the WHOLE raw recording, before cutting.
3. Cut at real silence boundaries from FFmpeg `silencedetect`, never inside a phrase. ASR word end times are unreliable (they stretch to the next word).
4. `python tools/audio/build_voice.py fixed.wav cutlist.json voice.wav`: 3 ms edge fades, one gain to -14 LUFS measured on dual-mono stereo, oversampled limiter with `level=0`.
5. No EQ, compression, de-clipping, noise reduction or per-clip level matching. In the production this came from, the owner listened to A/B files and rejected the processed chain.
6. Always give the owner A/B files and record their words. Never choose for them.

## Reels: what to do and not do

- No zooms or punch-ins. Constant presenter scale. Check on encoded frames: face-box width constant within 1 percent per segment.
- Use layout slides, the room extension, the pay board and the other blocks in `skills/pb-video-style` and `docs/REEL-9x16-BLOCKS.md`.
- Look-downs (the speaker glances at the phone to stop recording): trim only at silence; if a syllable would clip, hide the glance behind a card.
- Words that were not said but must be shown ("advertised", "typically", the place) go on screen as text, not retakes, when the owner agrees.
- Draft at 540x960; at most two full 1080x1920 finals; keep a posting-day list (ads, figures, codes, logo permission, one private phone upload) separate from the build.

## Order of work

Script and hook BEFORE recording, record, transcribe, silences and mistakes (owner reviews candidates), story beats, plan (`templates/PLAN.md`), brief (`templates/BUILD-BRIEF.md`), build in Hyperframes, checks, draft, owner reviews, fix, final. Record every new lesson in `docs/LESSONS.md`.

## Checks before the owner sees a draft

- Frame strips (about 10 frames each side) across every cut.
- Lip sync against the raw.
- Contrast behind every caption, measured on the encoded frame.
- Every word whole at each cut: transcribe the final file and compare; ASR cannot prove a clipped word, so the owner listens.
- First 2.5 s frame by frame, nothing over the mouth; last 10 frames show the call to action.
- Loudness and true peak on the delivered file; zero clipped samples.
- ffprobe: size, 30 fps, duration, audio 48 kHz stereo.
- Black, solid-colour and freeze scan; check panel areas, not only whole frames.
- AI "watch" reviews are noisy: verify every complaint on real frames before acting. The owner's viewing is the final gate.

## Cleanup after delivery

Only after the owner confirms the finals are safe elsewhere: list the temporary files (review and QA frames, frame caches, superseded masters, transcodes, old builds) with sizes, ask, then delete. Keep finals, the approved project, the style kit, plans, scripts and raw recordings.
