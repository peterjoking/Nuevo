import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Mi reloj Digital")
myClock = tk.Label()
myClock ['text']= '22:22:00'
myClock.pack()
myClock['font'] = 'Tahoma 150 bold'


strftime('%H:%M:%S')

def tic():
    myClock['text'] = strftime('%H:%M:%S')

tic()

def tac():
    tic()
    myClock.after(1000, tac)
tac()

myClock['bg']='black'
myClock['fg']='#00FF00'

root.mainloop()