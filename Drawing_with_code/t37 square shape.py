from turtle import *
# youtube.com/@sierra_wild.3d

# setup(1.0,1.0)
speed(0)

def sqr(x,y, thickness):
    pensize(thickness)
    forward(x)
    left(90)
    pensize(thickness * 2)
    forward(y)
    left(90)
    forward(x)
    left(90)
    pensize(thickness)
    forward(y)

for i in range(8):
    sqr(100, 100, 4)
    left(45)

exitonclick()