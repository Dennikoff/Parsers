import tkinter as tk
from app.internal.parser.parser import parse
from PIL import ImageTk, Image

LADA = "https://auto.ru/moskva/cars/vaz/all/"
BMW = "https://auto.ru/moskva/cars/bmw/all/"
HYUNDAI = "https://auto.ru/moskva/cars/hyundai/all/"
MERCEDES = "https://auto.ru/moskva/cars/mercedes/all/"
NISSAN = "https://auto.ru/moskva/cars/nissan/all/"
SKODA = "https://auto.ru/moskva/cars/skoda/all/"
TOYOTA = "https://auto.ru/moskva/cars/toyota/all/"


def take_content(url):
    content = parse(url)


    def button_clicked(url):
        parse(url)


def get_image(name):
    image = Image.open("images/lada.png")
    image = image.resize((50, 50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    return img


def create_button(window, name, col, row):
    url = f"https://auto.ru/moskva/cars/{name}/all/"
    button = tk.Button(window, text=name, command=lambda: button_clicked(url))
    button.grid(column=col, row=row, sticky='wesn')


def window_init():
    window = tk.Tk()
    window.title("Car parser")
    window.geometry("600x400")

    button_vaz = create_button(window, "vaz", 0, 1)
    button_bmw = create_button(window, "bmw", 1, 1)
    button_hyundai = create_button(window, "hyundai", 2, 1)
    button_mercedes = create_button(window, "mercedes", 3, 1)
    button_nissan = create_button(window, "nissan", 4, 1)
    button_skoda = create_button(window, "skoda", 5, 1)
    button_toyota = create_button(window, "toyota", 6, 1)


    window.grid_columnconfigure(0, minsize=80)
    window.grid_columnconfigure(1, minsize=80)
    window.grid_columnconfigure(2, minsize=80)
    window.grid_columnconfigure(3, minsize=80)
    window.grid_columnconfigure(4, minsize=80)
    window.grid_columnconfigure(5, minsize=80)
    window.grid_columnconfigure(6, minsize=80)
    window.grid_columnconfigure(7, minsize=80)
    window.grid_rowconfigure(0, minsize=100)

    window.mainloop()
