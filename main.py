from scrape_links import RecipeCrawler
import json

path = '/ja/wiki/カテゴリ:大型'

path_dict = {
    '小型': '/ja/wiki/カテゴリ:小型',
    '中型': '/ja/wiki/カテゴリ:中型',
    '大型': '/ja/wiki/カテゴリ:大型',
    '超大型': '/ja/wiki/カテゴリ:超大型',
}

crawler = RecipeCrawler()
recipes_for_each_tier = {
    '小型': {},
    '中型': {},
    '大型': {},
    '超大型': {},
}

for tier_name in path_dict.keys():
    crawler.set_path(path_dict[tier_name])
    recipes_for_each_tier[tier_name] = crawler.scrape_details()

with open('recipes_for_each_tier.json', 'w') as f:
    json.dump(recipes_for_each_tier, f, ensure_ascii=False)
