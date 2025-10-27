import turtle

t = turtle.Turtle()
t.speed(9)
top_x = 115
mid_x = 145

top_y = 250
mid_y = 100

t.pensize(5)

t.goto(top_x, top_y)
t.goto(-mid_x, mid_y)
t.goto(mid_x, mid_y)
t.goto(-top_x, top_y)
t.goto(0, 0)

t.pensize(10)
t.circle(150)


turtle.done()