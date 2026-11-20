# Pack: third-party platforms and integrations

In one past project (a self-hosted social scheduler), every delay was an outside gate found mid-build. Find them before the plan exists. For each platform or API involved, answer every line below from the provider's current documentation or issue tracker, read in this session. Write "not checked" where you did not look.

## Gate checklist

- **Access level.** Is there a sandbox or development mode? What does it not allow (public posting, other users, real data)? What does production approval require: review form, demo video, privacy policy URL, verified domain, business verification? Typical wait?
- **Account and ownership.** Which account must own the app, page, channel or project? Must assets sit in a specific business portfolio or organisation? Personal versus business or creator account types?
- **Login and API changes.** Has the provider changed its login flow, API version or scopes recently? When a tool connects to several platforms, run one search of the tool's issue tracker per platform (open issues, newest first, platform name plus "login", "connect", "broken"). Do not stop after the first platforms turn up problems: in the 2026-11-15 proof run both models searched issues, found the LinkedIn and TikTok problems, and missed the Instagram login break that cost the real project the most time. If your lookup budget cannot cover every platform, list the unsearched ones as "issue tracker not checked".
- **Scopes and permissions.** Exact scopes needed, and which need review.
- **Limits and cost.** Rate limits, quotas, free-tier caps, paid features. Any cost needs the user's approval first.
- **Expiry.** Token lifetimes, refresh rules, snapshot and trial expiry. Put renewal dates in the handoff.
- **Owner-only steps.** Every login, consent screen, secret entry, video recording or button press only the user can do, batched into as few sittings as possible and in order.
- **Secrets.** Names and storage location only. Never values in chat or in notes.
- **Self-hosted pieces.** Snapshot before change, rollback command written down before deploy, other services on the host listed as untouched, backup restore rehearsed at least once.
- **Verification.** A read-only check that proves each connection works, and one real end-to-end action the user approves.

## Plan shape

1. Gates with waiting time first (approvals, verification, DNS).
2. One table: gate, owner, status, evidence, date checked.
3. Build steps only after the table shows no unknown rows.
4. A fallback for each gate that could be refused.
