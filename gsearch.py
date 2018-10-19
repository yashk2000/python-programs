import requests ; from bs4 import BeautifulSoup
import sys

search_item=input("enter search parameter and print Ctrl-C to stop :")
base="http://www.google.co.in"
url="http://www.google.co.in/search?q="+ search_item

response=requests.get(url)
soup=BeautifulSoup(response.text,"lxml")

for item in soup.select(".r a"):
	print(item.text)


for next_page in soup.select(".fl"):
		res=requests.get(base + next_page.get('href'))
		soup= BeautifulSoup(res.text,"lxml")
		for item in soup.select(".r a"):
				print(item.text)
