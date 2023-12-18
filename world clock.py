import tkinter as tk
from time import strftime, time, gmtime

class WorldClock:
    def __init__(self, master, city, timezone_offset):
        self.master = master
        self.city = city
        self.timezone_offset = timezone_offset

        self.label = tk.Label(master, font=('calibri', 12, 'bold'))
        self.label.pack(padx=5, pady=5)

        self.update_time()

    def update_time(self):
        current_time = time()
        shifted_time = current_time + (self.timezone_offset * 3600)
        time_string = strftime('%H:%M:%S %p', gmtime(shifted_time))
        self.label.config(text=f"{self.city}: {time_string}")
        self.master.after(1000, self.update_time)


root = tk.Tk()
root.title("World Clocks")
cities = [("New York", -5), ("Tokyo", 9), ("London", 0), ("Sydney", 11)]
clocks = [WorldClock(root, city, offset) for city, offset in cities]
root.mainloop()