legislationedits
================

This program tweets out edits to proposed legislation going through the U.S. Congress. Here are the instructions to get you started.

To run this Twitter bot you will need:

A Python runtime environment
In command line: git clone https://github.com/zbay/anon.git
Login and make a Twitter app called "legislation-edits" or something similar at https://apps.twitter.com/. Set the Consumer Key, Consumer Secret, Access token, and Access token secret. Add the code to creds.py (under accounts). Give a Twitter account permission for your app to read+write to it.


Edit a proposed piece of U.S. legislation on Wikipedia and see the bot work.
Run trackEdits.py periodically to A. update the list of Wikipedia articles to check for and B. tweet the most recent edits. 
The app currently checks for edits in the last ten minutes (600 seconds). Thus, you will need to run trackEdits.py that frequently.

My problem: I don't have the time, effort, or free computing power necessary to run this script 24/7. Hopefully somebody else can bring this to fruition.
