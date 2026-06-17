---
angle: lesson
status: draft
date: 2026-06-17
---

## POST TEXT
Built auto-posting into my GitHub Action. Then deleted it.

Claude drafts, opens a PR, I merge. The Action was supposed to fire tweepy and post.

Yanked tweepy. Now it prints the draft and I post manually.

One review step before anything goes public. Is that too cautious?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson — removed tweepy auto-posting from the GitHub Action pipeline, pivoting to printing draft to Actions summary for manual review.
Fresh vs log: `lesson` angle unused so far; `behind-the-scenes` (draft-02) described the original pipeline with tweepy, but this documents the pivot away from full automation three days later.
Grounded in: commit 283a720 from 2026-06-13 "chore: remove tweepy posting, print draft to Actions summary instead."
Caveat: exact reason for removal not stated in commit message; framed as keeping a human review step before anything posts publicly, which matches the spirit of the change.
