from bs4 import BeautifulSoup
import requests

# Pull info from web
url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
contents = requests.get(url)
web_info = contents.text

# Scrape with Beautiful Soup
soup = BeautifulSoup(web_info, 'html.parser')
title = soup.find_all(name='h3', class_='title')

# Add movie titles to list
top_100 = []
for items in title:
    top_100.append(items.getText())
top_100.reverse()

# Add list items to txt file
with open(file="top_100.txt", mode='w', encoding='utf-8') as file:
    for row in top_100:
        file.write(str(row) + '\n')
