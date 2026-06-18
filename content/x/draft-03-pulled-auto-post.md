---
angle: lesson
status: draft
date: 2026-06-18
---

## POST TEXT
I built a pipeline to auto-post tweets. Then I deleted the auto-post step.

Claude drafts, I merge the PR, GitHub Actions was going to post on merge. Cut that last part this week.

Turns out I want to read a tweet before it goes live. Where's your line on full AI automation?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson — the decision to pull tweepy auto-posting from the GitHub Action.
Fresh vs log: origin (draft-01) and behind-the-scenes (draft-02) are the only used angles. This is the first lesson post and covers a different event entirely.
Grounded in: commit 283a7202 on 2026-06-13 ("chore: remove tweepy posting, print draft to Actions summary instead") in freshfilings-content. The workflow now prints the draft to the GitHub Actions run summary instead of calling tweepy to post. The tweepy script (scripts/post_to_x.py) still exists but is no longer wired up.
Why it's interesting: the stated plan was full Claude-to-X automation (Claude drafts, PR opens, merge fires tweepy). The actual change shows a conscious pullback: human reads it before it posts. That tension (how far to let AI go with public-facing content) is exactly what the build-in-public audience debates.
Character count: 275 (under 280).
