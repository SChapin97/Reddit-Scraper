# Requirements:
   python3 and pip3 (`sudo apt install python3-pip`)
   
   praw (`python3 -m pip install praw`)
   
   a text editor (needed to configure personal settings)

   (Optional -- for mailing the output):
   
   A (linux mail server) to host the script/send the emails using `mail_subreddit_posts.sh`

# Usage:
Fill in your details in praw.ini (client_id, client_secret for a reddit script; username and password for a reddit account)

Run one of the following python files:

## subreddit_watcher.py :: Fully Working
Usage: `cat template.html > output.html; python3 subreddit_watcher.py `insert subreddit name` > output.html`
Currently supported subreddit names: `buildapcsales` `laptopdeals` `gamecube` `vive`
Note that only one subreddit name is supported at this time, but the script can be executed multiple times with different names.

Used to find posts that match a search item for one of many subreddits (which can be configured in the `subreddit_watcher.py` script itself). If found, it will output part of an html file with formatted links to the found posts. When appended to the template file `template.html`, it can be viewed like a normal webpage, or emailed using `mail_subreddit_posts.sh` (assuming `postfix` is setup on the linux machine the script is run on).

I personally use `mail_subreddit_posts.sh` in a cronjob on a linux server that I have postfix setup to handle outgoing mail to alert me of any posts that are found after searching every 5 minutes.
Cronjob (`crontab -e`) is as such: `*/5 * * * * (cd <directory installed>; /bin/bash mail_subreddit_posts.sh)`

## multireddit_newsfeed.py :: Mostly complete
Usage: `cat template.html > output.html; python3 multireddit_newsfeed.py `insert multireddit name`>> output.html`
Used to output the top 5 posts (or less if less than 5 posts were created that day) from each subreddit in each multireddit for your reddit account.
Each multireddit will be sent in a different email.

Once complete, the script will output part of an html file with formatted links to each post, thumbnail to a linked image if present, and an outgoing link if the post is not a self post. When appended to the template file `template.html`, it can be viewed like a normal webpage, or emailed using `mail_newsfeed_posts.sh` (assuming `postfix` is setup on the linux machine the script is run on).
Cronjob (`crontab -e`) is as such: `0 11 * * * (cd <directory installed>; /bin/bash mail_newsfeed_posts.sh)`. Note that this runs at 11 AM (according to the server). Use the site crontab.guru to easily change this if needed.
