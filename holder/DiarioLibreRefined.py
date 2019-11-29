from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen

#CategoryOptions = ["Actualidad", "Economia", "Revista", "Deportes", "Estilos", "Opinion"]

def EconomiaCleaner(Links):
    ResultList = []
    for link in Links:
        html = urlopen(f"{link}")
        bsObj = BeautifulSoup(html, "html.parser")
        try:
          h1title = bsObj.find("span", {"class": "priority-content"}).get_text()
          h1title = re.sub("\s\s+", " ", h1title)
          if h1title not in ResultList:
                ResultList.append([f"{link}",f"{h1title}"])
        except Exception:
          continue
    return ResultList

def EconomyProof():
    html = urlopen("https://www.diariolibre.com/economia/embajadora-de-eeuu-dice-que-el-clima-de-inversion-en-el-pais-es-impredecible-GE15557908")
    bsObj = BeautifulSoup(html, "html.parser")
    h1tittle = bsObj.find("span", {"class": "priority-content"}).get_text()
    return h1tittle

def Cleaner(Links):
    ResultList = []
    for link in Links:
        html = urlopen(f"{link}")
        bsObj = BeautifulSoup(html, "html.parser")
        h1title = bsObj.find("h1").get_text()
        h1title = re.sub("\s\s+", " ", h1title)
        ResultList.append([f"{link}",f"{h1title}"])
    return ResultList

def UnWraper(ListArray):
    ResultList = []
    for item in ListArray[0]:
        ResultList.append(item)
        
    return ResultList

def discardTwins(list1):
      newList= []
      [newList.append(x) for x in list1 if x not in newList]
          
      return newList
 
#ErrorFree
def retrieveTittlesActualidad(): 
    tittles = [[0 for x in range(9)] for y in range(1)]
    Url="https://www.diariolibre.com/actualidad"
    pageHtml = requests.get(Url)
    content = BeautifulSoup(pageHtml.content, 'html.parser')



    #La pagina se divide en grandes bloques de rows y esos rows contienen divs, #mientras el rowsContainer[0] solamente contiene  la noticia destacada 
    rowsContainer = content.find('section',{'class':'mb-2'}).find('div', {'class': 'container dl-container custom-container'})
    divCursor = rowsContainer.contents[1].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})

    #eSTAN FUERA DEL FOR PORQUE ES EL ARTICULO DESTACADO, ES UNICO Y DETERGENTE
    #tittles[0][0] = content.find('div', {'class': 'container dl-container custom-container'}).find('span', attrs={'class': 'priority-content'}).string
    tittles[0][0] ='https://www.diariolibre.com'+ content.find('div', {'class': 'container dl-container custom-container'}).find('a').get('href')

    cursor = 1
    while cursor <=8:
      for item in range(3): 
        if cursor > 2 and cursor <=5:
          divCursor = rowsContainer.contents[3].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
          #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
          tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
          cursor = cursor + 1
          
        elif cursor > 5:
          if cursor <9:
            divCursor = rowsContainer.contents[5].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
            #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
            tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
            cursor = cursor + 1

        elif cursor<=2:
          if item <2:
            #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
            tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
            cursor = cursor + 1
    result = UnWraper(tittles)
    FinalResult = Cleaner(result)
    return FinalResult
#DebugForError
def retrieveTittlesEconomia():
    Url="https://www.diariolibre.com/economia"

    tittles = [[0 for x in range(9)] for y in range(1)]
    pageHtml = requests.get(Url)
    content = BeautifulSoup(pageHtml.content, 'html.parser')

    #La pagina se divide en grandes bloques de rows y esos rows contienen divs, #mientras el rowsContainer[0] solamente contiene  la noticia destacada 
    rowsContainer = content.find('section',{'class':'mt-0 mb-0'}).find('div', {'class': 'container dl-container custom-container'})

    divCursor = rowsContainer.contents[1].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
    
    #ese tiene 2 porque se toma el del medio para ponerlo en grande

    #tittles[0][0] =content.find('div', {'class': 'container dl-container custom-container'}).find('span', attrs={'class': 'priority-content'}).string
    tittles[0][0] = 'https://www.diariolibre.com'+content.find('div', {'class': 'container dl-container custom-container'}).find('a').get('href')

    cursor = 1
    while cursor <=8:
      for item in range(3): 
        if cursor > 2 and cursor <=5:
          divCursor = rowsContainer.contents[3].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
          ##tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
          tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
          cursor = cursor + 1
          
        elif cursor > 5:
          if cursor <9:
            divCursor = rowsContainer.contents[5].find_all('div', {'class': "col-sm-6 col-md-4 pt-0 pb-2"})
            ##tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
            tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
            cursor = cursor + 1

        elif cursor<=2:
          if item <2:
            ##tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
            tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
            cursor = cursor + 1
    result = UnWraper(tittles)
    FinalResult = EconomiaCleaner(result)
    #FinalResult = Cleaner(result)
    return FinalResult
