import turtle

# setup
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(7)
t.pensize(4)
t.pencolor("black")



# functions

def leaf(size):
    t.circle(size, 100)
    t.left(80)
    t.circle(size, 100)
    

# magic

leaf(120)
leaf(100)
leaf(100)
leaf(120)

t.left(75)
t.circle(200, 50)
t.dot(20)

t.teleport(0,0)

t.right(60)
t.circle(-185, 50)
t.dot(20)

turtle.exitonclick() # end