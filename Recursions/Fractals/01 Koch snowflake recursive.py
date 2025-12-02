from turtle import *

setup(1.0,1.0) 

speed(0)
pensize(2)

# tracer(0) # draw instantly

def koch(length,step):
    if step == 0:
        fd(length)
    else:
        length = length / 3
        step = step - 1
        koch(length, step)
        right(60)
        koch(length,step)
        left(120)
        koch(length,step)
        right(60)
        koch(length,step)

teleport(-200,-200)

x = 3 #change this for different overall shape

fillcolor("#C4C4C4")
begin_fill()
for i in range(x):
    koch(500, 4)
    left(360/x)
end_fill()
hideturtle()

update()
exitonclick()