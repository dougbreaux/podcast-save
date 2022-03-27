import feedparser
import urllib.request
import datetime
import time
import os

feed = feedparser.parse('https://heritagepark.org/podcast/1e3ea995-6640-464a-96d8-7e70eecdb18a.xml')

for entry in feed.entries:

    title = entry.title
    fileUrl = entry.enclosures[0].href
    
    published = entry.published_parsed
    year = published.tm_year
    month = published.tm_mon
    day = published.tm_mday

    filename = f'{year}-{month}-{day}-{title}.mp3'
    
    print(filename)
    #urllib.request.urlretrieve(fileUrl, filename)
