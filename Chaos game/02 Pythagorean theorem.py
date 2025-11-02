from turtle import *
import math

# parameters
Ax = 0
Ay = 10

Cx = 300
Cy = 300

Bx = Cx
By = Ay

# Calculate C of a triangle using Pythagorean theorem

a = abs(Ax - Bx)
b = abs(By - Cy)
c = abs(a**2 + b**2) 
c = round(math.sqrt(c))

print(f"{a=}", f"{b=}", f"{c=}")

# draw a triangle
teleport(Ax, Ay)
setheading(0)
forward(a)
left(90)
forward(b)

# draw c
teleport(Ax, Ay)
setheading(towards(Cx,Cy))
forward((c / 3) * 2)


exitonclick()