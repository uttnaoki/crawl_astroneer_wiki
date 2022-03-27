from scrape_links import RecipeCrawler

path = '/ja/wiki/カテゴリ:大型'

crawler = RecipeCrawler()
crawler.set_path(path)
crawler.scrape_details()
