#Link of the tutorial: https://youtu.be/ng2o98k983k
from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')   #Defining the type of parse lxml

print(soup.prettify())  # to clean the html_file
# to get the title of the html
match=soup.title.text
print(match)
#to get the div tag
match=soup.div
print(match)
#to grab div in the footer
#lets use find method

match=soup.find('div',class_='_footer_') #Underscore is important
print(match)
#To grab the headline
#go on headline and give inspect
article=soup.find('div',class_='article') #Underscore is important
print(article)

headline=article.h2.a.text
print(headline)

summary=article.p.text
print(summary)
#to get all of the articles we use findall
for article in soup.find_all('div',class_='article'):
    headline=article.h2.a.text
    print(headline)

    summary=article.p.text
    print(summary)

    #blank line
    print()

#Doing the scrapping for the actual website.
#check the scrape2.py
