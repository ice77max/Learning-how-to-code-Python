# https://youtu.be/epDKamC-V-8?si=DhO09GAMu_5vuudt
# I finished on 12:37

import tkinter as tk

root = tk.Tk()
root.title("My first GUI")

def on_click():
    print("Hello, World!")


lbl = tk.Label(root, text="Label 1")
lbl.grid(row = 0, column=0)

btn = tk.Button(root, text="Button 1", command=on_click)
btn.grid(row=0, column=1)


root.mainloop()