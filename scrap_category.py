import requests
import csv
from bs4 import BeautifulSoup

from get_category_all_pages import get_category_all_pages
from scrap_book_show import scrap_book_show


def scrap_category(url):
    '''Cree l'entete du csv de la categorie
    recupere tous les urls de livre de la categorie
    et applique scrap book show a chacun des urls'''
    en_tete = [
        "product_page_url",
        "universal_product_code",
        "title", "price_including_tax",
        "price_excluding_tax",
        "number_available",
        "product_description",
        "category",
        "review_rating",
        "image_url"
    ]
    csv_name = get_category_all_pages(url)[0] + ".csv"
    with open('csv/' + csv_name, 'w', encoding="utf-8-sig") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
    book_list = []
    list_pages_urls = get_category_all_pages(url)[1]
    print(get_category_all_pages(url)[1])
    for url in list_pages_urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        image_containers = soup.find_all(class_="image_container")
        for image_container in image_containers:
            book_link = image_container.find("a")['href'][8:]
            real_link = f"https://books.toscrape.com/catalogue/{book_link}"
            book_list.append(real_link)
    for book_show_url in book_list:
        scrap_book_show(book_show_url, csv_name)
