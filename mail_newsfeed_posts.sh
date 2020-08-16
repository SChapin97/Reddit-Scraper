#!/bin/bash

cat template.html > output.html
python3 multireddit_newsfeed.py >> output.html
mail -a ail -a "Content-type: text/html" -r "sender@example.com" -s "Daily Reddit Newsfeed" "recipient@example.com" < output.html

rm output.html