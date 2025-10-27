from turtle import *

setup(1.0,1.0)
hideturtle()
speed(0)
pencolor("#232323")
tracer(2)

for i in range(500, 10000):
    penup()
    circle(i/2,10 + i*3.14 )
    dot(3)

exitonclick()