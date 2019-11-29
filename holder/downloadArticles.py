import requests
from bs4 import BeautifulSoup
import os
import re

def downDiarioLibre(url):
  content=requests.get(url)
  bsObj = BeautifulSoup(content.content, 'html.parser')

  dir=  os.getcwd()
  content = bsObj.find('div',{'class':'paragraph'})
  fileName = url[(url.rindex('/')+1):(len(url))] 
  completePath = dir+'/articles/'+fileName+'.html'

  if os.path.exists(dir + "/articles") is False:
    os.mkdir(dir+'/articles')
  
  if content != None:
    with open(completePath,'w') as f:
      f.write(str(content)) 

  return completePath

def downListinDiario(url):
  content=requests.get(url)
  bsObj = BeautifulSoup(content.content, 'html.parser')

  dir=  os.getcwd()
  content = bsObj.find('div',{'id':'ArticleBody'})
  fileName = url[(url.rindex('/')+1):(len(url))]
  completePath = dir+'/articles/'+fileName+'.html'

  if os.path.exists(dir + "/articles") is False:
    os.mkdir(dir+'/articles')

  with open(completePath,'w') as f:
    f.write(str(content)) 

  return completePath

def main(url): 
  if 'diariolibre' in url:
    pathArticle = downDiarioLibre(url)
  elif 'listindiario' in url:
    pathArticle = downListinDiario(url)

  with open(pathArticle,'r') as document:
    html = document.read()




#CON FINES DE TESTEO
def discardTwins(list1):
  newList= []
  [newList.append(x) for x in list1 if x not in newList]
          
  return newList

def retrieveTittlesDeportes():

  Url="https://www.diariolibre.com/deportes"
  pageHtml = requests.get(Url)
  content = BeautifulSoup(pageHtml.content, 'html.parser')

  linksContainer = content.find_all('a', href=re.compile("^(/deportes/)([\w]+/){0,5}(((?!.*(tbt|disqus_thread).*).)*$)"))
  linksDeportes = []

  for item in range(len(linksContainer)):
    if len(linksContainer[item]['href']) > 35 and  '#disqus_thread' not in linksContainer[item]['href']:
      linksDeportes.append("https://www.diariolibre.com"+linksContainer[item]['href'])
  
  linksDeportes= discardTwins(linksDeportes)
  return linksDeportes 

def GetRepublicaLinks():
    htmllink = requests.get('https://listindiario.com/la-republica')
    bsObj = BeautifulSoup(htmllink.content, "html.parser")
    ResultS = []
    for link in bsObj.find_all("a", href=re.compile("^(/la-republica/)")):
        if 'href' in link.attrs:
            WholeLink = "https://listindiario.com" + f"{link.attrs['href']}"
            if WholeLink not in ResultS:
                ResultS.append(WholeLink)
    return ResultS


arrayListin= GetRepublicaLinks()
#arrayDeportes = retrieveTittlesDeportes()

for x in arrayListin:
  main(x)

