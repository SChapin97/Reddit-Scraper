#!/bin/bash

## Subreddit: r/buildapcsales
python3 subreddit_watcher.py buildapcsales > mailfile

if [[ -f "mailfile" && -s "mailfile" ]]; then
   mail -a "Content-type: text/html" -r "sender@example.com" -s "buildapcsales subreddit alert" "recipient@example.com" < <(cat template.html mailfile)
fi

rm mailfile


## Subreddit: r/laptopdeals
python3 subreddit_watcher.py laptopdeals > mailfile

if [[ -f "mailfile" && -s "mailfile" ]]; then
   mail -a "Content-type: text/html" -r "sender@example.com" -s "laptopdeals subreddit alert" "recipient@example.com" < <(cat template.html mailfile)
fi

rm mailfile


## Subreddit: r/gamecube
python3 subreddit_watcher.py gamecube > mailfile

if [[ -f "mailfile" && -s "mailfile" ]]; then
   mail -a "Content-type: text/html" -r "sender@example.com" -s "gamecube subreddit alert" "recipient@example.com" < <(cat template.html mailfile)
fi

rm mailfile


## Subreddit: r/vive
python3 subreddit_watcher.py vive > mailfile

if [[ -f "mailfile" && -s "mailfile" ]]; then
   mail -a "Content-type: text/html" -r "sender@example.com" -s "vive subreddit alert" "recipient@example.com" < <(cat template.html mailfile)
fi

rm mailfile



#cleaning up previous_posts if we have more than 30 posts
count=`wc -l previous_posts | cut -f1 -d " "`
if [ $count -gt 30 ]; then
   #Deleting the contents of previous_posts
   :> previous_posts

   #Calling the script again so we don't get duplicate emails
   python3 subreddit_watcher.py buildapcsales laptopdeals gamecube vive > /dev/null
fi
