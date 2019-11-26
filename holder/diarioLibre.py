
import requests
from bs4 import BeautifulSoup

 #ASI ERAN ANTES :'v
 #tittles[0][cursor] = divCursor[item].find('span', attrs={'class': 'priority-content'}).string
 #tittles[1][cursor] = 'https://www.diariolibre.com'+ divCursor[item].find('a').get('href')



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
    return tittles
    
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

    return tittles

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

    return tittles

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


articlesRevista =retrieveTittlesRevista()
articlesEconomia = retrieveTittlesEconomia()
articlesActualidad = retrieveTittlesActualidad()
#FULLLIST CONTIENE TOODO
fullList = potaraFunction(articlesRevista,articlesEconomia)
fullList = potaraFunction(fullList,articlesActualidad)

'''
for x in range(len(fullList)):
      print(fullList[x])
'''


