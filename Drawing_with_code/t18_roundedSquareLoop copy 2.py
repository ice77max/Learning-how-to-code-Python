import turtle

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.penup()
t.goto(50, -150)
t.pendown()
t.pencolor("light blue")

# mgic

for j in range(50):
    for i in range(2):
        t.circle(20, extent=88)
        t.fd(70)
        for i in range(2):
            t.circle(20, extent=88)
            t.fd(150)
    t.left(5)
    
    




turtle.exitonclick() # end



