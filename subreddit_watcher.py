import praw
import time
import os
import sys

REDDIT_WRAPPER = praw.Reddit("bot1", user_agent="Post Scraper")
POST_REDUNDANCY_FILE_PATH = "previous_posts"

def main():
    #Currently only want to print ONE of the subreddits due to
    #    template.html being handled outside of this script.
    #TODO: Look into handling of the template inside of this script
    if "buildapcsales" in str(sys.argv):
        buildapcsales()
    elif "laptopdeals" in str(sys.argv):
        laptopdeals()
    elif "gamecube" in str(sys.argv):
        gamecube()
    elif "vive" in str(sys.argv):
        vive()
        
##Subreddit-specific functions
def buildapcsales():
    search_items = ["print", "lamp", "ikea", "CPU"]

    subreddit = REDDIT_WRAPPER.subreddit("buildapcsales")
    iterate_posts(subreddit, search_items)


def laptopdeals():
    search_items = ["xps", "thinkpad", "mac"]

    subreddit = REDDIT_WRAPPER.subreddit("laptopdeals")
    iterate_posts(subreddit, search_items)


def gamecube():
    search_items = ["loader", "restock"]

    subreddit = REDDIT_WRAPPER.subreddit("gamecube")
    iterate_posts(subreddit, search_items)


def vive():
    search_items = ["restock", "deluxe", "strap", "wireless"]

    subreddit = REDDIT_WRAPPER.subreddit("vive")
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
    #TODO: Might have to do some character replacement for HTML escaping
    print("\t\t<div>")
    print("\t\t\t<a href=\"http://redd.it/" + post.id + "\">" + post.title + "</a>")
    print("\t\t\t<a href=\"" + post.url + "\">Link to the product</a>")
    if "http" in post.thumbnail:
        print("\t\t\t<img src=\"" + post.thumbnail + "\" alt = \"Thumbnail image from the post\">")
    print("\t\t</div>")

main()