#ErrorFree
def retrieveTittlesRevista():
    Url="https://www.diariolibre.com/revista"

    tittles = [[0 for x in range(9)] for y in range(1)]
    pageHtml = requests.get(Url)
    content = BeautifulSoup(pageHtml.content, 'html.parser')

    #La pagina se divide en grandes bloques de rows y esos rows contienen divs, #mientras el rowsContainer[0] solamente contiene  la noticia destacada 
    rowsContainer = content.find_all('div', {'class': 'container dl-container custom-container'})

    #print(rowsContainer)
    
    divCursor = rowsContainer[1].contents[1].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})

    #print (divCursor[0].find('span', attrs={'class': 'priority-content'}).string)
    
    #ese tiene 2 porque se toma el del medio para ponerlo en grande

    #tittles[0][0] = content.find('div', {'class': 'container dl-container custom-container'}).find('span', attrs={'class': 'priority-content'}).string
    tittles[0][0] = 'https://www.diariolibre.com'+content.find('div', {'class': 'container dl-container custom-container'}).find('a').get('href')

    cursor = 1
    while cursor <=8:
      for item in range(3): 
        if cursor > 2 and cursor <=5:
          divCursor = rowsContainer[1].contents[3].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
          #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
          tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
          cursor = cursor + 1
          
        elif cursor > 5:
          if cursor <9:
            divCursor = rowsContainer[1].contents[5].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
            #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
            tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
            cursor = cursor + 1

        elif cursor<=2:
          if item <2:
            #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
            tittles[0][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')
            cursor = cursor + 1
    result = UnWraper(tittles)
    FinalResult = Cleaner(result)
    return FinalResult

def retrieveTittlesDeportes():
    
  Url="https://www.diariolibre.com/deportes"
  pageHtml = requests.get(Url)
  content = BeautifulSoup(pageHtml.content, 'html.parser')

  linksContainer = content.find_all('a', href=re.compile("^(/deportes/)([\w]+/){0,5}(((?!.*(tbt|disqus_thread).*).)*$)"))
  linksDeportes = []

  '''  for item in range(len(linksContainer)):
      print(len(linksContainer[item]['href']))
      print(linksContainer[item]['href'])'''

  for item in range(len(linksContainer)):
    if len(linksContainer[item]['href']) > 35 and  '#disqus_thread' not in linksContainer[item]['href']:
      linksDeportes.append("https://www.diariolibre.com"+linksContainer[item]['href'])
  
  linksDeportes= discardTwins(linksDeportes)
  FinalResult = Cleaner(linksDeportes)
  return FinalResult

def retrieveTittlesEstilos():
    ResultS = []
    htmllink = urlopen('https://www.diariolibre.com/estilos')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/estilos/)")):
        if 'href' in link.attrs:
            WholeLink = "https://www.diariolibre.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    FinalResult = EconomiaCleaner(ResultS)
    return FinalResult

def retrieveTittlesOpinion():
    ResultS = []
    htmllink = urlopen('https://www.diariolibre.com/opinion')
    bsObj = BeautifulSoup(htmllink, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/opinion/)")):
        if 'href' in link.attrs:
            WholeLink = "https://www.diariolibre.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                  ResultS.append(WholeLink)
    FinalResult = EconomiaCleaner(ResultS)
    return FinalResult

def giveTittle(url):
  html = requests.get(url)
  content = BeautifulSoup(html.content, "html.parser")
  tittle = content.find('div', {"class": "detail-news"}).find('span',{'class':'priority-content'}).text
  return tittle

def potaraFunction(list1,list2):
  for x in range(len(list1)):
    for y in range(len(list2)):
      if list1[x] != list2[y] and list2[y] != 0:
        list1.append(list2[y])   
  return list1


def GetDiarioLibreLinks(Election):
    #CategoryOptions = ["Actualidad", "Economia", "Revista", "Deportes", "Estilos", "Opinion"]
    if Election == 0:
          Actualidad = retrieveTittlesActualidad()
          return Actualidad
    
    elif Election == 1:
        Economia = retrieveTittlesEconomia()
        return Economia
    
    elif Election == 2:
        Revista = retrieveTittlesRevista()
        return Revista
    
    elif Election == 3:
        Deportes = retrieveTittlesDeportes()
        return Deportes
    
    elif Election == 4:
        Estilos = retrieveTittlesEstilos()
        return Estilos
    
    elif Election == 5:
        Opinion = retrieveTittlesOpinion()
        return Opinion


#CategoryOptions = ["Actualidad Good", "Economia Good", "Revista Good", "Deportes Good", "Estilos Good", "Opinion "]
