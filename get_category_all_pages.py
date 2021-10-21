import requests

from bs4 import BeautifulSoup


def get_category_all_pages(url):
    '''Arrive sur index.html de la categorie
    recupere le nom de categorie
    retourne une liste de deux elements
    [le nom de la categorie, liste des urls des pages liees a la categorie'''
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
