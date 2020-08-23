import praw
import time
import os
import sys
import html

REDDIT_WRAPPER = praw.Reddit("bot1", user_agent="Post Scraper")
POST_REDUNDANCY_FILE_PATH = "previous_posts"
IMAGE_FORMATS = ["jpeg", "jpg", "png", "gif"]

def main():
    #Currently only want to print ONE of the subreddits due to
    #    template.html being handled outside of this script.
    #TODO: Look into handling of the template inside of this script
    if "buildapcsales" in str(sys.argv):
        buildapcsales()
    elif "laptopdeals" in str(sys.argv):
        laptopdeals()

##Subreddit-specific functions
def buildapcsales():
    search_items = ["print", "lamp", "ikea", "CPU"]

    subreddit = REDDIT_WRAPPER.subreddit("buildapcsales")
    iterate_posts(subreddit, search_items)


def laptopdeals():
    search_items = ["xps", "thinkpad", "mac"]

    subreddit = REDDIT_WRAPPER.subreddit("laptopdeals")
    iterate_posts(subreddit, search_items)


##Generic functions
#Generic function to go through each posts on a subreddit's new posts list
def iterate_posts(subreddit, search_items):
    #Making sure that previous_posts exists
    if not os.path.exists(POST_REDUNDANCY_FILE_PATH):
        f = open(POST_REDUNDANCY_FILE_PATH, "w")
        f.close()

    printed_posts = False #Used so we can output the end of the html doc

    for post in subreddit.new():
        printable = False
        for item in search_items:
            if item.upper() in post.title.upper():
                printable = True
                break

        if not printable:
            continue

        #Looking to see if the ID has already been found by the script
        redundant_file = open(POST_REDUNDANCY_FILE_PATH, "r")
        found = False

        for line in redundant_file.readlines():
            if post.id in line:
                found = True

        #If the post ID has not been found, then we want to print the post information
        if not found:
            redundant_file = open(POST_REDUNDANCY_FILE_PATH, "a")
            #Adding to the redundant post file
            redundant_file.write(post.id + "\r\n")
            redundant_file.close()
            printPost(post)
            printed_posts = True

    if printed_posts:
        print("\t</body>\n</html>")


#Generic print post information function
def printPost(post):
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
    print("\t\t\t<a href=\"" + url + "\" class=\"link\">Link to the product</a>")
    print("\t\t</div>")

def is_image(url):
    for format in IMAGE_FORMATS:
        if url.endswith(format):
            return True
    else:
        return False

main()
