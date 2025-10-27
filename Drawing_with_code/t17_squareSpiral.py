import turtle as t

t.speed(0)
t.pensize(3)

def spiral_square():
    for i in range(200):
        t.fd(i * 3)
        t.left(90)
def zero_out():
    t.penup()
    t.goto(0,0)
    t.pendown()

spiral_square()
zero_out()
t.pencolor("white")
t.right(45)
spiral_square()
t.hideturtle()

t.exitonclick()