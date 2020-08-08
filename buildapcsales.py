import praw
import time
import os

reddit = praw.Reddit("bot1", user_agent="Post Scraper")
searchItems = ["print", "lamp", "ikea", "CPU"]
post_redundancy_file_path = "previous_posts"

def bapcs_posts():
    bapcs = reddit.subreddit("buildapcsales")
    printedPosts = False #Used so we can output the end of the html doc

    #Making sure that previous_posts exists
    if not os.path.exists(post_redundancy_file_path):
        f = open(post_redundancy_file_path, "w")
        f.close()

    for post in bapcs.new():
        printable = False
        for item in searchItems:
            if item.upper() in post.title.upper():
                printable = True
                break

        if not printable:
            continue

        #Looking to see if the ID has already been found by the script
        redundant_file = open(post_redundancy_file_path, "r")
        found = False

        for line in redundant_file.readlines():
            if post.id in line:
                found = True

        #If the post ID has not been found, then we want to print the post information
        if not found:
            redundant_file = open(post_redundancy_file_path, "a")
            #Adding to the redundant post file
            redundant_file.write(post.id + "\r\n")
            redundant_file.close()
            printPost(post)
            printedPosts = True

    if printedPosts:
        print("\t</body>\n</html>")

def printPost(post):
    #TODO: Might have to do some character replacement for HTML escaping
    print("\t\t<div>")
    print("\t\t\t<a href=\"http://redd.it/" + post.id + "\">" + post.title + "</a>")
    print("\t\t\t<a href=\"" + post.url + "\">Link to the product</a>")
    if "http" in post.thumbnail:
        print("\t\t\t<img src=\"" + post.thumbnail + "\" alt = \"Thumbnail image from the post\">")
    print("\t\t</div>")

bapcs_posts()
