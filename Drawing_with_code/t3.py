import turtle

t = turtle.Turtle()
t1 = turtle.Turtle()
turtle.bgcolor("#110B13")

penSize = 2
turtle_speed = 0
angle_of_rotation = 5

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

#firts turtle setup
t.pencolor("#FF073A")
t.pensize(penSize)
t.speed(turtle_speed)

#second turtle setup
t1.color("#39FF14")
t1.pensize(penSize)
t1.speed(turtle_speed)

# move second turtle
t1.penup()
t1.goto(0, 100)
t1.pendown()

for i in range(37):
    square(t)
    t.right(angle_of_rotation)
    square(t1)
    t1.left(angle_of_rotation)


turtle.exitonclick()