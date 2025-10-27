import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("#00FFFF")
turtle.bgcolor("black")

def square(size):
    for i in range(4):
        t.fd(size)
        t.right(90)

for i in range(10):
    square(100)
    t.right(10)

t.penup()
t.goto(0,30)
t.pendown()
t.setheading(180)

for i in range(10):
    square(100)
    t.right(10)

t.hideturtle()
turtle.done()