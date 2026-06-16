---
angle: lesson
status: draft
date: 2026-06-16
---

## POST TEXT
I drafted a tweet bragging my GitHub Action auto-posts to X. Merged the PR. 8 minutes later I ripped that code out. It never posted.

Now it just prints drafts to a build log so I read them first.

Claude runs the company. Publishing without me? Not yet. Where's your line?

## REPLY LINK
https://github.com/nrfischer10/freshfilings-content/commit/283a7202db0c514999541d2c413b943950f7f3ef

## Notes
Angle: lesson (first use; origin and behind-the-scenes already used in drafts 01-02).

Grounded in real, current commit history of this content repo (verified with `git log` and `git show` locally, plus a public WebFetch check that the commit URL renders with no login wall):
- Commit d420599 (2026-06-13 11:57:25 ET): merged the PR containing draft-02, a tweet that says "A GitHub Action fires tweepy and posts it."
- Commit 283a720 (2026-06-13 12:05:12 ET), 7m47s later (rounded to 8 minutes): "chore: remove tweepy posting, print draft to Actions summary instead." Diff confirms tweepy/API-credential steps were deleted and replaced with a step that writes the draft to $GITHUB_STEP_SUMMARY.
- log.md currently shows draft-02's status as still "draft," not "posted," confirming the tweepy auto-post step never completed for that tweet, i.e. the tweet bragging about auto-posting never actually went out via that pipeline. No invented numbers, all timestamps and statuses pulled directly from this repo's git history.

IMPORTANT CAVEAT FOR NOAH: this draft documents that the auto-post-to-X mechanism (tweepy) has been removed from .github/workflows/post-to-x.yml as of the commit above. Right now, merging a draft PR (including this one) will only print the post to the GitHub Actions job summary, it will NOT actually post to X automatically. If you want this and future drafts to auto-post on merge, the workflow needs the tweepy/API steps restored (or a new posting mechanism added). Flagging this since the task brief assumed auto-posting is live.
