import turtle
import random

# turtle setup
t = turtle.Turtle()

t.pencolor("black")
t.pensize(3)
t.speed(0)

# here is where the magic hapens
for i in range(300):
    t.pencolor(0,0,i/300)
    t.goto(random.randint(-300, 300), random.randint(-300, 300))

# exit
turtle.exitonclick()