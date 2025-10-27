import turtle
import colorsys

# turtle setup
t = turtle.Turtle()
t.speed(10)
t.pensize(2)

screen = turtle.Screen()
screen.setup(1.0, 1.0)

# turtle move
t.penup()
t.goto(0, -300)
t.pendown()

# magic

for i in range(23)[::-1]:
    hue = i / 23
    rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
    t.fillcolor(rgb)
    
    t.begin_fill()
    t.circle(i * 15)
    t.end_fill()

# end
turtle.exitonclick()

# YT short done