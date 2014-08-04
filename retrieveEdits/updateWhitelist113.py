import urllib2

intermediateFile = open('intermediateList113.txt', 'w')
intermediateFile.truncate()
outputFile = open("whitelist113.txt", 'w')
outputFile.truncate()

#CHANGE THIS LINE FOR FUTURE SESSIONS OF CONGRESS
billPage = 'http://en.wikipedia.org/wiki/List_of_bills_in_the_113th_United_States_Congress'

inputFile = urllib2.urlopen(billPage)

intermediateFile.writelines(inputFile.read())

intermediateFile.close()

intermediateFile = open('intermediateList113.txt', 'r')

for line in intermediateFile:
   start = line.find("<td><a href=\"/wiki/")
   end = line.find(" title=")
   wiki = line[start:end-1]
   wikiPage = wiki[19:]
   isAct = False
   
   if wikiPage.find("Act_") > -1  or wikiPage.find("_act") > -1 or wikiPage.find("act_") > -1 or wikiPage.find("_Act") > -1 or wikiPage.find("bill") > -1 or wikiPage.find("Amendments") > -1 or wikiPage.find("Resolution") > -1 or wikiPage.find("Authorization") > -1 or wikiPage.find("To_") == 0 or wikiPage.find("United_States_federal_budget") > -1 :
    isAct = True
    
    #adverb test
   if not isAct:
     firstSpace = wikiPage.find("_")
     firstWord = wikiPage[0:firstSpace]
     if len(firstWord) > 3:
       if firstWord[len(firstWord)-3:] == "ing":
        isAct = True
  
   if isAct:
       outputFile.write(wikiPage + "\n")
outputFile.close()
