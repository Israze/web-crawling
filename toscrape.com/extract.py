import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-"
# category_url = 'https://books.toscrape.com/catalogue/category/'

all_books_without_categories = []
category_list = []

with open("results.txt", "w", encoding="utf-8") as file:
    for page in range(1, 51):
        url = base_url + str(page) + ".html"

        response = requests.get(url)

        soup  = BeautifulSoup(response.text, "html.parser")

        books = soup.findAll('article', class_='product_pod')

        for all_books in books:
            name = all_books.find("h3")
            name_text = name.get_text()
            formated_text = f"{name_text}, \n"
            file.write(formated_text)

    #         for book in name:
    #             all_books_without_categories.append(book.get_text())
    #
    # for name in all_books_without_categories:
    #     print(name)


#     categories = soup.findAll('ul', class_=['nav', 'nav-list'])
#
# #categories of books on the website
#     for category_name in categories:
#         category_name_down = category_name.find("li")
#         clean_category_name = ', '.join(category_name_down.get_text().split())  # Removes extra spaces
#         category_list.append(clean_category_name)
#
# for group in category_list:
#     print(group)





