#!/bin/bash

#Display date in formatted like "January 1 1970"
date=`date "+%A %b %d"`

#3DPrinting multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py 3dprinting >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily 3DPrinting Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/3DPrinting.html


#Deals multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py deals >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily Deals Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/deals.html


#Dev multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py dev >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily Dev Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/dev.html


#Memes multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py memes >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily Memes Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/memes.html


#Mindless multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py mindless >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily Mindless Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/mindless.html


#Misc multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py misc >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily Misc Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/misc.html


#News multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py news >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily News Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/news.html


#Pictures multireddit
cat template.html > output.html
python3 multireddit_newsfeed.py pictures >> output.html
#mail -a "Content-type: text/html" -r "schapin@samuelchapin.com" -s "Daily Pictures Multireddit Feed - $date" "reconless@gmail.com" < output.html
mv output.html .output/pictures.html
