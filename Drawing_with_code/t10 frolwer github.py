from turtle import *

# day 15 from github atlemgw/turtlegraphics

for i in range(420):
    for j in range(4):
        forward(0.2 * i * j)
        left(91)
        hideturtle()
        pensize(3)
        speed(0)
    left(73 * 15 / 100 + 15)