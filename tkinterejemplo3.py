#caja de mensaje y boton

import tkinter
from tkinter import messagebox
from tkinter import filedialog
raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
    tkinter.messagebox.showinfo('El titulo aqui', 'este es el mensaje')

boton1 = tkinter.Button(raiz, text='Pulsar para ver que pasa', command = avisar)
boton1.pack()



# siguiente ejercicio
def preguntar():
    resultado = tkinter.messagebox.askquestion('Pregunta 1', 'quiere borrar el archivo?')
    if (resultado =='yes'):
        print("Si quiero borrar")
    else:
        print("no no quiero borrar nada")

boton2 = tkinter.Button(raiz, text='Que quiere hacer?', command = preguntar)
boton2.pack()

def abrir():
    rutafichero= filedialog.askopenfilename(title='Abrir archivo')
    print(rutafichero)

buton3 = tkinter.Button(raiz, text = "abrir archivo", command= abrir)
buton3.pack()
raiz.mainloop()
