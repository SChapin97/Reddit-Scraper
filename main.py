import praw
import time
import re

reddit = praw.Reddit("bot1", user_agent="Post Scraper")

def multi_reddit():
    u_user = reddit.user.me()
    u_mreddits = u_user.multireddits()

    for mreddit in u_mreddits:
        print(mreddit.name)
        for subreddit in mreddit.subreddits:
            print(" " + subreddit.display_name)
            top_posts(subreddit)


def top_posts(subreddit):
    for post in subreddit.top("day", limit=5):
        print("   ", post.title)
        print("       Score:", str(post.score) + " (" + str(int(post.upvote_ratio * 100)) + "%);",
              "Comments:", post.num_comments)
        print("       Post:", "https://www.reddit.com" + post.permalink)
        if post.url != "https://www.reddit.com" + post.permalink:
            print("       Link:", post.url)


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

multi_reddit()
