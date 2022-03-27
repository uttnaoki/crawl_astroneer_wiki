import requests
from bs4 import BeautifulSoup
import time
import re

DELAY_TIME = 3

class ScrapeLinks():
    def __init__(self):
        self.domain_url = ''
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

    def scrape_details(self):
        links = self.scrape_links()
        # for link in [links[3]]:
        for link in links:
            response = requests.get(self.domain_url + link['url'])
            soup = BeautifulSoup(response.text, 'html.parser')
            tr_list = soup.select('table.infoboxtable tr')
            time.sleep(DELAY_TIME)
            if len(tr_list) < 8:
                continue
            td = tr_list[7].select('td')[0]
            print(td.text)
            
            num_list = re.sub(r'\D+', ' ', td.text).split()
            mat_list = re.sub(r'[\dx ]+', ' ', td.text).split()
            print([ { 'name': mat_list[i], 'num': num_list[i] } for i in range(len(num_list))])
