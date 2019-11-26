from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
  
  
#Para llamar a la pagina principal, provisto a ser eliminada
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

#Obtener todos los articulos anidados en la lista de articulos proveida
def GetLinksRecursive(LinksInFirstResult):
    
    newHtml = ""
    FinalLinksContainer = []
    for actualLink in LinksInFirstResult:
        try:
            newHtml = urlopen(f"{actualLink}")  
            bsObjsnew = BeautifulSoup(newHtml, "html.parser")
            
        except:
          continue
        
        for linkin in bsObjsnew.find_all("aside", {"id": "masrecientes"}):
             
             AFinders = linkin.findAll("a")
             try:
               for a in AFinders:
                 hond = a.attrs['href']
                 if (hond not in FinalLinksContainer) and (hond not in LinksInFirstResult):
                       FinalLinksContainer.append(hond)
                 
             except:
               continue
          
    return FinalLinksContainer

#Obtener el titulo de los resultados
def TitledName(Links):
    ResultList = []
    for link in Links:
        html = urlopen(f"{link}")
        bsObj = BeautifulSoup(html, "html.parser")
        h1title = bsObj.find("h1").get_text()
        ResultList.append([f"{link}",f"{h1title}"])
    return ResultList


#Obtener todos los articulos, pero en su reespectiva categoria.
def GetLinksOfOpiniones():
    html = urlopen("https://hoy.com.do/opiniones/")
    ResultingLinks = []
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find_all("div", {"class": re.compile("(.*article-content)(.*)")}):
        Afinder = link.find_all("a")
        for a in Afinder:
            poiner = a.attrs['href']
            if poiner not in ResultingLinks:
                ResultingLinks.append(poiner)
    finalresult = TitledName(ResultingLinks)
    return finalresult


#print(GetLinksOfEditorial())
#firstresult = getAllHoyLinksMain()
#secondresult = GetLinksRecursive(firstresult)
#print(len(firstresult), "primero no recursivo")
#print(len(secondresult), "segundo recursivo")
#print(len(SecondLinkHold))
#print(firstresult)
 