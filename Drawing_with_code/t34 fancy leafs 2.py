from turtle import *

setup(1.0,1.0)

speed(0)
pensize(3)

def leaf(size, angle):
    begin_fill()
    circle(size,angle)
    left(180 -angle)
    circle(size,angle)
    
def fancy_leaf(heading):
    for i in range(15, 25):
        setheading(heading)
        leaf(150, i * 5)

for i in range(8):
    fancy_leaf(i * 45)

hideturtle()

exitonclick()