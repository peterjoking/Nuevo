from tkinter import *
myventana = Tk()
myventana.geometry("500x500")
myventana.title('Formulario')
myventana.resizable(False, False)
myventana.config(background= '#213141')
main_title = Label(text= 'Formulario Python | Datos', font = ('Arial', 14), bg = "#56CD63", fg = "white", width = "500", height = "2")
main_title.pack()
#Para dar transparencia
#myventana.attributes("-alpha", 0.8)
def send_data():
    username_data = usernames.get()
    password_data = str(password.get())
    codigo_data = codigo.get()
    produto_data = produto.get()

    print(username_data, "\t",password_data,"\t", codigo_data,"\t", produto_data)
    new_file = open("/Users/Pedro/Google Drive/Practicas/Registro_Udemy_Formulario.txt", "a")
    new_file.write(username_data)
    new_file.write('\t')
    new_file.write(password_data)
    new_file.write('\t')
    new_file.write(codigo_data)
    new_file.write('\t')
    new_file.write(produto_data)
    new_file.write('\t\n')
    new_file.close()
    print("Nuevo usuario {}".format(username_data))

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    codigo_entry.delete(0, END)
    produto_entry.delete(0,END)



username_label = Label(text='username', bg="#FFEEDD")
username_label.place(x=22, y=60)
password_label = Label(text='password', bg="#FFEEDD")
password_label.place(x=22, y=100)
codigo_label = Label(text="Código do Produto", bg="#FFEEDD")
codigo_label.place(x=22, y =200)
produto_label = Label(text='Produto', bg="#FFEEDD")
produto_label.place(x=22, y=250)

usernames = StringVar()
password = StringVar()
codigo = StringVar()
produto = StringVar()

username_entry = Entry(textvariable=usernames, width="20")
password_entry = Entry(textvariable=password, width="20", show="*")
codigo_entry = Entry(textvariable=codigo, width="20")
produto_entry = Entry(textvariable=produto, width="20")

username_entry.place(x=150, y=60)
password_entry.place(x=150, y=100)
codigo_entry.place(x=150, y=200)
produto_entry.place(x=150, y=250)

# Submit Button
submit_btn = Button(myventana,text = "Submit Info", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)
myventana.mainloop()