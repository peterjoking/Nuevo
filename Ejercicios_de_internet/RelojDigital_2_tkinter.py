import time
import tkinter as tk
import datetime
from datetime import date
class Digitalclock():
    def __init__(self):

        self.mywindows= tk.Tk()
        self.mywindows.geometry('600x300')
        self.mywindows.resizable(0,0)
        self.mywindows.title('Mi ventana Reloj Digital')
        self.mywindows.config(background='#000000')
        self.current_time_label = tk.Label(text="", font=('Tahoma', 44), fg='#00ff00', bg='#000000', pady=10, padx=10)
        self.created_by_label = tk.Label(text="Pedro Burlando", font=('Tahoma', 9), fg='#ffffff', bg='#000000', pady=3,padx=3)
        self.week_day= tk.Label(text="", font=('Tahoma', 12), fg='#ffffff', bg='#449a66', pady=10, padx=10)
        self.current_time_label.place(x=175, y=50)
        self.week_day.place(x=210, y=160)
        self.created_by_label.place(x=260, y=220)
        self.update_clock()
        self.get_date()

        self.mywindows.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=now)
        self.mywindows.after(1000, self.update_clock)

    def get_date(self):
        # Get Week Day
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime("%A")

        # Get Current date
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        self.week_day.configure(text=d1 + ' | ' + week_day)

main= Digitalclock()