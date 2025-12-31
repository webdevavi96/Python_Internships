# Day 9 - Web Scraping Internship Task

"""
Task:
Create a web scraper, extract data from websites,
handle HTML/XML files.
"""

import requests
from bs4 import BeautifulSoup
import os


def handle_scraper(filename):
    url = "http://books.toscrape.com/"

    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()

        else:
            res = requests.get(url, timeout=10)
            res.raise_for_status()

            data = res.text

            with open(filename, "w", encoding="utf-8") as f:
                f.write(data)

        soup = BeautifulSoup(data, "html.parser")
        return soup

    except Exception as e:
        print("Error occurred:", str(e))
        return None


def extract_books(soup):
    books = soup.find_all("article", class_="product_pod")

    output = []
    output.append("Books available:\n")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        output.append(f"Title: {title}")
        output.append(f"Price: {price}")
        output.append("-" * 40)

    return "\n".join(output)


options = {
    "a": "to print the data.",
    "b": "To extract the data into a text file.",
}

user_choice = str(input(f"Choose one option to proced: {options}"))

file = "res.html"

soup = handle_scraper(file)

if not soup:
    exit()

if user_choice == "a":
    print(extract_books(soup))

elif user_choice == "b":
    extracted_data = extract_books(soup)

    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(extracted_data)

    print("Data successfully saved to data.txt")

else:
    print("Invalid option selected.")
