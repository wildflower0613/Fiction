import re
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL of the website
base_url = "https://books.toscrape.com/catalogue/category/books/fiction_10/"
current_url = base_url + "page-1.html"


def extrbook_data(book_url: str) -> dict:
    page = requests.get(book_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_="table table-striped")
    if not table:
        print("Table not found for:", book_url)
        print("Page title was:", soup.title)
        return {}
    extract = table.find("tbody")
    count = 0
    data = list()
    rows = table.find_all("tr")
    for row in rows:
        key = row.find("th").text.strip()
        value = row.find("td").text.strip()
        data.append([key, value])
    ratingtag = soup.find("p", class_="star-rating")
    rating = ratingtag["class"][1]
    proddescript = soup.find("p", attrs={'class': None}).get_text()
    title = (book.h3.a['title'])
    safetitle = re.sub(r'[^\w\-]', '_', title)
    price = book.find('p', class_='price_color').get_text()
    print(title, price, book_url, rating, proddescript)



while current_url:
    # Fetch the content of the current page
    response = requests.get(current_url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    write_header = True


    def extrbook_data(book_url: str) -> dict:
        page = requests.get(book_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find("table", class_="table table-striped")
        if not table:
            print("Table not found for:", book_url)
            print("Page title was:", soup.title)
            return {}
        extract = table.find("tbody")
        count = 0
        data = list()
        rows = table.find_all("tr")
        for row in rows:
            key = row.find("th").text.strip()
            value = row.find("td").text.strip()
            data.append([key, value])
        ratingtag = soup.find("p", class_="star-rating")
        rating = ratingtag["class"][1]
        proddescript = soup.find("p", attrs={'class': None}).get_text()
        title = (book.h3.a['title'])
        safetitle = re.sub(r'[^\w\-]', '_', title)
        price = book.find('p', class_='price_color').get_text()









    # Extract the desired data (e.g., book titles)
    for book in books:
        relative_url = book.a["href"]
        book_url = urljoin(current_url, relative_url)
        book_dict = dict(extrbook_data(book_url))
        book_dict["title"] = title
        book_dict["rating"] = rating
        book_dict["description"] = proddescript
        headers = list(book_dict.keys())
        row = list(book_dict.values())
        headers = list(book_dict.keys())
        row = list(book_dict.values())

    with open('fiction_books.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if write_header == True:
            writer.writerow(headers)
            write_header = False
        writer.writerow(row)





    # Find the "Next" button
    next_button = soup.find("li", class_="next")
    if next_button:

    # Get the relative URL and form the absolute URL
        next_page = next_button.a["href"]
        current_url = urljoin(base_url, next_page)
    else:
    # No "Next" button found, end the loop
        current_url = None









