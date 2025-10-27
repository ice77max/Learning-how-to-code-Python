from turtle import *

setup(1.0,1.0)

speed(0)
pensize(3)

def leaf(size, angle):
    # fillcolor("white")
    begin_fill()
    circle(size,angle)
    left(180 -angle)
    circle(size,angle)
    # end_fill()

def fancy_leaf(heading):
    for i in range(3,36)[::-1]:
        setheading(heading)
        leaf(i * 8, 100)

# for i in range(1, 15):
#     setheading(45)
#     leaf(150, i * 10)

for i in range(1,9):
    fancy_leaf(i * 45)

hideturtle()

exitonclick()