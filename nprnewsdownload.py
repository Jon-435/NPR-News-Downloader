import requests
from bs4 import BeautifulSoup

url = 'https://www.npr.org/rss/podcast.php?id=500005'
response = requests.get(url)
xml_data = response.content

soup = BeautifulSoup(xml_data, 'xml')
item = soup.find('item')

enclosure_tag = item.find('enclosure')

mp3_url = enclosure_tag['url']

response = requests.get(mp3_url)
with open('npr_news.mp3', 'wb') as f:
    f.write(response.content)