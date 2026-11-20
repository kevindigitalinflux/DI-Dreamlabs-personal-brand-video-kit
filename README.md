# DI Dreamlabs personal brand video kit

An open-source starter kit that turns an AI coding agent (Claude Code or Codex) into a personal-brand video studio: it plans, cuts, captions, animates and checks short talking-head videos (Reels, TikTok, Shorts) and long educational videos, using free local tools.

Built by DI Dreamlabs from a real production: a 60-second sales reel, its cover, and four educational videos.

## Install (copy and paste into your agent)

Open Claude Code or Codex in an empty folder where you want your video projects to live, and paste:

```
Read https://raw.githubusercontent.com/kevindigitalinflux/DI-Dreamlabs-personal-brand-video-kit/main/SETUP.md and follow it. Ask me before installing anything.
```

The agent will:

1. Check what is already on your computer (Node, Git, FFmpeg, Python, Chrome, OBS, your agent's plugins).
2. Show you one list of everything it wants to install, with source and size, and wait for ONE yes.
3. Install the tools, the Hyperframes video plugin (pinned version), the editing scripts and the skills in this repo.
4. Interview you for your brand (colours, fonts, logos, audience) and write `brand/brand.json`.
5. Run a self-test so you know it works.

Logins, paid services, uploads and publishing always stop and ask you. Nothing is posted anywhere without your explicit yes.

## What you get

| Folder | What it is |
|---|---|
| `SETUP.md` | The runbook your agent follows to set everything up |
| `skills/` | Skills for your agent: `pb-video-style` (the look and motion graphics), `pb-edit-pipeline` (cutting, audio, QA), `pb-content-craft` (hooks and scripts), `fable-mode` (the deep-work runbook that makes planning better) |
| `docs/MODEL-ROLES.md` | Which model plans and which builds, and how to hand work between them |
| `docs/WORKFLOW.md` | The end-to-end process from idea to approved video |
| `docs/REEL-9x16-BLOCKS.md` | The motion-graphics components: room extension, layout slides, captions, pay board, logo row, checklist, offer card, cover |
| `docs/LESSONS.md` | Real mistakes and fixes (hollow audio from two microphones, zoom bugs, cleanup) |
| `tools/audio/` | Python tools (standard library only) to detect and fix a comb-filter echo and to build the final voice track |
| `templates/` | Plan and Codex brief templates |
| `brand/` | `brand.example.json` and the brand interview. Your real `brand.json` and logos are git-ignored |
| `scripts/` | Check scripts for Windows (PowerShell) and Mac/Linux (bash) |

## The planning and building split

Use a strong reasoning model to plan and review, a fast workhorse model to build. See `docs/MODEL-ROLES.md`.

- Plan and review: Claude Opus (or the strongest Codex model available to you).
- Build: Claude Sonnet, or Codex at high effort.
- Every build starts from a written plan and a brief, and stops at gates where you look at a small sample before the expensive render.

## Rules this kit enforces

- No music or sound effects unless you decide otherwise. No AI voice.
- No zooms or punch-ins in reels. No stick figures or clip-art.
- Logos only with permission, and never on your accent colour.
- Never invent numbers, results or claims. Never add a call to action you did not say.
- Local transcription (Parakeet through Hyperframes). No paid transcription services.
- At most two full final renders per video. Drafts first.

## Licence

MIT. See `LICENSE` and `NOTICE.md` for the third-party tools this kit installs (Hyperframes Apache-2.0, Herk Edit Kit MIT). This kit contains no logos, footage or scripts from any brand.
