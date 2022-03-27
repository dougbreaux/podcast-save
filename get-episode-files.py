import feedparser
import urllib.request
import re
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

    # zero-pad single-digit month/day
    filename = f'{year}-{month:02d}-{day:02d}-{title}.mp3'

    # remove/replace illegal filename chars, like '?'
    valid_filename = re.sub('[^\w_.)( -]', '', filename)
    
    print("Retrieving " + valid_filename)
    urllib.request.urlretrieve(fileUrl, valid_filename)
    
    date=datetime.datetime(year=year, month=month, day=day)
    modTime=time.mktime(date.timetuple())
    os.utime(valid_filename, (modTime,modTime))
