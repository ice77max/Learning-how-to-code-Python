from turtle import *

tracer(30,0)
setworldcoordinates(0, 0, 700, 700)
hideturtle()

MIN_SIZE = 6 # change to increase or decrease amount of recursions
DRAW_SOLID = True
SET_COLOR = "#CD80F7"
BG_COLOR = "#8EF87E"

bgcolor(BG_COLOR)

def isTooSmall(width, height):
    # determine if the shape is to small to draw
    return width < MIN_SIZE or height < MIN_SIZE

def drawCarpet (x, y, w, h):
    # x and y are lower left corner of the carpet
    
    #move the pen to the position
    penup()
    goto(x,y)

    # draw outer rectangle
    pendown()
    if DRAW_SOLID:
        fillcolor(SET_COLOR)
        begin_fill()
    goto(x, y + h)
    goto(x + w, y + h)
    goto(x + w, y)
    goto(x, y)
    if DRAW_SOLID:
        end_fill()
    penup()
    
    # draw inner rec
    drawInnerRec(x, y, w, h)
    
def drawInnerRec(x, y, w, h):
    if isTooSmall(w, h):
        # base case
        return
    else:
        # recursive case
        
        oneThirdWidth = w / 3
        oneThirdHeight = h / 3
        twoThirdsWidth = 2 * (w / 3)
        twoThirdsHeight = 2 * (h / 3)

        # move into position
        penup()
        goto(x + oneThirdWidth, y + oneThirdHeight)

        # draw the inner rec
        if DRAW_SOLID:
            fillcolor(BG_COLOR)
            begin_fill()
        pendown()
        goto(x + oneThirdWidth, y + twoThirdsHeight)
        goto(x + twoThirdsWidth, y + twoThirdsHeight)
        goto(x + twoThirdsWidth, y + oneThirdHeight)
        goto(x + oneThirdWidth, y + oneThirdHeight)
        penup()
        if DRAW_SOLID:
            end_fill()
            
        # Draw the inner rectangles across the top
        drawInnerRec(x, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)
        drawInnerRec(x + oneThirdWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)
        drawInnerRec(x + twoThirdsWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)

        # draw inner rec across the middle
        drawInnerRec(x, y + oneThirdHeight, oneThirdWidth, oneThirdHeight)
        drawInnerRec(x + twoThirdsWidth, y + oneThirdHeight, oneThirdWidth, oneThirdHeight)

        # draw inner rec across the bottom
        drawInnerRec(x, y, oneThirdWidth, oneThirdHeight)
        drawInnerRec(x + oneThirdWidth, y, oneThirdWidth, oneThirdHeight)
        drawInnerRec(x + twoThirdsWidth, y, oneThirdWidth, oneThirdHeight)

drawCarpet(50, 50, 600, 600)

exitonclick()