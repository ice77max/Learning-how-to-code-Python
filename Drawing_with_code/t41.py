from turtle import *
import random

setup(1.0,1.0)
speed(0)

# hexagon
corners = {}
pensize(1)
teleport(-200,-250)
penup()

for i in range(6):
    forward(400)
    pos = position()
    val = (round(pos[0]),round(pos[1]))
    corners[i + 1] = val
    write(f"{i+1}", font=("Arial", 14))
    left(360/6)


for i in range(100):
    dice = random.randrange(1,7)
    where_to_go = corners[dice]
    x = round(where_to_go[0])
    y = round(where_to_go[1])
    setheading(towards(x,y))

# TODO use Pythagorean theorem to draw the dot
    current_pos = position()

    dot(10)





exitonclick()