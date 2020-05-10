import praw

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


multi_reddit()
