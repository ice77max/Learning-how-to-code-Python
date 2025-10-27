import turtle

# turtle setup
t = turtle.Turtle()
t.pensize(4)
t.speed(9)

t.circle(110)
t.penup()
t.goto(0, 110)
t.pendown()

for x in range(3):
    for i in range(3):
        t.fd(100)
        t.left(120)
    t.left(120)



turtle.exitonclick()