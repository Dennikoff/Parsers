from tkinter import *
from bs4 import BeautifulSoup as BS
import requests

URL = "https://auto.ru/moskva/cars/hyundai/all/"


def get_html(url, params=None):
    r = requests.get(url, params=params)
    print(r.url)
    r.encoding = 'utf-8'
    return r


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


def parse():
    html = 1
    params = ""
    i = 2
    while True:
        html = get_html(url.get(), params)
        params = f"page={i}"
        i+=1

        if html.status_code == 200:
            get_content(html.text)
        else:
            print("Error")
            break

window = Tk()
window.title("Car parser")
frm = Frame(window, pady=10,padx=10)
frm.grid()
window.geometry("600x400")

Label(frm, text="Hello World!").grid(column=0, row=0)

url = StringVar()

message_entry = Entry(textvariable=url)
message_entry.place(relx=.3, rely=.1, anchor="nw")

message_button = Button(text="Parse", command=parse)
message_button.place(relx=.5, rely=.5, anchor="nw")




window.mainloop()
