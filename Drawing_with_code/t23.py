import turtle as t

# setup
t.pensize(3)
t.speed(0)
t.tracer(2)

def pettle(size):
    t.fd(size)
    t.circle(35, 180)
    t.fd(size)

def flower(size, angle):
    pettle(size)
    t.left(angle)

for i in range(45):
    flower(50, 3)
    flower(100, 3)
    flower(100, 5)
    flower(150, 5)
    flower(200, 5)


t.exitonclick()