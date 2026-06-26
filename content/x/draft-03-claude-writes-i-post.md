---
angle: lesson
status: draft
date: 2026-06-26
---

## POST TEXT
Claude writes my tweets. I still hit post myself.

The pipeline was real: GitHub Action, tweepy, auto-fire on PR merge.

Pulled the auto-post step. It prints the draft, I do the rest.

AI writes. I decide what goes live.

How much do you trust AI to publish for you?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson — the decision to remove tweepy auto-posting and keep a human in the loop.
Fresh vs log: origin (draft-01) and behind-the-scenes (draft-02) already used. First lesson post.
Grounded in: commit 283a720 (2026-06-13) "chore: remove tweepy posting, print draft to Actions summary instead". The full tweepy pipeline exists in scripts/post_to_x.py and .github/workflows/post-to-x.yml; the workflow was updated to skip the tweepy call and print the draft to GitHub Step Summary instead. All facts verified from repo files.
