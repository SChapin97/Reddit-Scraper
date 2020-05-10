import praw
import time
import re

reddit = praw.Reddit("bot1", user_agent="Post Scraper")

def multi_reddit():
    u_user = reddit.user.me()
    u_mreddits = u_user.multireddits()

    for mreddit in u_mreddits:
    	print(mreddit.name, mreddit.visibility)
        for subreddit in mreddit.subreddits:
            print("   " + subreddit.display_name)
            top_posts(subreddit)


def bapcs_posts():
    bapcs = reddit.subreddit("buildapcsales")

    totalPosts = []

    for post in bapcs.hot():
        # print("totalPosts length:", len(totalPosts))
        if len(totalPosts) == 10:
            break
    # print(totalPosts)

    # print(post.title, "; ", post.score, post.created_utc)
    minutesSince = (time.time() - post.created_utc) // 60
    # print("Minutes Since:", minutesSince)

    if post.score > 0:  # and (post.score // minutesSince) > 0:
        m = re.search("(?P<type>\\[[^\\[\\]]+\\])\\s*(?P<item>[^$]+)(?P<price>\\$.+)", post.title)
        if m and m.group("type") == "[MONITOR]":
            print("Type:", m.group("type"), "; Item:", m.group("item"), "; Price:", m.group("price"))
            totalPosts.append(post)
            print("score per minute:", minutesSince // post.score, "; Title:", post.title)


def top_posts(subreddit):
    for post in subreddit.top("day", limit=3):
        print("      Points:", post.score, "Title:", post.title)

multi_reddit()
