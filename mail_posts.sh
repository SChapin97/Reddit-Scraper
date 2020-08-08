#!/bin/bash

## buildapcsales
python3 buildapcsales.py > mailfile

if [[ -f "mailfile" && -s "mailfile" ]]; then
   mail -a "Content-type: text/html" -r "sender@example.com" -s "buildapcsales alert" "recipient@example.com" < <(cat template.html mailfile)
fi

rm mailfile


## laptopdeals
python3 laptopdeals.py > mailfile

if [[ -f "mailfile" && -s "mailfile" ]]; then
   mail -a "Content-type: text/html" -r "sender@example.com.com" -s "laptopdeals alert" "recipient@example.com" < <(cat template.html mailfile)
fi

rm mailfile

#cleaning up previous_posts if we have more than 30 posts
count=`wc -l previous_posts | cut -f1 -d " "`
if [ $count -gt 30 ]; then
   #Deleting the contents of previous_posts
   :> previous_posts

   #Calling the scripts again so we don't get duplicate emails
   python3 buildapcsales.py > /dev/null
   python3 laptopdeals.py > /dev/null
fi





