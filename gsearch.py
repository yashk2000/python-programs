import requests ; from bs4 import BeautifulSoup
import sys

search_item=input("enter search parameter and print Ctrl-C to stop :")#getting search parameter
# searching on "http://www.google.co.in"
engine="http://www.google.co.in"
url="http://www.google.co.in/search?q="+ search_item#obtaining url of search parameter
response=requests.get(url)#getting a web page
soup=BeautifulSoup(response.text,"lxml")#processing the html page into text using lxml
for item in soup.select(".r a"):#printing results on first page
	print(item.text)
for next_page in soup.select(".fl"):#going to next page
	res=requests.get(engine+next_page.get('href'))#obtaining the next web page
	soup= BeautifulSoup(res.text,"lxml")#processing the web page
	for item in soup.select(".r a"):#printing the results on that page
		print(item.text)
