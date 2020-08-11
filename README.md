# Requirements:
   python3 and pip3 (`sudo apt install python3-pip`)
   
   praw (`python3 -m pip install praw`)
   
   a text editor (needed to configure personal settings)

   (Optional -- for mailing the output):
   
   A (linux mail server) to host the script/send the emails using `mail_posts.sh`

# Usage:
Fill in your details in praw.ini (client_id, client_secret for a reddit script; username and password for a reddit account)

Run one of the following python files:

## buildapcsales.py :: Fully Working
Usage: cat template.html > output.html; python3 buildapcsales.py > output.html

Used to output the newest posts from /r/buildapcsales, then print any posts that contain the strings in `searchItems` to STDOUT.
Post redundancy is built into this file (any posts that are printed will have their IDs stored in the `previous_posts` file and will not be printed again).

Personally, the script is not very useful on its own, but I have a cronjob that will run the script every 5 minutes and email me (using `postfix`) if an item has been found.
Use `mail_posts.sh` in a cronjob to automate this process (if you have a dedicated server you can put this script on)
Cronjob (`crontab -e`) is as such: `*/5 * * * * (cd <directory installed> ; /bin/bash mail_posts.sh)`

## top_posts.py :: In Development
Used to output the top 5 posts from each subreddit in each multireddit for your reddit account.

The goal for this script is to send me daily updates about the various subreddits I care about (packaged into different multireddits based on subject).
Similarly to buildapcsales.py, I will likely also have the output emailed to me on a daily bases (by using a cronjob) once complete.

## laptopdeals.py :: Fully Working
Usage: cat template.html > output.html; python3 buildapcsales.py > output.html

Basically the same thing as buildapcsales.py, but with the /r/laptopdeals subreddit.
Also included in `mail_posts.sh` to automate the process of sending the output via email.
