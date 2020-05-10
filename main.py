import praw
import time
import re

reddit = praw.Reddit("bot1", user_agent="Post Scraper")

bapcs = reddit.subreddit("buildapcsales")

totalPosts=[]

for post in bapcs.hot():
    # print("totalPosts length:", len(totalPosts))
    if len(totalPosts) == 10:
        break;
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
