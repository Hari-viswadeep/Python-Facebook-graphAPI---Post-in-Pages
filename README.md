# Python-Facebook-graphAPI---Post-in-Pages
Python program which collects posts in public Facebook pages using graph API

Before running the script, make sure following things are ready

1) Create an App in Facebook using developer account.
2) Get APP_SECRET_ID & APP_ID.
3) List out pages to be crawled.
4) Make sure bs4 is installed.

NOTE:- Only public pages can be accessed with the script. And number of posts to be crawled is limited to 100 (FB sets this limit)

once the aboove mentioned things are ready run the script facebook_page_content.py

--> results are stored in a pickle file (fb_page_contents.p) which is in readable format.
