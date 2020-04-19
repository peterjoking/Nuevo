import tkinter

raiz = tkinter.Tk()

raiz.title("Programa 2")
#Opciones múltiples
def seleccionar():
    print('La opción elegida es {}'.format(opcion.get()))

opcion = tkinter.IntVar()

botonradio1 = tkinter.Radiobutton(raiz, text='Opción 1', variable=opcion, value = 1, command=seleccionar)
botonradio1.pack()

botonradio2 = tkinter.Radiobutton(raiz, text='Opción 2', variable=opcion, value = 2, command=seleccionar)
botonradio2.pack()

botonradio3 = tkinter.Radiobutton(raiz, text='Prueba 3', variable=opcion, value = 3, command=seleccionar)
botonradio3.pack()

#Boton chequear
def verificar():
    valor = check1.get()
    if (valor ==1):
        print("el check está activado")
    else:
        print("El check no está activado")

check1 = tkinter.IntVar()
boton1 = tkinter.Checkbutton(raiz, text='Opcion numero 1', variable = check1, onvalue =1, offvalue=0, command=verificar)
boton1.pack()

raiz.mainloop()