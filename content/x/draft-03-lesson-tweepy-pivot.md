---
angle: lesson
status: draft
date: 2026-06-22
---

## POST TEXT
I automated tweeting. Deleted it 20 minutes later.

GitHub Action: draft PR merges, tweepy fires, no second look.

Then I thought: merge = published forever.

Stripped it back. Prints the draft now, I copy-paste.

AI built it. Where would you draw the line?

## REPLY LINK
https://freshfilings.dev

## Notes
Angle: lesson — commit 283a720 ("chore: remove tweepy posting, print draft to Actions summary instead") ripped out 38 lines of tweepy/Python setup from the GitHub Action the same day the pipeline was built. The pivot: fully automated posting felt right until you realize there's no human review before your public voice fires. Now the Action just prints the draft to GITHUB_STEP_SUMMARY and Noah copy-pastes manually.
Fresh vs log: origin (draft-01) and behind-the-scenes (draft-02) are both taken. This is the first lesson post and covers a different axis entirely. Draft-02 actually described the tweepy pipeline that was already stripped by the time this draft was written, so this is a natural honest follow-up to that irony.
Grounded in: real commit 283a720, dated 2026-06-13, in this repo (nrfischer10/freshfilings-content).
Caveat: freshfilings.dev returned 403 and nrfischer10/freshfilings is private; all facts sourced from git log in this repo.
