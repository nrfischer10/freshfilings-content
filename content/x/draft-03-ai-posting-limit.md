---
angle: lesson
status: draft
date: 2026-06-30
---

## POST TEXT
Almost gave Claude the keys to my Twitter account.

Plan was: Claude drafts, I merge the PR, GitHub Action fires tweepy. Zero human touch.

Sat with it for a day. Nope. Pulled the tweepy step. Claude still writes these, I still post.

Where do you draw the line with AI?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson — the decision to remove tweepy auto-posting and keep a human in the loop.
Fresh vs log: origin (#1) and behind-the-scenes (#2) are the only prior angles. This is the first lesson post and hasn't been touched.
Grounded in: the real 2026-06-13 commit "chore: remove tweepy posting, print draft to Actions summary instead" in freshfilings-content. The original pipeline (Claude drafts, PR merge triggers tweepy) was replaced with printing the draft to the Actions summary so a human still posts.
Caveat: the freshfilings repo is private so commit access was via freshfilings-content only. All claims trace directly to that commit message.
