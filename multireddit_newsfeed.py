import praw
import html

reddit = praw.Reddit("bot1", user_agent="Post Scraper")
IMAGE_FORMATS = ["jpeg", "jpg", "png", "gif"]

def multi_reddit():
    u_user = reddit.user.me()
    u_mreddits = u_user.multireddits()

    for mreddit in u_mreddits:
        print("\t<h1>" + mreddit.name + "</h1>")
        for subreddit in mreddit.subreddits:
            print("\t<h2>" + subreddit.display_name + "</h2>")
            top_posts(subreddit)

    print("\t</body>\n</html>")

def top_posts(subreddit):
    for post in subreddit.top("day", limit=5):
        #If a url starts with /r/, it is a x-post and needs to have reddit.com prepended to it.
        url = post.url
        if url.startswith('/r/'):
            url = 'https://reddit.com' + url

        print("\t\t<div>")
        print("\t\t\t<a href=\"http://redd.it/" + post.id + "\" class=\"post\">" + html.escape(post.title) + "</a>")
        if "http" in post.thumbnail:
            if is_image(url):
                print("\t\t\t<a href=\"" + url + "\" class=\"image\"><img src=\"" + url + "\" alt=\"Full sized image from the post\" class=\"image\"></a>")
            else:
                print("\t\t\t<a href=\"" + url + "\" class=\"image\"><img src=\"" + post.thumbnail + "\" alt=\"Thumbnail image from the post\" class=\"image\"></a>")

        elif (not "redd.it" or "reddit" in url) and (not post.id in url) :
            print("\t\t\t<a href=\"" + url + "\" class=\"link\">Outgoing link</a>")
        print("\t\t</div>")


def is_image(url):
    for format in IMAGE_FORMATS:
         if url.endswith(format):
             return True
    else:
        return False

multi_reddit()
