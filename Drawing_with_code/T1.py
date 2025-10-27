import turtle

# setup
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
colors = ["royal blue", "dodger blue"]

# magic

for n in range(400):
    t.forward(n + 1)
    t.right(89)
    t.pencolor(colors[n % 2])
    
turtle.exitonclick() # end