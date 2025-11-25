from turtle import *

tracer(50, 0)
setworldcoordinates(0, 0, 700, 700)
hideturtle()
pensize(2)

def drawKochCurve(startPosition, startHeading, length):
    if length < 1:
        # BASE CASE
        return
    else:
        # recursive case
        # move to the start position
        recursiveArgs = []
        penup()
        goto(startPosition)
        setheading(startHeading)
        recursiveArgs.append({"position": position(),
                              "heading": heading()})
        
        # erase the middle third
        fd(length / 3)
        pencolor("white")
        pendown()
        forward(length / 3)

        # draw a bump
        backward(length / 3)
        left(60)
        recursiveArgs.append({"position": position(),
                              "heading": heading()})
        pencolor("black")
        forward(length / 3)
        right(120)
        recursiveArgs.append({"position": position(),
                              "heading": heading()})
        forward(length / 3)
        left(60)
        recursiveArgs.append({"position": position(),
                              "heading": heading()})

        for i in range(4):
            drawKochCurve(recursiveArgs[i]["position"],
                          recursiveArgs[i]["heading"],
                          length / 3)
        return
    
def drawKochSnowflake(startPosition, startHeading, length):
    # a koch snowflake is three koch curves in a triangle
    
    # move to the start position
    penup()
    goto(startPosition)
    setheading(startHeading)

    for i in range(3):
        # record the starting position and heading
        curveStartingPosition = position()
        curveStartingHeading = heading()
        drawKochCurve(curveStartingPosition,
                      curveStartingHeading, length)

        # move back to the start position for this side
        penup()
        goto(curveStartingPosition)
        setheading(curveStartingHeading)

        # move to the start position of the next side
        forward(length)
        right(120)

drawKochSnowflake((100, 500), 0, 500)
exitonclick()