from turtle import *

setup(1.0,1.0)

speed(0)
pensize(3)

def pie_slice(size):
    forward(size)
    left(90)
    dot(15)
    circle(size,90)
    left(90)
    dot(15)
    forward(size)

def sign():
    for i in range(6):
        if i % 2 == 0:
            pie_slice(100)
        else:
            pie_slice(120)
        left(150)

x = 200
sign()
teleport(-x,-x)
sign()
teleport(-x,x)
sign()
teleport(x,-x)
sign()
teleport(x,x)
sign()


exitonclick()