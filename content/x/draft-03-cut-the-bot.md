---
angle: lesson
status: draft
date: 2026-06-20
---

## POST TEXT
I built a bot to tweet for me. Then I cut it.

It worked: Claude drafts, opens PR, Action fires tweepy on merge. But auto-posting for a brand with 0 customers felt like too much.

Now it prints the draft. I read it. I decide.

What's the one thing you still won't automate?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson — the decision to roll back tweepy auto-posting from the GitHub Actions workflow.
Fresh vs log: origin (01) and behind-the-scenes (02) are taken. This is the first lesson post and covers a specific, verifiable event: commit 283a720 in this repo "chore: remove tweepy posting, print draft to Actions summary instead," which walked back the pipeline described in draft-02.
Grounded in: git log of freshfilings-content shows that commit as the most recent change, removing tweepy from the workflow and replacing it with printing the draft to Actions summary for human review.
Caveats: freshfilings.dev returned 403 and the main freshfilings repo is private, so all facts come from this content repo's git history and the session context provided. "0 customers" sourced from session context.
