import requests
from bs4 import BeautifulSoup

class WebScrapper():
   wikiDoc = requests.get("https://en.wikipedia.org/wiki/Deep_learning");
   parsedDoc = BeautifulSoup(wikiDoc.content, "html.parser")

   #Function to get the title of the page
   def getTitle(self):
     title = self.parsedDoc.title.string
     return title

   #Function to get all the links available
   def getWikiLinks(self):
       list =[]
       for link in self.parsedDoc.find_all('a'):
           # print(list)
           list.append(link.get('href'))

   #To save all the links in txt file
       for l in list:
           print(l,file=open("links.txt",'a'))
       return list

webs = WebScrapper()
print(webs.getTitle())
print(webs.getWikiLinks())