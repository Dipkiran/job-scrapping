from bs4 import BeautifulSoup

import requests
import csv

outfile = open('career.csv','w')
writer = csv.writer(outfile)
writer.writerow(["job_link", "job_desc"])

r = requests.get("http://jkssb.nic.in/WriteReadData/File/Home.htm")

data = r.text

soup = BeautifulSoup(data, "html.parser")


article = soup.find("div", {"class": "top"}).findAll('li')
i = 1
for element in article:
    for a in element.find_all('a', href=True):
        if i <11:
            item_link =  a.text
            item_text = "http://jkssb.nic.in/" + a['href']
            writer.writerow([item_link, item_text])
            i+=1

outfile.close()
