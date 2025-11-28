from turtle import *

tracer(30,0)  # full control over updates
setworldcoordinates(0, 0, 700, 700)
hideturtle()

MIN_SIZE = 6
DRAW_SOLID = True
SET_COLOR = "#11EFFF"
BG_COLOR = "#F7A117"

bgcolor(BG_COLOR)

def isTooSmall(width, height):
    return width < MIN_SIZE or height < MIN_SIZE

def drawRect(x, y, w, h, color):
    penup()
    goto(x,y)
    pendown()
    fillcolor(color)
    begin_fill()
    goto(x, y + h)
    goto(x + w, y + h)
    goto(x + w, y)
    goto(x, y)
    end_fill()
    penup()

def drawCarpetBreadth(x, y, w, h):
    # queue of rectangles to process
    queue = [(x, y, w, h)]
    
    while queue:
        next_level = []
        for (x, y, w, h) in queue:
            if isTooSmall(w, h):
                continue
            
            # draw outer rectangle
            drawRect(x, y, w, h, SET_COLOR)
            
            # carve out the inner hole
            oneThirdWidth = w / 3
            oneThirdHeight = h / 3
            twoThirdsWidth = 2 * oneThirdWidth
            twoThirdsHeight = 2 * oneThirdHeight
            
            drawRect(x + oneThirdWidth, y + oneThirdHeight,
                     oneThirdWidth, oneThirdHeight, BG_COLOR)
            
            # enqueue the 8 surrounding rectangles for next level
            next_level.extend([
                (x, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight),
                (x + oneThirdWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight),
                (x + twoThirdsWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight),
                
                (x, y + oneThirdHeight, oneThirdWidth, oneThirdHeight),
                (x + twoThirdsWidth, y + oneThirdHeight, oneThirdWidth, oneThirdHeight),
                
                (x, y, oneThirdWidth, oneThirdHeight),
                (x + oneThirdWidth, y, oneThirdWidth, oneThirdHeight),
                (x + twoThirdsWidth, y, oneThirdWidth, oneThirdHeight),
            ])
        
        # move to next level
        queue = next_level
        update()  # refresh screen after each level

drawCarpetBreadth(50, 50, 600, 600)
exitonclick()