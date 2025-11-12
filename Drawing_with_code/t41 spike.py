from turtle import *
from time import sleep
# YouTube/Sierra_wild_3d

# setup
pensize(3)
speed(0)
bgcolor("black")
pencolor("#FF4242")

t = Turtle()
setup(1.0,1.0)

# functions

def shape(a, b, c, d, e, f):
    forward(a)
    left(b)
    forward(c)
    right(d)
    forward(e) # end of the spike
    pekDot(c, f)
    left(d*2)
    forward(e)
    right(d)
    forward(c)

def pekDot(c, f):
    penup()
    right(10)
    forward(c)
    dot(f)
    backward(c)
    left(10)
    pendown()
    
def writeBottomOfTheScreen(i, t):
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.pencolor("#FF4242")
    t.goto(300, -350)
    t.write(f"Angle: {i * 10}", font=("Coper", 20, "normal"))
    
# magic
tracer(1)
hideturtle()

for x in range(15):
    writeBottomOfTheScreen(x, t)
    for i in range(20):
        shape(a=200, b=90, c=40, d=80, e=100, f=20)
        left(x * 10)
    sleep(1)
    clear()
    t.clear()
    
exitonclick() # end script