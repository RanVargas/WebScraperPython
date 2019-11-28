from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import asyncio

#Categorias a elegir CategoryOptions = ["Republica", "Opinion", "Deportes", "Mundiales", "Entretenimiento", "Vida", "Economia"]

def GetRepublicaLinks():
    htmllink = urlopen('https://listindiario.com/la-republica')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    ResultS = []
    for link in bsObj.find_all("a", href=re.compile("^(/la-republica/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                ResultS.append(WholeLink)
    return ResultS
    
    
def GetOpinionLinks():
    ResultS = []
    htmllink = urlopen('https://listindiario.com/opinion')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/editorial/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    return ResultS
    
async def GetDeporteLinks():
    ResultS = []
    htmllink = urlopen('https://listindiario.com/el-deporte')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/el-deporte/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                await ResultS.append(WholeLink)
    return ResultS    

def GetMundialesLinks():
    ResultS = []
    htmllink = urlopen('https://listindiario.com/las-mundiales')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/las-mundiales/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    return ResultS

def GetEntretenimientoLinks():
    ResultS = []
    htmllink = urlopen('https://listindiario.com/entretenimiento')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/entretenimiento/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    return ResultS

def GetVidaLinks():
    ResultS = []
    htmllink = urlopen('https://listindiario.com/la-vida')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/la-vida/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    return ResultS

def GetEconomiaLinks():
    ResultS = []
    htmllink = urlopen('https://listindiario.com/economia')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/economia/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    return ResultS

def Cleaner(Links):
    ResultList = []
    for link in Links:
        html = urlopen(f"{link}")
        bsObj = BeautifulSoup(html, "html.parser")
        h1title = bsObj.find("h1").get_text()
        h1title = re.sub("\s\s+", " ", h1title)
        ResultList.append([f"{link}",f"{h1title}"])
    return ResultList

def GetListinDiarioLinks(Election):
    if Election == 0:
          Republica = GetRepublicaLinks()
          result = Cleaner(Republica)
          return result
    
    elif Election == 1:
        Opinion = GetOpinionLinks()
        result = Cleaner(Opinion)
        return result
    
    elif Election == 2:
        Deportes = GetDeporteLinks()
        result = Cleaner(Deportes)
        taks = asyncio.create_task(Deportes)
        return taks
    
    elif Election == 3:
        Mundiales = GetMundialesLinks()
        result = Cleaner(Mundiales)
        return result
    
    elif Election == 4:
        Entretenimiento = GetEntretenimientoLinks()
        result = Cleaner(Entretenimiento)
        return result
    
    elif Election == 5:
        Vida = GetVidaLinks()
        result = Cleaner(Vida)
        return result
    
    elif Election == 6:
        Economia = GetEconomiaLinks()
        result = Cleaner(Economia)
        return result
    
    
    
    


print(GetListinDiarioLinks(2))