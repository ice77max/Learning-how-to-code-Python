from turtle import *
import random
import math

# of set of
setup(1.0,1.0)

speed(0)
pensize(1)

penup()

# variables 
corners = {}

# TODO Play with those numbers
# change those numbers to get different shapes
sides = 6
side_size = 400
# of set so the shape is in the center of the screen
teleport(-100,-350)

no_of_iterations = 100000

# functions

def draw_numbers(sides, side_size):
    for i in range(sides):
        forward(side_size)
        pos = position()
        val = (round(pos[0]),round(pos[1]))
        corners[i + 1] = val # fills the dictionary with positions of the corners
        write(f"{i+1}", font=("Arial", 14))
        left(360/sides)

def pythagorean_triangle(current_pos, where_to_go):
    # parameters
    Ax = current_pos[0]
    Ay = current_pos[1]

    Cx = where_to_go[0]
    Cy = where_to_go[1]

    Bx = Cx
    By = Ay

    # Calculate C of a triangle using Pythagorean theorem
    a = abs(Ax - Bx)
    b = abs(By - Cy)
    c = abs(a**2 + b**2) 
    c = round(math.sqrt(c))
    return round((c / 3) * 2)

# hexagon (or any other shape)
draw_numbers(sides, side_size)

tracer(0)
# koch snowflake
for i in range(no_of_iterations):
    dice = random.randrange(1,sides + 1)
    where_to_go = corners[dice]
    x = round(where_to_go[0])
    y = round(where_to_go[1])
    setheading(towards(x,y))

    current_pos = position()
    current_pos_rounded = (round(current_pos[0]), round(current_pos[1]))
    
    forward(pythagorean_triangle(current_pos_rounded, where_to_go))

    dot(3)





exitonclick()