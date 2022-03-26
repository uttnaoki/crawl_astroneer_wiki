import requests
from bs4 import BeautifulSoup

class ScrapeLinks():
    def __init__(self):
        self.url = ''

    def shape_a_tag(self, a_tag):
        return {
            'name': a_tag['title'],
            'url': a_tag['href']
        }

    def scrape_links(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tag_list = soup.select('div.mw-category-group a')
        return [ self.shape_a_tag(a_tag) for a_tag in a_tag_list ]

