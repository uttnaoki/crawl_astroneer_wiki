from scrape_links import ScrapeLinks

domain_url = 'https://astroneer.fandom.com'
url = 'https://astroneer.fandom.com/ja/wiki/カテゴリ:大型'

links = ScrapeLinks()
links.domain_url = domain_url
links.url = url
links.scrape_details()
