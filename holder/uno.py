from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
  
def filterer(givenn):
    newlist = []
    for i in givenn:
        if i not in newlist:
            newlist.append(i)
    return newlist


def TitledName(Links):
    ResultList = []
    for link in Links:
        html = urlopen(f"{link}")
        bsObj = BeautifulSoup(html, "html.parser")
        h1title = bsObj.find("h1").get_text()
        h1title = re.sub("\s\s+", " ", h1title)
        ResultList.append([f"{link}",f"{h1title}"])
    return ResultList


#Obtener todos los articulos, pero en su reespectiva categoria.
def GetLinksOfEditorial():
    html = urlopen("https://hoy.com.do/opiniones/")
    ResultingLinks = []
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find_all("div", {"class": re.compile("(.*article-content)(.*)")}):
        Afinder = link.find_all("a")
        for a in Afinder:
            poiner = a.attrs['href']
            if poiner not in ResultingLinks:
                ResultingLinks.append(poiner)
    
    return TitledName(ResultingLinks)

print(GetLinksOfEditorial())
#print(len(SecondLinkHold))
#print(len(terminated))
 