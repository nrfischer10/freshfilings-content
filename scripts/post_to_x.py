#!/usr/bin/env python3
"""
Post an approved X draft to @FreshFilings and reply with the link.

Called by .github/workflows/post-to-x.yml when a draft-*.md file is
added to main. Expects four env vars: X_API_KEY, X_API_SECRET,
X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET. Also expects DRAFT_FILE to be
set by the workflow.

Draft format the cloud agent must produce (sections are parsed literally):

  ## POST TEXT
  <tweet text, ≤ 280 chars>

  ## REPLY LINK
  <URL to post as first reply, or "none">

Anything else in the file (notes, angle, reasoning) is ignored.
"""

import os
import re
import sys
import tweepy


def parse_draft(path: str) -> tuple[str, str | None]:
    with open(path) as f:
        text = f.read()

    post_match = re.search(
        r"##\s*POST TEXT\s*\n(.*?)(?=\n##|\Z)", text, re.DOTALL | re.IGNORECASE
    )
    if not post_match:
        print("ERROR: no '## POST TEXT' section found in draft.")
        sys.exit(1)
    post_text = post_match.group(1).strip().strip("`").strip()

    link_match = re.search(
        r"##\s*REPLY LINK\s*\n(.*?)(?=\n##|\Z)", text, re.DOTALL | re.IGNORECASE
    )
    reply_link: str | None = None
    if link_match:
        candidate = link_match.group(1).strip().strip("`").strip()
        if candidate.lower() not in ("none", ""):
            reply_link = candidate

    return post_text, reply_link


def main() -> None:
    draft_file = os.environ.get("DRAFT_FILE")
    if not draft_file:
        print("ERROR: DRAFT_FILE env var not set.")
        sys.exit(1)

    post_text, reply_link = parse_draft(draft_file)
    print(f"Posting ({len(post_text)} chars):\n{post_text}")
    if reply_link:
        print(f"Reply link: {reply_link}")

    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )

    response = client.create_tweet(text=post_text)
    tweet_id = response.data["id"]
    print(f"Posted: https://x.com/i/web/status/{tweet_id}")

    if reply_link:
        client.create_tweet(text=reply_link, in_reply_to_tweet_id=tweet_id)
        print(f"Reply posted with link: {reply_link}")


if __name__ == "__main__":
    main()
