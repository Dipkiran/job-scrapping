from bs4 import BeautifulSoup

import requests

r = requests.get("http://jkssb.nic.in/WriteReadData/File/Home.htm")

data = r.text

soup = BeautifulSoup(data, "html.parser")


article = soup.find("div", {"class": "top"}).findAll('li')
i = 1
for element in article:
    for a in element.find_all('a', href=True):
        print a.text
        print "http://jkssb.nic.in/" + a['href']

