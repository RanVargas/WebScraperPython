import requests
from bs4 import BeautifulSoup
import os


def downDiarioLibre(url):
  content=requests.get(url)
  bsObj = BeautifulSoup(content.content, 'html.parser')

  dir=  os.getcwd()
  bsObj = bsObj.find('div',{'class':'text'})
  fileName = url[(url.rindex('/')+1):(len(url))] #para obteber el nombre del articulo
  completePath = dir+'/articles/'+fileName+'.html'

  if os.path.exists(dir + "/articles") is False:
    os.mkdir(dir+'/articles') 

  with open(completePath,'w') as f:
    f.write(str(bsObj))
  return completePath

def main(url): #Cambiale el nombre si quieres, no se me ocurrio nada xd
  pathArticle = downDiarioLibre(url)

  with open(pathArticle,'r') as document:
    html = document.read()

  content = BeautifulSoup(html,'html.parser')

  print(content.find_all('p'))



url= "https://www.diariolibre.com/actualidad/ciudad/el-metro-de-santo-domingo-por-dentro-durante-su-servicio-y-receso-diario-KJ15585395"
main(url)



"""
Hay que hacer 3 funciones. Una funcion por periodico que retorne todo el contenido de ese articulo. 
Eso voy a ver si lo hago maniana ya que te puse a tu lo de escribir el objeto en el html
"""