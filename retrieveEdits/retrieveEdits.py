import urllib2
import json
import time
from twython import Twython
from creds import *

twitter = Twython(APP_KEY, APP_SECRET,
                  FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)

#NUMBER OF SECONDS BETWEEN CHECKS
frequency = 600.0

st = time.time()
startTime = st - frequency

outputFile = open("whitelist113.txt", 'r')

for line in outputFile:
  line = line.replace (" ", "_")
  line = line.replace("\n", "")
  url = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=timestamp|user&format=json&titles=" + line + "&redirects"
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
