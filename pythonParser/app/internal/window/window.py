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


def get_image(name):
    image = Image.open(f"images/{name}")
    image = image.resize((50, 50), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    return image


def window_init():
    window = tk.Tk()
    window.title("Car parser")
    window.geometry("600x400")
    window.configure(bg="white")
    image = get_image("lada.png")
    button_lada = tk.Button(window, image=image)
    button_lada.grid(column=0, row=0)

    window.grid_columnconfigure(0, minsize=70)
    window.grid_rowconfigure(0, minsize=70)

    window.mainloop()
