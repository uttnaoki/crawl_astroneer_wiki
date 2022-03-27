from recipe_crawler import RecipeCrawler
import json

path = '/ja/wiki/カテゴリ:大型'

path_dict = {
    'Small': '/wiki/Category:Small',
    'Medium': '/wiki/Category:Medium',
    'Large': '/wiki/Category:Large',
    'Extra_Large': '/wiki/Category:Extra_Large',
}

crawler = RecipeCrawler()
recipes_for_each_tier = {
    'Small': {},
    'Medium': {},
    'Large': {},
    'Extra_Large': {},
}

for tier_name in path_dict.keys():
    crawler.set_path(path_dict[tier_name])
    recipes_for_each_tier[tier_name] = crawler.scrape_details()

with open('recipes_for_each_tier.json', 'w') as f:
    json.dump(recipes_for_each_tier, f, ensure_ascii=False)
