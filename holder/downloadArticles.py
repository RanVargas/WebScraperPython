import requests
from bs4 import BeautifulSoup
import os
import re
import requests

def downHoy(url):
  content=requests.get(url)
  bsObj = BeautifulSoup(content.content, 'html.parser')

  dir=  os.getcwd()
  content = bsObj.find('section',{'class':'articulo'})
  fileName = url[(url.rindex('/')+1):(len(url))] 
  completePath = dir+'/articles/'+fileName+'.html'

  if os.path.exists(dir + "/articles") is False:
    os.mkdir(dir+'/articles')
  
  if content != None:
    with open(completePath,'w') as f:
      f.write(str(content)) 

  return completePath


def downDiarioLibre(url):
  content=requests.get(url)
  bsObj = BeautifulSoup(content.content, 'html.parser')

  dir=  os.getcwd()
  contentTittle = bsObj.find('h1')
  content = bsObj.find('div',{'class':'text'})
  fileName = url[(url.rindex('/')+1):(len(url))] 
  completePath = dir+'/articles/'+fileName+'.html'

  if os.path.exists(dir + "/articles") is False:
    os.mkdir(dir+'/articles')

  with open(completePath,'w') as f:
    f.write(str(contentTittle))
    f.write(str(content)) 

  return completePath

def downListinDiario(url):
  content=requests.get(url)
  bsObj = BeautifulSoup(content.content, 'html.parser')

  dir=  os.getcwd()
  contentTittle = bsObj.find('h1')
  content = bsObj.find('div',{'id':'ArticleBody'})
  fileName = url[(url.rindex('/')+1):(len(url))]
  completePath = dir+'/articles/'+fileName+'.html'

  if os.path.exists(dir + "/articles") is False:
    os.mkdir(dir+'/articles')

  with open(completePath,'w') as f:
    f.write(str(contentTittle))
    f.write(str(content)) 

  return completePath

def mainDownloader(url): 

  if 'diariolibre' in url:
    pathArticle = downDiarioLibre(url)
  
  elif 'listindiario' in url:
    pathArticle = downListinDiario(url)
  
  elif 'hoy.com.do' in url:
        pathArticle = downListinDiario(url)
 
  return pathArticle

