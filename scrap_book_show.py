import requests
import re
import csv

from bs4 import BeautifulSoup

from download_image import download_image


def scrap_book_show(url, csv_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_tds = soup.find_all("td")
    product_page_url = url
    print(product_page_url)
    universal_product_code = all_tds[0].string
    print(universal_product_code)
    title = soup.find("h1").string
    print(title)
    price_including_tax = all_tds[2].string
    print(price_including_tax)
    price_excluding_tax = all_tds[3].string
    print(price_excluding_tax)
    number_available = re.findall('\\d+', all_tds[5].string)[0]
    print(number_available)
    product_description = soup.findAll("meta")[2]["content"]
    print(product_description)
    product_description = product_description.replace(',', ';')
    print(product_description)
    category = soup.find(class_="breadcrumb").find_all_next("a")[2].string
    print(category)
    review_rating = soup.find(class_="star-rating")['class'][1]
    print(review_rating)
    image_url = "https://books.toscrape.com/" + soup.find("img")['src'][6:]
    print(image_url)
    download_image(image_url, universal_product_code)
    row = [
        product_page_url,
        universal_product_code,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        review_rating,
        image_url
    ]
    with open('csv/' + csv_name, 'a', encoding="utf-8-sig") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(row)
