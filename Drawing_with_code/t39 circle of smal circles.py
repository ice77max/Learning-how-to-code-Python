from turtle import *
import colorsys
# youtube.com/@sierra_wild.3d
setup(1.0,1.0)

speed(0)
pensize(3)
bgcolor("black")

def circle_s(size, range_no, steps, sizeOfSmallC):
    for i in range(range_no):
        h = i / range_no
        rgb = colorsys.hsv_to_rgb(h,0.8, 0.8)
        pencolor(rgb)
        penup()
        circle(size,steps)
        pendown()
        circle(sizeOfSmallC)
        penup()

tracer(3)
teleport(0, -150)
for i in range(15*3):
    circle_s(170 + (i * 10), 36, 10, 9)
    circle(170 + (i * 10), 5 + i * 0.1)

    right(90)
    forward(10)
    left(90)


exitonclick()