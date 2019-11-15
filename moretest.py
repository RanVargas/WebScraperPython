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

  
receiveds = getAllHoyLinksMain()
for itemm in receiveds:
    print(itemm)
 
#print(len(SecondLinkHold))
#print(len(terminated))
 