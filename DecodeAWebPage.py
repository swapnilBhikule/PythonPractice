import requests
from bs4 import BeautifulSoup

link = 'https://www.nytimes.com/'

r = requests.get(link)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.find('class', 'story-heading')

print(title)