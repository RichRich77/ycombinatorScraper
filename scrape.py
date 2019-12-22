'''
BeautifulSoup is a library that gives tools for scraping (used for this app)
Scrapy is a Framework that goes beyond BeautifulSoup capabilities for scraping websites (scrapy.org)
Consider checking the website for API before scraping. Data you want may be available via that sites' API
'''

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res, res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
# votes = soup.select('.score')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['points'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        # title = links[idx].getText()
        # href = links[idx].get('href', None)
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'points': points})
    # return hn
    return sort_stories_by_votes(hn)

# print(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(links, subtext))


