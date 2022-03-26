from scrape_links import ScrapeLinks

url = 'https://astroneer.fandom.com/ja/wiki/カテゴリ:大型'

links = ScrapeLinks()
links.url = url
print(links.scrape_links())
