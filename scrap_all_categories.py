import requests

from bs4 import BeautifulSoup


def scrap_all_categories():

    index = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    page = requests.get(index)
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = soup.find(class_="nav-list").findChildren("a")
    urls_categories = []
    url_prefix = "https://books.toscrape.com/catalogue/category/"
    for url in urls:
        urls_categories.append(url_prefix + url['href'][3:])
    urls_categories.pop(0)
    return urls_categories
