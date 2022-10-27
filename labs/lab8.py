import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.yelp.com/biz/the-hitching-post-cincinnati").content
soup = BeautifulSoup(data, 'html.parser')

span = soup.find("h1")
title = span.text


span = soup.find("div", {"class":"five-stars__09f24__mBKym five-stars--large__09f24__Waiqf display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})
rating = span['aria-label']


span = soup.find("span", {"class":"css-1d810fm"})
status = span.text


span = soup.find("span", {"class":"display--inline__09f24__c6N_k margin-l1__09f24__m8GL9 border-color--default__09f24__NPAKY"})
hours = span.text

print("The restaurant %s has a %s is currently %s and their hours are %s" % (title, rating, status, hours))

