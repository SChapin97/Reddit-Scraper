import praw
import time
import re
import os

reddit = praw.Reddit("bot1", user_agent="Post Scraper")
searchItems = ["print", "lamp", "ikea"]
post_redundancy_file_path = "previous_posts"

def bapcs_posts():
    bapcs = reddit.subreddit("buildapcsales")

    #Making sure that previous_posts exists
    if not os.path.exists(post_redundancy_file_path):
        f = open(post_redundancy_file_path, "w")
        f.close()

    for post in bapcs.new(): #, limit=30):
        printable = False
        for item in searchItems:
            if item.upper() in post.title.upper():
                printable = True
                break

        if not printable:
            continue

        m = re.search("(?P<type>\\[[^\\[\\]]+\\])\\s*(?P<item>[^$]+)(?P<price>\\$.+)", post.title)
        if m:
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

def printPost(post):
    print(post.title, "; Upvotes:", post.score) #, post.created_utc)
    print("Reddit link: http://redd.it/" + post.id)
    print("Post link:", post.url)

bapcs_posts()
