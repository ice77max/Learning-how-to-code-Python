from turtle import *

setup(1.0,1.0)
hideturtle()
speed(0)
pencolor("#232323")
tracer(2)

for i in range(1000):
    penup()
    circle(i/3,10)
    dot(i * 0.03)

exitonclick()