import turtle

# turtle setup
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("#000000")

colors = ["#20d2ff", "#FF0000", "#6cfe2e"]

for i in range(500):
    t.pencolor(colors[i % len(colors)])
    t.fd(i*2)
    t.left(119)
    


turtle.exitonclick()