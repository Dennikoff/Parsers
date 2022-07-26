from bs4 import BeautifulSoup as BS
# from html import get_html


def parse(url):
    params = ""
    i = 2
    # while True:
    #     html = get_html(url.get(), params)
    #     params = f"page={i}"
    #     i += 1
    #
    #     if html.status_code == 200:
    #         get_content(html.text)
    #     else:
    #         print("Error")
    #         break


def get_content(html):
    soup = BS(html, "html.parser")
    items = soup.find_all('div', class_="ListingItem")

    cars = []

    for item in items:
        cars.append({
            "name": item.find('a', class_="Link ListingItemTitle__link").get_text(),
            "price": item.find('div', class_="ListingItemPrice__content").get_text().replace("\xa0", " "),
        })
    for car in cars:
        print(car)