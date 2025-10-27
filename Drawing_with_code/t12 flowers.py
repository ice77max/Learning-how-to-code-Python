import turtle
import time
import colors
import random

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("black")
screen = turtle.Screen()
screen.setup(width= 1.0, height= 1.0, startx=None, starty=None)

# functions

def zero_out_turtle():
    t.penup
    t.goto(0,0)
    t.pendown()
    t.clear()
    t.setheading(0)

def flower(repetitions, angle):
    t.pencolor(random.choice(colors.extended_colors))
    for i in range(repetitions):
        t.fd(i)
        t.left(90)
        t.fd(i)
        t.left(90)
        t.fd(i / 2)
        t.right(angle)

# magic
time.sleep(2)
for i in range(1, 20):
    flower(200, i * 11)
    time.sleep(1)
    zero_out_turtle()

# patterns I like

# flower(150, 150)
# time.sleep(2)
# zero_out_turtle()
# flower(250, 100)

turtle.exitonclick() # end