# import tkinter as tk
# lives = 3
# root = tk.Tk()
# frame = tk.Frame(root)
# canvas = tk.Canvas(frame, width=600, height=400, bg='#aaaaff')
# frame.pack()
# canvas.pack()
# root.title('Hello, Pong!')
# root.mainloop()

import tkinter as tk
class Game (tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 600
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello, Pong!')
    game = Game(root)
    game.mainloop()
