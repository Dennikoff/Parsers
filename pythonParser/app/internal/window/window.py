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


def window_init():
    window = tk.Tk()
    window.title("Car parser")
    window.geometry("600x400")

    img = Image.open("lada.png")

    lada_image = ImageTk.PhotoImage(file=img)
    button_lada = tk.Button(window,)
    button_lada.grid(column=0, row=1)
