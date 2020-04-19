import tkinter
raiz = tkinter.Tk()
raiz.title("Mi primer programa de tkinter")


#creamos el componente frame.
#creamos el componente label
texto = "Etiqueta Label"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg='red', bg='pink', font=('Arial', 30))
etiqueta.pack()

#creando el metodo entrada junto con los otros
entrada = tkinter.Entry(raiz)
entrada.config(justify= 'center')
entrada.pack()

#creando el metodo entrada junto con los otros
entrada2 = tkinter.Entry(raiz)
entrada2.config(justify= 'center', show='*')
entrada2.pack()

#componente texto
entrada3 = tkinter.Text(raiz)
entrada3.config(width=20, height= 10, font=('Verdana',15), padx=10, pady=20, fg='green', selectbackground="lightblue")

#agregar boton
def accion():
    print("Esto es lo que muestra")
boton1 = tkinter.Button(raiz, text="Toque Aquí", command=accion)
boton1.config(fg='green', background='yellow')
boton1.pack()

entrada3.pack()

#creamos el componente frame.
frame = tkinter.Frame(raiz)
frame.config(bg="orange", width=100, height=50 )
frame.pack()

#agregar boton
def accion():
    print("Esto es lo que muestra")
boton = tkinter.Button(raiz, text="Toque Aquí", command=accion)
boton.pack()


texto = "Etiqueta Label"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg='blue', bg = 'yellow', font=('Arial', 30))
etiqueta.pack()


raiz.mainloop()

