import urllib2

intermediateFile = open('intermediateList.txt', 'w')
outputFile = open("whitelist.txt", 'w')

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
