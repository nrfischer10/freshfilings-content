---
angle: lesson
status: draft
date: 2026-06-29
---

## POST TEXT
Claude almost auto-posted this tweet. Deleted 38 lines of code first.

Too many ways for the wrong post to go live while I'm not looking.

Now it just prints to the GitHub Action summary. I still hit send.

Have you ever over-built something and then pulled back?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson (pivot away from full automation).
Fresh vs log: origin (01) and behind-the-scenes (02) are the only prior angles. lesson is unused.
Grounded in: commit 283a720 (2026-06-13) "chore: remove tweepy posting, print draft to Actions summary instead" — 38 deletions, 12 insertions in .github/workflows/post-to-x.yml. The Action also lost write permissions (contents: write → read) since it no longer commits back to the repo. The original plan was full automation: merge PR → tweepy posts to X → Action marks draft as "posted" in log.md and pushes. That whole chain was pulled. Concrete number (38 lines) comes directly from the git diff stat.
Caveat: freshfilings.dev returned 403 and the main freshfilings repo is private, so this draft is grounded solely in the content repo's own git history.
