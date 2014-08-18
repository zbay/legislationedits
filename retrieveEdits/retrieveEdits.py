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
  if len(line) > 1: #making sure an empty line isn't fed in to the url
    url =  "http://en.wikipedia.org/w/api.php?action=query&rvdiffto=prev&prop=revisions&rvprop=timestamp|user&format=json&titles=" + line + "&redirects"
    jsonurl = urllib2.urlopen(url)
    revision = json.loads(jsonurl.read())
    query = revision["query"]
    pages = query["pages"]
    page = next (iter (pages.values()))
    revisions = page["revisions"]
    step = revisions[0]
    timestamp = step['timestamp']
    user = step['user']
    diff = step['diff']
    fromID = str(diff['from'])
    toID = str(diff['to'])
  
 # 2013-02-05T09:37:29Z
  
  time1 = time.strptime(timestamp, "%Y" + "-" + "%m" + "-" + "%d" + "T" + "%H" + ":" + "%M" + ":" "%S" + "Z")
  revisionTime = time.mktime(time1)
  time2 = time.strftime("%H" + ":" + "%M" + " UTC", time1)
  line = line.replace ("_", " ")
  
if revisionTime > startTime:
    #if user[:8] == "143.231.": #House IP address. A regular expression version would be better but I'm lazy
     # output = "ANONYMOUS US HOUSE EDIT: Article /" + line + "\""
    #elif user[:8] == "156.33.": #Senate IP address. Regular expression ideal, again
     # output = "ANONYMOUS SENATE EDIT: Article /" + line + "\""
    #else:
    output = "Article \"" + line + "\" edited by " + user
     
    line = line.replace (" ", "_")
    edit = output[:116] + " http://en.wikipedia.org/w/index.php?title=" + line + "&diff=" + toID + "&oldid=" + fromID
    twitter.update_status(status=edit)
