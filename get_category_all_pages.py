import requests

from bs4 import BeautifulSoup


def get_category_all_pages(url):
    # Landing on category index.html
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Define which category
    category = soup.find("h1").string
    list_url = [url]
    if soup.find(class_="current"):
        nb_total_pages = int(soup.find(class_="current").string[-27])
        for i in range(2, nb_total_pages + 1):
            list_url.append(f"{url[0:-10]}page-{i}.html")
    return [category, list_url]
