import requests

from bs4 import BeautifulSoup

def scrap_all_categories():
    index_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    page = requests.get(index_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = soup.find(class_="nav-list").findChildren("a")
    urls_categories = []
    for url in urls:
        urls_categories.append("https://books.toscrape.com/catalogue/category/" + url['href'][3:])
    urls_categories.pop(0)
    return urls_categories
