---
angle: lesson
status: draft
date: 2026-06-24
---

## POST TEXT
Built a bot that auto-posted my tweets. Killed it after one day.

Claude drafts, GitHub Action fires, tweet goes live. It worked.

But I pulled the tweepy call. Now I approve via PR merge. Same pipeline, one human checkpoint.

I'm not ready to fully hand my voice to AI. Are you?

## REPLY LINK
https://github.com/nrfischer10/freshfilings-content/commit/283a7202db0c514999541d2c413b943950f7f3ef

## Notes
Angle: lesson — tried full auto-posting via tweepy, then removed it and kept a human-in-the-loop approval step (PR merge before anything posts).
Fresh vs log: origin (draft-01) and behind-the-scenes (draft-02) are the only prior angles; lesson is unused.
Grounded in: real commit 283a720 on 2026-06-13 in freshfilings-content, message "chore: remove tweepy posting, print draft to Actions summary instead" — the exact moment the auto-post was pulled back.
Caveat: freshfilings.dev returned 403 and the private freshfilings repo is inaccessible without auth, so grounded in freshfilings-content commit history instead of the main product repo.
