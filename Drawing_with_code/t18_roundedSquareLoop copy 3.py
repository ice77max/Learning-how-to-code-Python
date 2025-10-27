import turtle

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.penup()
t.goto(250, -150)
t.pendown()
t.pencolor("light blue")


def one_side(fd):
    for i_ in range(1):
        t.circle(20, extent=88)
        t.fd(fd)


# mgic

for j in range(120):
    one_side(50)
    one_side(150)
    one_side(50)
    one_side(150)

    t.left(5)
    
    




turtle.exitonclick() # end



