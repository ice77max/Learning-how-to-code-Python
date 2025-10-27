from turtle import *

setup(1.0,1.0)

speed(0)
pencolor("black")
pensize(2)

# 
font_data = ("Arial", 10, "normal")

# functions
def axis(distance):
    back(distance)
    forward(distance*2)
    shapesize(2,2)
    stamp()

def numbers(numbers, distanceBetweenNumbers):
    penup()
    for i in range(numbers + 1):
        write(i, font=font_data)
        forward(distanceBetweenNumbers)

#horizontal line
axis(500)

# vertical line
teleport(0,0)
left(90)
axis(400)

# numbers
teleport(5,0)
numbers(10,35)

teleport(5,0)
right(90)
numbers(10,45)


exitonclick()