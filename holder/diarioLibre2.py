import requests
from bs4 import BeautifulSoup
import re

def retrieveTittlesActualidad():
    tittles = []
    Url="https://www.diariolibre.com/actualidad"
    pageHtml = requests.get(Url)
    content = BeautifulSoup(pageHtml.content, 'html.parser')

    #La pagina se divide en grandes bloques de rows y esos rows contienen divs, #mientras el rowsContainer[0] solamente contiene  la noticia destacada 
    rowsContainer = content.find('section',{'class':'mb-2'}).find('div', {'class': 'container dl-container custom-container'})
    divCursor = rowsContainer.contents[1].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})

    #eSTAN FUERA DEL FOR PORQUE ES EL ARTICULO DESTACADO, ES UNICO Y DETERGENTE
    tittles.append('https://www.diariolibre.com'+ content.find('div', {'class': 'container dl-container custom-container'}).find('a').get('href'))

    cursor = 1
    while cursor <=8:
      for item in range(3): 
        if cursor > 2 and cursor <=5:
          divCursor = rowsContainer.contents[3].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
          tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
          cursor = cursor + 1
          
        elif cursor > 5:
          if cursor <9:
            divCursor = rowsContainer.contents[5].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
            tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
            cursor = cursor + 1

        elif cursor<=2:
          if item <2:
            tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
            cursor = cursor + 1

    return tittles
    
def retrieveTittlesEconomia():
    Url="https://www.diariolibre.com/economia"

    tittles = []
    pageHtml = requests.get(Url)
    content = BeautifulSoup(pageHtml.content, 'html.parser')

    rowsContainer = content.find('section',{'class':'mt-0 mb-0'}).find('div', {'class': 'container dl-container custom-container'})
    divCursor = rowsContainer.contents[1].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})

    tittles.append('https://www.diariolibre.com'+content.find('div', {'class': 'container dl-container custom-container'}).find('a').get('href'))

    cursor = 1
    while cursor <=8:
      for item in range(3): 
        if cursor > 2 and cursor <=5:
          divCursor = rowsContainer.contents[3].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
          tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])

          cursor = cursor + 1
          
        elif cursor > 5:
          if cursor <9:
            divCursor = rowsContainer.contents[5].find_all('div', {'class': "col-sm-6 col-md-4 pt-0 pb-2"})

            tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
            cursor = cursor + 1

        elif cursor<=2:
          if item <2:       
            tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
            cursor = cursor + 1

    return tittles

def retrieveTittlesRevista():
    Url="https://www.diariolibre.com/revista"

    tittles = []
    pageHtml = requests.get(Url)
    content = BeautifulSoup(pageHtml.content, 'html.parser')

    rowsContainer = content.find_all('div', {'class': 'container dl-container custom-container'})
    divCursor = rowsContainer[1].contents[1].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})

    tittles.append('https://www.diariolibre.com'+content.find('div', {'class': 'container dl-container custom-container'}).find('a').get('href'))

    cursor = 1
    while cursor <=8:
      for item in range(3): 
        if cursor > 2 and cursor <=5:
          divCursor = rowsContainer[1].contents[3].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})    
          tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
          cursor = cursor + 1
        
        elif cursor > 5:
          if cursor <9:
            divCursor = rowsContainer[1].contents[5].find_all('div', {'class': "col-sm-6 col-md-4 pt-2 pb-2"})
            tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
            cursor = cursor + 1

        elif cursor<=2:
          if item <2:
            tittles.append('https://www.diariolibre.com'+ divCursor[item].find('span', {"class":"priority-content"}).parent.parent['href'])
            cursor = cursor + 1

    return tittles

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
  return linksDeportes 

def getTittle(url):
  html = requests.get(url)
  content = BeautifulSoup(html.content, "html.parser")
  tittle = content.find('h1').text
  return tittle

def potaraFunction(list1,list2):
  for x in range(len(list1)):
    for y in range(len(list2)):
      if list1[x] != list2[y] and list2[y] != 0:
        list1.append(list2[y])   
  return list1

def discardTwins(list1):
  newList= []
  [newList.append(x) for x in list1 if x not in newList]
          
  return newList
 
def getContent(url):
  html = requests.get(url)
  content = BeautifulSoup(html.content, "html.parser")
  text = content.find('div',{"class":"content-box"}).find_all('p')
  textPage = ""
  for item in text:
    textPage = textPage + item.text
  
  return textPage

def getCompleteArray(array):
  newarray = [[0 for x in range(len(array))] for y in range(3)]
  for x in range(len(array)):
    newarray[0][x] = array[x]
    newarray[1][x] = getTittle(array[x])
    newarray[2][x] = getContent(array[x])
  return newarray



arrayRevista = getCompleteArray(retrieveTittlesRevista())
arrayEconomia = getCompleteArray(retrieveTittlesEconomia())
arrayActualidad = getCompleteArray(retrieveTittlesActualidad())
arrayDeportes = getCompleteArray(retrieveTittlesDeportes())


 
arrayDeportes=  arrayActualidad

for x in range(len(arrayDeportes)):
  print("\n")
  for y in range(len(arrayDeportes[x])):
            print(arrayDeportes[x][y])
"""   
for x in arrayDeportes:
  print(x)
   

       


for x in range(len(revista)):
  print("\n")
  for y in range(len(revista[x])):
            print(revista[x][y])
"""