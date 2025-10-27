import turtle as t

# setup

t.pensize(2)
t.speed(8)

t.tracer(20)
h = 0.3

for i in range(175):
    c = "#F0B3B3"
    h += 0.004
    t.color(c)
    t.circle(180 - i, 80)
    t.left(80)
    t.circle(180 - i, 80)
    t.left(18)
    

t.exitonclick()