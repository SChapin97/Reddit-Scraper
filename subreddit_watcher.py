#!/usr/bin/python3

import praw
import time
import os
import sys
import html

REDDIT_WRAPPER = praw.Reddit("bot1", user_agent="Post Scraper")
POST_REDUNDANCY_FILE_PATH = "previous_posts"

def main():
    if "buildapcsales" in str(sys.argv):
        buildapcsales()
    if "homelabsales" in str(sys.argv):
        homelabsales()

##Subreddit-specific functions
def buildapcsales():
    search_items = ["[meta]", "[other]", "UPS", "interrupt", "hdd", "hard drive"]
    ignore_items = ["newegg shuffle", "newegg souffl", "prebuilt"]

    subreddit = REDDIT_WRAPPER.subreddit("buildapcsales")
    iterate_posts(subreddit, search_items, ignore_items)



def homelabsales():
    search_items = ["MN]", "camera", "security"]
    ignore_items = ["[W"] #Subreddit title-style for wanted postings

    subreddit = REDDIT_WRAPPER.subreddit("homelabsales")
    iterate_posts(subreddit, search_items, ignore_items)


##Generic functions
#Generic function to go through each posts on a subreddit's new posts list
def iterate_posts(subreddit, search_items, ignore_items):
    #Making sure that previous_posts exists
    if not os.path.exists(POST_REDUNDANCY_FILE_PATH):
        f = open(POST_REDUNDANCY_FILE_PATH, "w")
        f.close()

    printed_posts = False #Used so we can output the end of the html doc

    for post in subreddit.new():
        printable = False
        for item in search_items:
            if item.upper() in post.title.upper():
                for ignore in ignore_items:
                    if ignore.upper() in post.title.upper():
                        break
                else: #This statement is redundant, but it makes this slightly more readable
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
            redundant_file.write(post.id + "\n")
            redundant_file.close()
            printPost(post)
            printed_posts = True


#Generic print post information function
def printPost(post):
    #If a url starts with /r/, it is a x-post and needs to have reddit.com prepended to it.
    url = post.url
    if url.startswith('/r/'):
        url = 'https://reddit.com' + url

    print(post.title + "\n", "<https://redd.it/" + post.id + ">")
    print("Link to the product: <" + url + ">\n<end_item>\n")

main()
