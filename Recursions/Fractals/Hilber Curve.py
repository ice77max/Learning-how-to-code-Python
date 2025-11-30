from turtle import *

# setup
tracer(5,0)
setworldcoordinates(0,0, 700, 700)
hideturtle()

LINE_LENGTH = 5
ANGLE = 90
LEVELS = 6
DRAW_SOLID = True
setheading(0) # change to start at an angle

# functions

def hilbertCurveQuadrant(level, angle):
    if level == 0:
        # Base case
        return
    else:
        # recursive case
        right(angle)
        hilbertCurveQuadrant(level - 1, -angle)
        forward(LINE_LENGTH)
        left(angle)
        hilbertCurveQuadrant(level - 1, angle)
        forward(LINE_LENGTH)
        hilbertCurveQuadrant(level - 1, angle)
        left(angle)
        forward(LINE_LENGTH)
        hilbertCurveQuadrant(level - 1, -angle)
        right(angle)
        return
def hilbertCurve(startingPosition):
    penup()
    goto(startingPosition)
    pendown()
    if DRAW_SOLID:
        begin_fill()

    hilbertCurveQuadrant(LEVELS, ANGLE)
    forward(LINE_LENGTH)

    hilbertCurveQuadrant(LEVELS, ANGLE)
    left(ANGLE)
    forward(LINE_LENGTH)
    left(ANGLE)

    hilbertCurveQuadrant(LEVELS, ANGLE)
    forward(LINE_LENGTH)

    hilbertCurveQuadrant(LEVELS, ANGLE)

    left(ANGLE)
    forward(LINE_LENGTH)
    left(ANGLE)        
    if DRAW_SOLID:
        end_fill()

hilbertCurve((30, 350))


exitonclick()