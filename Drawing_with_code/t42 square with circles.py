from turtle import *
# youtube.com/@sierra_wild_3d
# setup

setup(1.0,1.0)
bgcolor("black")
pencolor("white")
pensize(3)
speed(0)

# functions

def square(x,y, c):
    forward(x)
    left(90)
    forward(y)
    cornerCircle(c)
    left(90)
    forward(x)
    left(90)
    forward(y)
    left(90)

def cornerCircle(c):
    right(90+45)
    circle(c)
    dotInTheMidleOfCircle(c)
    left(45)

def dotInTheMidleOfCircle(c):
    left(90)
    penup()
    forward(c)
    dot(c*0.7,"white")
    backward(c)
    pendown()

# magic

for i in range(36):
    square(200, 100, 20)
    left(10)
dot(25,"black")
hideturtle()


# end
exitonclick()