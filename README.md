legislationedits
================

This program tweets out edits to bills going through the U.S. Congress. Here are some instructions to get you started.

To use  this Twitter bot:

* Set up a Python IDE.

* In command line: git clone https://github.com/zbay/legislationedits.git

* Log in and make a Twitter app called "legislation-edits" or something similar at https://apps.twitter.com/. Set the Consumer Key, Consumer Secret, Access token, and Access token secret. Add the credentials to creds.py. Give a Twitter account permission for your app to read+write to it.

* Run updateWhitelist114.py to update the list of Wikipedia articles to monitor, based on editing activty.

* Edit a bill article on Wikipedia and see the bot work. Run retrieveEdits.py periodically to tweet the most recent edits.

* retrieveEdits.py currently checks for edits in the last ten minutes (600 seconds). To change this interval, edit the variable 'frequency' in retrieveEdits.py to something other than 600.0.

* Run Python file updateWhitelist113.py periodically to update the list of Wikipedia articles to check, from this page: (http://en.wikipedia.org/wiki/List_of_bills_in_the_114th_United_States_Congress) and this page: (http://en.wikipedia.org/wiki/List_of_Acts_of_the_114th_United_States_Congress). For future sessions of Congress, change the variable billPage to 'http://en.wikipedia.org/wiki/List_of_bills_in_the_115th_United_States_Congress' and so forth. 

* A very small number of bills on the 113th Congress's Wikipedia page fall through the cracks. 2/347 defied my formula. If the article doesn't link to the first word in a table cell, for example, it won't register. Also, if it lacks any identifying words like "Act", "Resolution", "To_", "Amendments", "Authorization", "Public_Law" or adverbs. If my automatic trawling for articles fails, add the article suffix to manualWhitelist114.txt so that updateWhitelist114.py can add it to the regular whitelist.
 
* updateWhitelist.py (in the 113 folder) works differently, getting links from the the category "Category:United_States_proposed_federal_legislation". Feel free to try the code with other Wikipedia categories!

I suck at web development. If somebody can explain the nuances of Heroku Scheduler to me, I could find a way to get this to work in the cloud.

Update: As of 8/12/2014, this project exists at https://twitter.com/wikibills. Give it a follow!

-zbay
