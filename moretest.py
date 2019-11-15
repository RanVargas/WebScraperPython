from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
 
def filterer(givenn):
    newlist = []
    for i in givenn:
        if i not in newlist:
            newlist.append(i)
    return newlist

def getAllHoyLinksMain():
    html = urlopen("https://hoy.com.do/")
    bsObj = BeautifulSoup(html, "html.parser")
    SecondLinkHold = []

    for section in bsObj.find_all("section", {"class": re.compile("(.*section)(.*)")}):
        
        #print(section.findAll("a"))
        holder = section.findAll("a")
            
        for a in holder:
            #SecondLinkHold.extend(a.attrs["href"])
            #hong+= a.attrs["href"]
            #print(a.attrs['href'])
            SecondLinkHold.append(a.attrs['href'])
    
    return filterer(SecondLinkHold)

def GetLinksRecursive(LinksInFirstResult, limiterr):
    limiterr += 1
    newHtml = ""
    FinalLinksContainer = []
    for actualLink in LinksInFirstResult:
        try:
            newHtml = urlopen(f"{actualLink}")  
            bsObjsnew = BeautifulSoup(newHtml, "html.parser")
            
        except:
          continue
        
        for linkin in bsObjsnew.find_all("aside", {"id": "masrecientes"}):
             linkinAs = linkin.findall("a")
             for a in linkinAs:
                 if a.attrs['href'] not in LinksInFirstResult:
                       FinalLinksContainer.append(a.attrs['href'])
    if limiterr == 1000:
          return FinalLinksContainer
      
    return FinalLinksContainer


hipo = 0
firstresult = getAllHoyLinksMain()
GetLinksRecursive(firstresult, hipo)
#print(len(SecondLinkHold))
#print(firstresult)
 