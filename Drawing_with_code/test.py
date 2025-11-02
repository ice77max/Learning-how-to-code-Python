from turtle import *
import tkinter as tk
from tkinter import ttk
import random
import math

class ChaosPolygon:
    def __init__(self, sides=6, side_size=400, iterations=10000, dot_size=3, show_labels=True):
        self.sides = sides
        self.side_size = side_size
        self.iterations = iterations
        self.dot_size = dot_size
        self.show_labels = show_labels
        self.corners = {}

    def setup_canvas(self):
        setup(1.0, 1.0)
        speed(0)
        pensize(1)
        penup()
        tracer(0)
        self.center_shape()

    def center_shape(self):
        angle = math.radians(360 / self.sides)
        radius = self.side_size / (2 * math.sin(angle / 2))
        teleport(0, -radius)

    def draw_polygon(self):
        self.corners.clear()
        for i in range(self.sides):
            forward(self.side_size)
            pos = position()
            val = (round(pos[0]), round(pos[1]))
            self.corners[i + 1] = val
            if self.show_labels:
                write(f"{i+1}", font=("Arial", 14))
            left(360 / self.sides)

    def pythagorean_step_size(self, current_pos, target_pos):
        Ax, Ay = current_pos
        Cx, Cy = target_pos
        Bx, By = Cx, Ay
        a = abs(Ax - Bx)
        b = abs(By - Cy)
        c = math.sqrt(a**2 + b**2)
        return round((c / 3) * 2)

    def iterate(self):
        for _ in range(self.iterations):
            dice = random.randint(1, self.sides)
            target = self.corners[dice]
            setheading(towards(target))
            current = (round(xcor()), round(ycor()))
            step = self.pythagorean_step_size(current, target)
            forward(step)
            dot(self.dot_size)
        update()

    def run(self):
        self.setup_canvas()
        self.draw_polygon()
        self.iterate()
        exitonclick()

# 🖥️ GUI
def launch_gui():
    def start_drawing():
        clear()
        reset()
        polygon = ChaosPolygon(
            sides=int(sides_var.get()),
            side_size=int(size_var.get()),
            iterations=int(iter_var.get()),
            dot_size=int(dot_var.get()),
            show_labels=label_var.get()
        )
        polygon.run()

    root = tk.Tk()
    root.title("Chaos Polygon Generator")

    ttk.Label(root, text="Sides:").grid(column=0, row=0)
    sides_var = tk.StringVar(value="6")
    ttk.Entry(root, textvariable=sides_var).grid(column=1, row=0)

    ttk.Label(root, text="Side Size:").grid(column=0, row=1)
    size_var = tk.StringVar(value="400")
    ttk.Entry(root, textvariable=size_var).grid(column=1, row=1)

    ttk.Label(root, text="Iterations:").grid(column=0, row=2)
    iter_var = tk.StringVar(value="10000")
    ttk.Entry(root, textvariable=iter_var).grid(column=1, row=2)

    ttk.Label(root, text="Dot Size:").grid(column=0, row=3)
    dot_var = tk.StringVar(value="3")
    ttk.Entry(root, textvariable=dot_var).grid(column=1, row=3)

    label_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(root, text="Show Labels", variable=label_var).grid(column=0, row=4, columnspan=2)

    ttk.Button(root, text="Generate", command=start_drawing).grid(column=0, row=5, columnspan=2)

    root.mainloop()

launch_gui()