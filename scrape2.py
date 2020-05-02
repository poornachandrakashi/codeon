from bs4 import BeautifulSoup
import requests

#Downloading the source code of the website.
source=requests.get('https://coreyms.com').text

soup =BeautifulSoup(source,'lxml')

print(soup.prettify())

#Parsing out the information
#Grab the first headline
