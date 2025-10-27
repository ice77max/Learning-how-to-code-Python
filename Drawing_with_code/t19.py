import turtle as t
t.speed(0)
t.pensize(2)
blue = 0
t.bgcolor("black")

# magic

for _ in range(72):
    t.pencolor(0.9,0.1,blue)
    t.circle(100)
    t.left(5)
    if blue <= 1:
        blue += 0.05

t.exitonclick()