import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
t.pensize(4)

for i in range(120)[::-1]:
    hue = i / 120 # use % / x to restrict the colors
    # i * x / 120 speeds up the color change

    # Hue Saturation Value
    rgb = colorsys.hsv_to_rgb(hue, 0.9, 0.9)
    t.pencolor(rgb)

    t.dot(i*3)

# this works as you are only changing the hue and not other values of the colors 

turtle.exitonclick()

# YT short done