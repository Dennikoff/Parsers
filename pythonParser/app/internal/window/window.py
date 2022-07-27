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
window = tk.Tk()


def take_content(url):
    content = parse(url)


def get_image(name):
    image = Image.open("images/lada.png")
    image = image.resize((50, 50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    return img


def create_button(name):
    global window
    button = tk.Button(window, text=name)
    button.grid(column=0, row=0)


def window_init():
    global window
    window.title("Car parser")
    window.geometry("600x400")
    window.configure(bg="white")

    button_lada = create_button("lada")

    window.grid_columnconfigure(0, minsize=70)
    window.grid_rowconfigure(0, minsize=70)

    window.mainloop()
