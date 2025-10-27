import turtle

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(4)
t.pencolor("white")
turtle.bgcolor("black")

#magic

r = 10 # radius
for i in range(30):
    t.circle(r * i)
    t.penup()
    t.sety((i * r) *-1)
    t.pendown()

turtle.exitonclick() # exit