import turtle

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("#F05BDF")

# mgic

for j in range(74):
    for i in range(4):
        t.circle(20, extent=90)
        t.fd(70)
    t.left(5)
t.hideturtle()   

turtle.exitonclick() # end



