import time
import tkinter as tk

mywindow = tk.Tk()
mywindow.geometry("400x180")
mywindow.resizable(False,False)
mywindow.title("Creating a Digital Clock - Python + Tkinter")
mywindow.config(background='#1f2f3f')
current_time_label = tk.Label(text=time.strftime('%H:%M:%S'), font=('Tahoma', 44), fg='#ffffff', bg='#443355', pady=10, padx=10)
current_time_label.place(x=70, y=40)
#print(current_time_label['text'])

def update_clock():
    time_now = time.strftime('%H:%M:%S')
    if current_time_label['text'] != time_now:
        current_time_label['text'] = time_now
        #print(current_time_label['text'])
    mywindow.after(1000, update_clock)

update_clock()
mywindow.mainloop()