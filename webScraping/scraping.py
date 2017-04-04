from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.nacion.com")
scrap = BeautifulSoup(html)
nameList = scrap.findAll("div", {"class": "u-first"})
for name in nameList:
    print(name.get_text())




