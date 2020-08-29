import tkinter as tk
import random

miventana = tk.Tk()


def changeBG():
    # miventana.config(background='#76880A')
    colors = ['green', 'blue', 'yellow', '#ff00AA', '#f0f0f0', '#767676', '#00ff33']
    ramdom_colors = random.choice(colors)
    miventana.config(background=ramdom_colors)

def changebg():
    colors2 = ['red', 'yellow', 'white', 'blue']
    random_fondo = random.choice(colors2)
    main_title.config(bg=random_fondo)

miventana.geometry("500x200")
miventana.resizable(False, False)
miventana.title("Ventana de cambio de color-Curso udemy")
main_title = tk.Label(text="Python + Tkinter", font=("tahoma", 12), bg='#ff7763', fg='black', width=60, height=3)
main_title.place(x=-20, y=10)
main_btm = tk.Button(miventana, text="Boton de cambio de color fondo", command=changeBG)
main_btm.place(x=160, y=100)
#agregando mas cosas
otro_btm = tk.Button(miventana, text="color fondo", command=changebg)
otro_btm.place(x=210, y=140)
miventana.mainloop()