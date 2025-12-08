import turtle
import os

# make sure the folder exists
os.makedirs("Chaos game/img", exist_ok=True)

turtle.forward(100)
ts = turtle.getscreen()

# save to the img folder
ts.getcanvas().postscript(file="Chaos game/img/duck.eps")