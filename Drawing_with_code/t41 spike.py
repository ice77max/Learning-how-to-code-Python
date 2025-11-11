from turtle import *
# YouTube/Sierra_wild_3d

# setup
pensize(3)
speed(0)
bgcolor("black")
pencolor("#0AF7FF")

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

for i in range(13):
    shape(a=200, b=90, c=40, d=80, e=100, f=20)
    left(120)

exitonclick() # end script