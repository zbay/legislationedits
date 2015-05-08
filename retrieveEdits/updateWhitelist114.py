import urllib2

intermediateFile = open('intermediateList114.txt', 'w')
outputFile = open("whitelist114.txt", 'w')

#CHANGE THIS LINE FOR FUTURE SESSIONS OF CONGRESS
billPage = 'http://en.wikipedia.org/wiki/List_of_bills_in_the_114th_United_States_Congress'
actPage = 'http://en.wikipedia.org/wiki/List_of_Acts_of_the_114th_United_States_Congress'

inputFile = urllib2.urlopen(billPage)
inputFile2 = urllib2.urlopen(actPage)

intermediateFile.writelines(inputFile.read())
intermediateFile.writelines(inputFile2.read())

intermediateFile.close()

intermediateFile = open('intermediateList114.txt', 'r')

checkForDuplicates = []

for line in intermediateFile:
   start = line.find("<td><a href=\"/wiki/")
   end = line.find(" title=")
   wiki = line[start:end-1]
   wikiPage = wiki[19:]
   isAct = False
   if start == -1:
      start = line.find("<td nowrap=\"nowrap\"><a href=\"/wiki/")
      wikiPage = wiki[35:]
      wiki = line[start:end-1]
      
   if start > -1:
    #how to filter out the good Wikipedia links from the bad
     if wikiPage.find("Act_") > -1  or wikiPage.find("_act") > -1 or wikiPage.find("act_") > -1 or wikiPage.find("_Act") > -1 or wikiPage.find("bill") > -1 or wikiPage.find("Bill_to") > -1 or wikiPage.find("bill_to") > -1 or wikiPage.find("Amendments") > -1 or wikiPage.find("Resolution") > -1 or wikiPage.find("Authorization") > -1 or wikiPage.find("authorization") >-1 or wikiPage.find("To_") == 0 or wikiPage.find("Public_Law") > -1 or wikiPage.find("United_States_federal_budget") > -1 or wikiPage.find("_Ban_") > -1:
      if len(wikiPage) > 2:
        isAct = True
    
    #adverb test
     if not isAct:
       firstSpace = wikiPage.find("_")
       firstWord = wikiPage[0:firstSpace]
       if len(firstWord) > 3:
         if firstWord[len(firstWord)-3:] == "ing":
          isAct = True
  
     if isAct:
         if wikiPage not in checkForDuplicates:
               outputFile.write(wikiPage + "\n")
               checkForDuplicates.append(wikiPage)

      inputFile3 = open("manualWhitelist114.txt", "r")
      for line in inputFile3:
        if wikiPage not in checkForDuplicates:
            outputFile.write(line + "\n")
            checkForDuplicates.append(wikiPage)
