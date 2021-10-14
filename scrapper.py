from scrap_all_categories import scrap_all_categories
from scrap_category import scrap_category

def scrapper():
    urls_categories = scrap_all_categories()
    for url in urls_categories:
        scrap_category(url)

scrapper()