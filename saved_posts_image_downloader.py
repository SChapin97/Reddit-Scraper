import praw
import requests
import re
import os

REDDIT_WRAPPER = praw.Reddit("bot1", user_agent="Post Scraper")
POST_REDUNDANCY_FILE_PATH = "redundant_saved__posts_list"
FILE_PATH = '/home/<user>/Pictures'

def main():
    previous_saved_posts = get_redundant_post_id_list()
    saved_posts = REDDIT_WRAPPER.user.me().saved()
    for post in saved_posts:
        try:
            if post.url:
                if not post.id in previous_saved_posts:
                    print(post.id + "is a new file, processing...")
                    add_post_to_list(post.id)
                    download_image(post.url)
        except (AttributeError):
            #Saved comments will throw errors, we want to silently fail these.
            continue

def download_image(url):
    image = requests.get(url).content
    image_found = re.search(r"\w+\.\w+$", url)
    if image_found:
        image_name = image_found.group()

        image_fullpath = os.path.join(FILE_PATH, image_name)
        image_file = open(image_fullpath, "wb")
        image_file.write(image)
        image_file.close()

def get_redundant_post_id_list():
    post_list = []
    with open(POST_REDUNDANCY_FILE_PATH, "r") as redundant_file:
        for line in redundant_file.readlines():
            post_list.append(line.strip())
    return post_list

def add_post_to_list(id):
    with open(POST_REDUNDANCY_FILE_PATH, "a") as redundant_file:
        #Overwriting the redundant file with the first post url
        redundant_file.write(id + "\n")

main()
