from scrap_all_categories import scrap_all_categories
from scrap_category import scrap_category


def scrapper():
    '''Recupere toutes les categories
    lance le scrapping sur toutes les pages categories
    qui lancera les scrapping sur les shows des categories'''
    urls_categories = scrap_all_categories()
    for url in urls_categories:
        scrap_category(url)


if __name__ == '__main__':
    scrapper()
