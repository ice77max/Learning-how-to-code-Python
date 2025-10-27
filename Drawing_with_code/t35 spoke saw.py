from turtle import *
import colorsys

setup(1.0,1.0)
bgcolor("black")
speed(0)

def sqr(x,y,lineSize):
    for _ in range(2):
        pensize(lineSize)
        forward(x)
        left(90)
        pensize(lineSize*3)
        forward(y)
        left(90)

x = 10
for i in range(int(360/x)):
    hue = i / (360/x)
    rgb = colorsys.hsv_to_rgb(hue,0.8,0.8)
    pencolor(rgb)
    sqr(200,100, 3)
    left(x)
hideturtle()

exitonclick()