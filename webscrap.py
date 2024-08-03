import requests
from bs4 import BeautifulSoup
import pandas as pad
import csv
def get_title(link):
    try:
        k=link.find("span",attrs={"class":"VU-ZEz"})
        k=k.text
        k=k.strip()
        print(k)
    except AttributeError:
        k=""
    return k
def get_price(link):
    try:
        k=link.find("div",attrs={"class":"Nx9bqj CxhGGd"})
        k=k.text
    except AttributeError:
        k=""
    return k
def get_rating(link):
    try:
        k=link.find("div",attrs={"class":"XQDdHH"}).text
    except AttributeError:
        k=""
    return k

HEADER = ({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",'Accept-Language':'en-US, en;q=0.5'})
URL ="https://www.flipkart.com/search?q=realme&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
r= requests.get(URL, headers=HEADER)
print(r)
soup=BeautifulSoup(r.content,'html.parser')
list=soup.findAll("a",attrs={ "class" : "CGtC98"})
hreflist=[]
for link in list:
    hreflist.append(link.get("href"))
print(hreflist)
d={"title":[],"price":[],"ratings":[],"website":[]}
i=0
for url in hreflist:
    try:
        r=requests.get("https://www.flipkart.com"+url,headers=HEADER)
        SOUP=BeautifulSoup(r.content,'html.parser')
        d["title"].append(get_title(SOUP))
        d["price"].append(get_price(SOUP))
        d["ratings"].append(get_rating(SOUP))
        d["website"].append("https://www.flipkart.com"+url)
    except requests.exceptions.ConnectionError as e:
        pass
print(d)
df = pad.DataFrame(d)
df.to_excel("data.xlsx", index = False)