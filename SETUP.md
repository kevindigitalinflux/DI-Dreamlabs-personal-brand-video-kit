# SETUP: runbook for the AI agent

You are an AI coding agent (Claude Code or Codex). A person pasted a one-line prompt asking you to follow this file. Your job: set up their personal-brand video studio. Be plain and kind; they may not be technical. Do the steps in order. Never skip a stop.

## Rules while setting up

- Detect first, install second. Show ONE list of everything you plan to install (name, source, rough size, why). Wait for ONE yes. Then install.
- Always stop and ask before: logins, paid services or API keys, uploads or publishing, deleting anything, changing system settings beyond installing the listed tools.
- Never ask the person to paste a secret into chat. Never write a secret into a file in this repo.
- If a command fails, show the exact error, try one reasonable fix, and if it fails again stop and explain in one short paragraph. Do not loop.
- Record what you did in `SETUP-LOG.md`: command, result, version.

## Step 1: ask four short questions

1. Which agent are you running in (Claude Code or Codex), and do you also use the other one?
2. Windows, Mac or Linux? (Detect it yourself, then confirm.)
3. Where should video projects live? (Default: a `videos` folder next to this repo.)
4. Do you record with OBS, a phone, or both? (If neither is installed, offer OBS Studio only if they will record on the computer.)

## Step 2: detect what is already installed (read-only)

Run and record versions. On Windows use PowerShell; on Mac and Linux use bash. You can run `scripts/check-env.ps1` or `scripts/check-env.sh` from this repo, which only prints versions.

| Need | Check | Minimum |
|---|---|---|
| Node.js | `node --version` | 22 |
| Git | `git --version` | any recent |
| FFmpeg and FFprobe | `ffmpeg -version` and `ffprobe -version` | 6 or newer |
| Python | `python --version` or `python3 --version` | 3.10 (the audio tools use only the standard library) |
| Chrome or Chromium (cover images) | Windows: look in `Program Files\Google\Chrome`; Mac: `/Applications/Google Chrome.app` | any |
| OBS Studio (optional, for recording) | look in Program Files or Applications | 30 or newer |
| Claude Code | `claude --version` | current |
| Codex CLI | `codex --version` | current |

## Step 3: show the install plan and wait for one yes

Only list what is missing. Typical install commands (use the package manager the person already has):

| OS | Command |
|---|---|
| Windows (winget) | `winget install OpenJS.NodeJS.LTS`, `winget install Git.Git`, `winget install Gyan.FFmpeg`, `winget install Python.Python.3.12`, optional `winget install Google.Chrome`, `winget install OBSProject.OBSStudio` |
| Mac (Homebrew) | `brew install node git ffmpeg python`, optional `brew install --cask google-chrome obs` |
| Linux (apt, example) | `sudo apt install nodejs npm git ffmpeg python3 chromium` (check Node is 22 or newer; otherwise use nvm) |

Also in the plan:

- **Hyperframes plugin** (open source, Apache-2.0, renders video from HTML). Official source: https://github.com/heygen-com/hyperframes. This kit was built and tested with version **0.8.162**.
  - Claude Code (from the official README): `claude plugin marketplace add heygen-com/hyperframes` then `claude plugin install hyperframes@hyperframes`.
  - Codex (verified against Codex CLI 0.170.0 `--help`, and against a working install of 0.8.162): `codex plugin marketplace add heygen-com/hyperframes@v0.8.162` (the `owner/repo@ref` form pins the release tag) then `codex plugin add hyperframes@hyperframes`. Restart Codex afterwards. Confirm with `codex plugin list`.
  - After installing, find the plugin's pinned launcher: `<plugin root>/skills/hyperframes/scripts/plugin-cli.mjs`. Record the plugin version. If it is not 0.8.162, tell the person; the kit probably still works, but run the self-test in Step 7 and report any difference.
  - Set `HYPERFRAMES_NO_TELEMETRY=1` when running Hyperframes commands unless the person says otherwise.
- **Herk Edit Kit** (MIT, editing scripts and skills by Nate Herk): `git clone https://github.com/nateherkai/herk-edit-kit herk-edit-kit`, then `git -C herk-edit-kit checkout 10511e5af86fc47756ea89803b397422e2d89284`, then `npm ci` inside it. Do NOT use its ElevenLabs transcription script (paid). Transcription here is local Parakeet through Hyperframes (`transcribe --engine parakeet`).
- **This kit's skills** copied into the agent's skills folder (Step 5).

Say plainly: "This installs open-source tools on your computer. Nothing is uploaded and nothing costs money. Reply yes to start, or tell me what to leave out."

## Step 4: install

Run the commands the person approved. After each, re-run its check from Step 2. Restart the terminal or agent when the PATH changes and tell the person.

## Step 5: install the skills

Copy folders (never overwrite an existing folder without asking):

| Agent | Destination |
|---|---|
| Claude Code | `~/.claude/skills/` (on Windows `C:\Users\<name>\.claude\skills\`) |
| Codex | `~/.codex/skills/` |

Copy from this repo: `skills/pb-video-style`, `skills/pb-edit-pipeline`, `skills/pb-content-craft`, `skills/fable-mode`.
Copy from `herk-edit-kit/.claude/skills/`: `edit-video`, `cut-silences`, `cut-mistakes`, `short-form-edit`, `short-form-video`, `video-storytelling`, `hyperframes-video-beats`, `style-library`.
Do not copy Herk's Hyperframes skill folders; the Hyperframes plugin provides its own, version-matched.

Tell the person to restart the agent so the skills load. Verify by asking the agent to list its skills.

## Step 6: brand interview

Read `brand/BRAND-INTERVIEW.md`. Ask the questions in groups of two or three. Write `brand/brand.json` from `brand/brand.example.json`. Put logo files they give you in `brand/logos/` (git-ignored). For any logo that is not theirs, ask whether they have written permission to use it publicly; if not, use text instead.

## Step 7: self-test (about two minutes, no uploads)

1. Print the versions of `ffmpeg`, `ffprobe`, `node`, `python`.
2. Create a Hyperframes test project in a temp folder with the pinned launcher: `node <launcher> init selftest --non-interactive`, then inside it `node <launcher> check --timeout 30000 --json`, then a short draft render. Confirm an MP4 exists with `ffprobe`.
3. Run `python tools/audio/comb_detect.py --help` to confirm Python works.
   Also build the component demo: `node components/instantiate.mjs brand/brand.json <project>/demo` (use `brand/brand.example.json` if there is no brand.json yet), then `node <launcher> lint` and `node <launcher> check --timeout 60000 --json` inside it. Expect 0 errors.
4. Report PASS or FAIL for each line in a small table with the versions found. Delete the temp folder only after telling the person.

## Step 8: hand over

Give the person a short summary (what was installed, where, what to say next) and these starter prompts:

- "Plan my first reel. Use fable-mode. Ask me what I need to decide."
- "Here is my recording. Transcribe it, find the mistakes and silences, and give me a cut list to approve."
- "Make a cover for this video in the same style."

Explain the model split from `docs/MODEL-ROLES.md`: plan with the strongest model (Claude Opus, or the best Codex model), build with the workhorse (Claude Sonnet, or Codex at high effort). Ask which they want to use now and set it.

## What you must NOT do during setup

- Do not install anything not on the approved list.
- Do not log in to any service, add API keys, or start any paid feature.
- Do not upload their footage anywhere. Cloud "listen" checks (for example Gemini) need a separate, specific yes per file.
- Do not post, schedule or publish.
