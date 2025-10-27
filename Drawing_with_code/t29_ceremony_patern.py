import turtle

# setup
t1 = turtle.Turtle()
t2 = turtle.Turtle() # turtle I used for debuging

screen = turtle.Screen()
screen.setup(1.0, 1.0)
turtle.bgcolor("black")

color = "#FBAA4D"
t1.speed(0)
t1.pensize(6)
t1.pencolor(color)
t1.fillcolor(color)
t1.hideturtle()

# function

def square(size):
    t1.left(90)
    t1.fd(size)
    t1.begin_fill()
    for _ in range(4):
        t1.fd(size)
        t1.left(90)
    t1.end_fill()
    t1.right(90)
    t1.fd(size)
    t1.left(90)

def patern(sqr_size, horizontal_size, vertical_size):
    y = int(((vertical_size / 2) + sqr_size) * -1)
    middle = t1.position()
    t1.teleport(int(middle[0]),y)
    for _ in range(2):
        t1.fd(int(horizontal_size/2))
        square(sqr_size)
        t1.fd(vertical_size)
        square(sqr_size)
        t1.fd(int(horizontal_size/2))
    t1.teleport(int(middle[0]),int(middle[1]))
# magic

x = 60
for i in range(1,10):
    patern(i + 10, i * x, i * x)
    
# exit
turtle.exitonclick()