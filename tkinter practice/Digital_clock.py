from tkinter import Label, Tk, mainloop
from time import strftime

window = Tk()
window.title("Digital Clock")
window.config(background="dark green")

# Time
def time():
    myTime = strftime("%H:%M:%S %p")
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(window, font= ("Arial", 48, "bold"),
              background="dark green",
              foreground="white")
clock.pack(anchor="center")
time()

# displaying day
myDay = strftime("%A")
day = Label(window, font= ("Arial", 48, "bold"),
              background="dark green",
              foreground="white")
day.pack(anchor="center")

day.config(text=myDay)

# displaying date
myDate = strftime("%d %B %Y")
date = Label(window, font= ("Arial", 48, "bold"),
              background="dark green",
              foreground="white")
date.pack(anchor="center")

date.config(text=myDate)

mainloop()