#!/bin/bash

#Display date in formatted like "January 1 1970"
date=`date "+%A %b %d"`

#News multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py news >> output.html
mail -a "Content-type: text/html" -r "sender@example.com" -s "Daily News Multireddit Feed - $date" "recipient@example.com" < output.html

rm output.html

#Dev multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py dev >> output.html
mail -a "Content-type: text/html" -r "sender@example.com" -s "Daily Dev Multireddit Feed - $date" "recipient@example.com" < output.html

rm output.html

#Memes multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py memes >> output.html
mail -a "Content-type: text/html" -r "sender@example.com" -s "Daily Memes Multireddit Feed - $date" "recipient@example.com" < output.html

rm output.html
