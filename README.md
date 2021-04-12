# Requirements:
   python3 and pip3 (`sudo apt install python3-pip`)
   
   praw (`python3 -m pip install praw`)
   
   a text editor (needed to configure personal settings)

# Usage:
Fill in your details in praw.ini (client_id, client_secret for a reddit script; username and password for a reddit account)

Run one of the following python files:

## subreddit_watcher.py :: Fully Working
Usage: `python3 subreddit_watcher.py `insert subreddit name(s)``
Currently supported subreddit names: `buildapcsales` `buildapcsales`
The script now supports multiple names per run. I will shortly be working on a variant of the script that will accept user input in JSON format so that one does not have to edit the script when they want to change what is searched for.

Used to find posts that match a search item for one of many subreddits (which can be configured in the `subreddit_watcher.py` script itself). If found, it will output to STDOUT with formatted links to the found posts.

Instead of mailing the output if a post is found, I have integrated it into a Discord bot to alert me on a dedicated server for these types of posts.
Since the output is to STDOUT, this could be used in many other types of delivery systems (rather than handling HTML files as previously done).

## multireddit_newsfeed.py :: Fully Working
Usage: `cat template.html > output.html; python3 multireddit_newsfeed.py `insert multireddit name`>> output.html`
Used to output the top 5 posts (or less if less than 5 posts were created that day) from each subreddit in each multireddit for your reddit account.
Each multireddit will be sent in a different email.

Once complete, the script will output part of an html file with formatted links to each post, thumbnail to a linked image if present, and an outgoing link if the post is not a self post. When appended to the template file `template.html`, it can be viewed like a normal webpage.
The way I have this setup is by adding the output of these daily scripts to my website via the `mail_newsfeed_posts.sh` script.
Cronjob (`crontab -e`) is as such: `0 11 * * * (cd <directory installed>; /bin/bash mail_newsfeed_posts.sh)`. Note that this runs at 11 AM (according to the server). Use the site crontab.guru to easily change this if needed.
