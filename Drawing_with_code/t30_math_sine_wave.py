import turtle
import math

# setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1.0, 1.0)

t = turtle.Turtle()
t.pensize(3)
t.pencolor("white")
t.speed(0)

# magic
t.penup()
for i in range(800):
    y = math.sin(math.radians(i*5)) * 50
    t.goto(i - 300, y)
    t.pendown()

# exit
screen.exitonclick()

# YT Short done