import requests 
from bs4 import BeautifulSoup as bs 
from datetime import date
import datetime
import os


if not os.path.isdir("logs"):
     os.mkdir("logs")

dt_now = str(datetime.datetime.now())

dt  = str(date.today())

filename=(dt)

path = ('logs')

fullfile = os.path.join(path,filename+".txt")

file = open (fullfile, "w")

link = "http://wiki/mediawiki-1.20.3/index.php/Список_сервисных_центров"

r = requests.get(link)
soup = bs(r.text,'lxml')

block = soup.find('div', id = "mw-content-text")


result = block.find_all('b')


file.write('Парсинг СЦ за:'+ dt_now + ':\n')

for sc in result:
	
	file.write(sc.text + '\n')


file.close
	

