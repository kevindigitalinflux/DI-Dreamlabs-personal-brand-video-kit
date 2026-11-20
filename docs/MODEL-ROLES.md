# Model roles: plan with the strongest, build with the workhorse

| Job | Use | Why |
|---|---|---|
| Plan, write briefs, review, decide design tradeoffs, security-sensitive choices | **Claude Opus** (current best: Opus 5.5, id `claude-opus-5-5`), or the strongest Codex model your account offers (**Codex Astra**, a Codex model; pick it in your Codex model picker) | Deeper reasoning, catches the misread the builder would make |
| Build: generators, compositions, scripts, long renders, QA runs | **Claude Sonnet** (current: Sonnet 5.5, id `claude-sonnet-5-5`), or Codex at **high effort** (**Codex Sol 6.2** at high reasoning effort) | Fast and cheap enough to iterate |

Codex Astra and Codex Sol 6.2 are two Codex models named by the kit's creator; the exact ids come from your own Codex model picker, which may differ by account and over time. If one is not offered to you, use the closest: the highest-reasoning model for planning, a workhorse model at high effort for building. Your agent checks what is available before assuming.

## How the hand-off works

1. **Plan** (planner model): result first, surface map, gates, plan, risks. Writes `plan.md` and a build brief from `templates/`.
2. **Sample gate** (you): look at the smallest sample (a style frame, one scene, an A/B audio pair). Reply in your own words. Record them verbatim.
3. **Build** (builder model): follows the brief step by step, stops at the gates, never decides a design question on its own.
4. **Review** (planner model): checks the delivered file against the plan with evidence (frames, numbers), lists what was not verified.
5. **You** watch and listen. Only you approve publishing.

One writer at a time per project folder. If the same agent plans and builds, switch to the planning model for step 1 and 4 and the builder for step 3.

## Switching models

- Claude Code: `/model` and choose Opus for planning, Sonnet for building.
- Codex: choose the model and reasoning effort in the picker (or `-m` and `-c model_reasoning_effort="high"`; confirm flags with `codex --help`).
