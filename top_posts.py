import praw

reddit = praw.Reddit("bot1", user_agent="Post Scraper")

def multi_reddit():
    u_user = reddit.user.me()
    u_mreddits = u_user.multireddits()
    i = 0

    for mreddit in u_mreddits:
        print("<h1>" + mreddit.name + "</h1>")
        for subreddit in mreddit.subreddits:
            print("<h2>" + subreddit.display_name + "</h2>")
            top_posts(subreddit)

    print("\t</body>\n</html>")

def top_posts(subreddit):
    for post in subreddit.top("day", limit=5):
        print("\t\t<div>")
        print("\t\t\t<a href=\"http://redd.it/" + post.id + "\">" + post.title + "</a>")
        #TODO: Fix type conversion issues
        #print("\t\t\t<p>Score:", str(post.score) + " (" + str(int(post.upvote_ratio * 100)) + "%);", "Comments:", post.num_comments +"</p>")
        if "http" in post.thumbnail:
            print("\t\t\t<img src=\"" + post.thumbnail + "\" alt = \"Thumbnail image from the post\">")
        if (not "redd.it" in post.url) and (not post.id in post.url) :
            print("\t\t\t<a href=\"" + post.url + "\">Outgoing link</a>")
        print("\t\t</div>")


multi_reddit()
