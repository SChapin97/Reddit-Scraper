import praw
import time
import re
import os.path

reddit = praw.Reddit("bot1", user_agent="Post Scraper")
searchItems = ["CPU"]
post_redundancy_file_path = "previous_posts"

def bapcs_posts():
    bapcs = reddit.subreddit("buildapcsales")

    #Making sure that previous_posts exists
    if not os.path.exists(post_redundancy_file_path):
        f = open(post_redundancy_file_path, "w")
        f.close()

    for post in bapcs.new(): #, limit=30):
        m = re.search("(?P<type>\\[[^\\[\\]]+\\])\\s*(?P<item>[^$]+)(?P<price>\\$.+)", post.title)
        if m:
            printPost(post, m)


def printPost(post, m):
    #Looking to see if the ID has already been found by the script
    redundant_file = open(post_redundancy_file_path, "r")
    found = False

    for line in redundant_file.readlines():
        if post.id in line:
            found = True

    #If the post ID has not been found, then we want to print the post information
    if not found:
        redundant_file.close()
        redundant_file = open(post_redundancy_file_path, "a")

        #Only want to print out items that are specified in the searchItems array.
        for item in searchItems:
            if item.upper() in post.title.upper():
                minutesSince = (time.time() - post.created_utc) // 60

                #Adding to the redundant post file
                redundant_file.write(post.id + "\r\n")

                print(post.title, "; Upvotes:", post.score) #, post.created_utc)
                print("Reddit link: https://www.reddit.com/r/buildapcsales/" + post.id)
                print("Post link:", post.url)
#                print("Type:", m.group("type"), "; Item:", m.group("item"), "; Price:", m.group("price"))

    redundant_file.close()

bapcs_posts()
