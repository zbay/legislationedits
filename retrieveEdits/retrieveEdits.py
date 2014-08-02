#break into several files

import urllib2
import json
import time
from twython import Twython
from creds import *

twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

st = time.time()
startTime = st - 600.0

intermediateFile = open('intermediateList.txt', 'w')
intermediateFile.truncate()
outputFile = open("whitelist.txt", 'w')
outputFile.truncate()

inputFile = urllib2.urlopen('http://en.wikipedia.org/w/api.php?action=query&cmlimit=500&list=categorymembers&cmtitle=Category:United_States_proposed_federal_legislation')

intermediateFile.writelines(inputFile.read())

intermediateFile.close()

intermediateFile = open('intermediateList.txt', 'r')

for line in intermediateFile:
   start = line.find("title=&quot;")
   end = line.rfind("&quot; /&gt;</span>")
  
   if start != -1 and line.find("Zlwilliams1") == -1 and line.find("Category:U") == -1:
         line2 = line[start+12:end]
         line2 = line2.replace("&quot;", "\"")
         line2 = line2.replace("&apos;", "'")
         line2 = line2.replace("&amp;", "&")
         line2 = line2.replace("&lt;", "<")
         line2 = line2.replace("&gt;", ">")
         line2 = line2.replace("&laquo;", "<<")
         line2 = line2.replace("&raquo;", ">>")
         line2 = line2.replace("&#039;", "'")
         line2 = line2.replace("&#8220;", "\"")
         line2 = line2.replace("&#8221;", "\"")
         line2 = line2.replace("&#8216;", "\'")
         line2 = line2.replace("&#8217;", "\'")
         line2 = line2.replace("&#9632;", "")
         line2 = line2.replace("&#8226;", "-")
         line2 = line2.replace("&quot;", "\"")
         outputFile.write(line2 + "\n")
outputFile.close()
outputFile = open("whitelist.txt", 'r')

for line in outputFile:
  line = line.replace (" ", "_")
  line = line.replace("\n", "")
  url = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=timestamp|user&format=json&titles=" + line
  jsonurl = urllib2.urlopen(url)
  revision = json.loads(jsonurl.read())
  query = revision["query"]
  pages = query["pages"]
  page = next (iter (pages.values()))
  revisions = page["revisions"]
  step = revisions[0]
  timestamp = step['timestamp']
  user = step['user']
  
 # 2013-02-05T09:37:29Z
  
  time1 = time.strptime(timestamp, "%Y" + "-" + "%m" + "-" + "%d" + "T" + "%H" + ":" + "%M" + ":" "%S" + "Z")
  revisionTime = time.mktime(time1)
  time2 = time.strftime("%H" + ":" + "%M" + " UTC", time1)
  line = line.replace ("_", " ")
  
  if revisionTime > startTime:
   output = "Article \"" + line + "\" edited by " + user
   line = line.replace (" ", "_")
   edit = output[:116] + " en.wikipedia.org/wiki/" + line
   twitter.update_status(status=edit)
