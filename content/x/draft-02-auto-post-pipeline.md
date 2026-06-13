---
angle: behind-the-scenes
status: draft
date: 2026-06-13
---

## POST TEXT
Claude writes my tweets. Here's exactly how.

It opens a PR in a public GitHub repo with the draft. I read it, merge if it's good. A GitHub Action fires tweepy and posts it.

I never touched the keyboard for this one. Does that feel weird to you, or is it just efficient?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: behind-the-scenes — the auto-posting pipeline (Claude drafts post, opens PR, GitHub Action calls tweepy on merge).
Fresh vs log: only `origin` used so far; this is the first behind-the-scenes post and a different axis entirely.
Grounded in: the 2026-06-13 freshfilings-content initial commit, which explicitly sets up "GitHub Action for auto-posting" and "tweepy posting script" in a separate public repo "so cloud agents can access this public repo without auth issues." That commit is the real event this post documents.
Caveat: freshfilings.dev returned 403 and the main freshfilings repo is private, so no live commit details from there. All facts used come from the commit message and the session context provided by Noah.
