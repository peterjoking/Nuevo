import tkinter as tk
lives = 3
root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width=800, height=400, bg='#aaaaff')
frame.pack()
canvas.pack()
root.title('Hello, Peter!')
root.mainloop()


from tkinter import Tk
pedro = Tk()
pedro.title('Hello, world!')
frame1 = tk.Frame(pedro)
canvas1 = tk.Canvas(frame1, width=600, height=600, bg='#ffaaff')
frame1.pack()
canvas1.pack()
pedro.mainloop()



