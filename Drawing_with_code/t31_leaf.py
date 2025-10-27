import turtle

# setup
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(10)
t.pensize(4)
t.pencolor("white")

colors = ["#3665FF", "#856AE6"]

# functions

def leaf(i):
    t.fillcolor(colors[int(i%3 / 2)])
    t.begin_fill()
    t.circle(100, 100)
    t.left(80)
    t.circle(100, 100)
    t.end_fill()

def dots():
    t.speed(0) 
    t.penup()

    t.circle(100, 100)
    t.left(80)
    t.dot(25, "#FF6C6C")
    t.circle(100, 100)


# magic

for i in range(9):
    leaf(i)
for i in range(9):
    dots()
t.dot(40,"#FFFC33")
t.dot(20,"#282824")
t.hideturtle()

turtle.exitonclick() # end