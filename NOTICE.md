# Third-party notices

This kit does not copy these projects. Setup downloads them from their own sources, which keep their own licences.

| Project | Source | Licence | How the kit uses it |
|---|---|---|---|
| Hyperframes | https://github.com/heygen-com/hyperframes | Apache-2.0 | Plugin installed through the agent's plugin manager, version 0.8.162 |
| Herk Edit Kit by Nate Herk | https://github.com/nateherkai/herk-edit-kit | MIT | Cloned at commit `10511e5af86fc47756ea89803b397422e2d89284` for its editing scripts and skills. Its ElevenLabs transcription script is NOT used (paid) |
| Ootto claude-content-skills | https://github.com/Ootto-AI/claude-content-skills | MIT | Hook and script techniques adapted (rewritten) in `skills/pb-content-craft`; licence text included there |
| FFmpeg | https://ffmpeg.org | LGPL/GPL, depends on build | Installed by your package manager |
| Parakeet speech model | Used through the Hyperframes `transcribe` command | See the Hyperframes docs | Local transcription, no upload |
| Fonts (Montserrat, DM Sans, Big Shoulders, Instrument Serif) | Google Fonts | SIL Open Font Licence | Optional examples only. Fonts are not bundled; setup downloads nothing unless you choose them in `brand.json` |

The skills in `skills/` were written by DI Dreamlabs and are MIT. Brand logos, footage and scripts from any specific creator or company are NOT part of this kit.
