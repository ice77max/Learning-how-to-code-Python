import turtle 
import time
import random

#setup
t = turtle.Turtle()
t.pensize(3)
t.speed(0)
turtle.tracer(1)
turtle.bgcolor("black")
screen = turtle.Screen()
screen.setup(1.0,1.0)

def wieloscian (sides):
    for j in range(sides):
        # t.pencolor(random.random(), random.random(), random.random()) # random color for each patern
        for i in range(sides):
            t.forward(100 - sides * 2)
            t.left(360 / sides)
        t.left(360 / sides)

# magic
for i in range(3, 25):
    t.pencolor((random.randrange(30,100))/100, (random.randrange(30,100))/100, (random.randrange(30,100))/100) # random color for whole drawing
    wieloscian(i)
    turtle.update()
    time.sleep(1) 
    t.goto(0,0)  
    t.clear()   

turtle.exitonclick() # end