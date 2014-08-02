legislationedits
================

This program tweets out edits to proposed legislation going through the U.S. Congress. Here are the instructions to get you started.

To use  this Twitter bot:

* Set up a Python runtime environment.

* In command line: git clone https://github.com/zbay/anon.git

* Log in and make a Twitter app called "legislation-edits" or something similar at https://apps.twitter.com/. Set the Consumer Key, Consumer Secret, Access token, and Access token secret. Add the credentials to creds.py. Give a Twitter account permission for your app to read+write to it.

* Edit a proposed piece of U.S. legislation on Wikipedia and see the bot work.
Run trackEdits.py periodically to A. update the list of Wikipedia articles to check for and B. tweet the most recent edits.

* trackEdits.py currently checks for edits in the last ten minutes (600 seconds). To change this interval, edit the variable 'frequency' in retrieveEdits.py to something other than 600.0.

* Run updateWhitelist.py periodically to update the list of Wikipedia articles to check, under the category "Category:United_States_proposed_federal_legislation". Feel free to try this code with other Wikipedia categories!

I suck at web development. If somebody can explain the nuances of Heroku Scheduler to me, I'll find a way to get this to work in the cloud.

-zbay
