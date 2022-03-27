import requests
from bs4 import BeautifulSoup
import time
import re

DELAY_SEC = 3
HOST_URL = 'https://astroneer.fandom.com'

class RecipeCrawler():
    def __init__(self):
        self.path = ''

    def set_path(self, path):
        self.path = path

    def shape_a_tag(self, a_tag):
        return {
            'name': a_tag['title'],
            'url': a_tag['href']
        }

    def scrape_links(self):
        response = requests.get(HOST_URL + self.path)
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tag_list = soup.select('div.mw-category-group a')
        return [ self.shape_a_tag(a_tag) for a_tag in a_tag_list ]

    def shape_mat_tag(self, td):
        num_list = re.sub(r'\D+', ' ', td.text).split()
        mat_list = re.sub(r'[\dx ]+', ' ', td.text).split()
        return [ { 'name': mat_list[i], 'num': int(num_list[i]) } for i in range(len(num_list))]

    def scrape_details(self):
        links = self.scrape_links()
        module_recipes = {}

        for link in links:
            print(link['name'])
            response = requests.get(HOST_URL + link['url'])
            soup = BeautifulSoup(response.text, 'html.parser')
            tr_list = soup.select('table.infoboxtable tr')
            time.sleep(DELAY_SEC)

            # クラフト対象でなければ continue
            if len(tr_list) < 8:
                continue
            td = tr_list[7].select('td')[0]
            module_recipes[link['name']] = self.shape_mat_tag(td)
        return module_recipes
