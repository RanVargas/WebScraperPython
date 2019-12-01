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
 
  return pathArticle

