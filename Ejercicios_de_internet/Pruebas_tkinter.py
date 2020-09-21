import tkinter as tk
from tkinter import messagebox
miventana = tk.Tk()
miventana.title('Título de Mi ventana')
miventana.geometry('500x500')
miventana.resizable(False, True)

def mensaje():
    messagebox.showinfo('Caja de Mensajes',' Este es un mensaje de la función messagebox')

boton1 = tk.Button(miventana, text= 'Boton1', bg='#00FF00', fg='#FF1111', font=('Times New Roman',18), command=mensaje )
#boton1.pack()
boton1.place(x=200, y=50)

miventana.mainloop()