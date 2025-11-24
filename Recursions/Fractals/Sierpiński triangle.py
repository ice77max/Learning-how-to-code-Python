import turtle as t

t.tracer(100,0) 
t.setworldcoordinates(0,0, 700, 700)
t.hideturtle()
t.pensize(1)

MIN_SIZE = 3

def midpoint(startx, starty, endx, endy):
    # Return x & y in the middle of the four given parameters.
    xDiff = abs(startx - endx)
    yDiff = abs(starty - endy)
    return (min(startx, endx) + (xDiff / 2.0), min(starty, endy) + (yDiff / 2.0))

def isTooSmall (ax, ay, bx, by, cx, cy):
    # Determine if the triangle is to small to draw.
    width = max(ax, bx, cx) - min(ax, bx, cx)
    height = max(ay, by, cy) - min(ay, by, cy)
    return width < MIN_SIZE or height < MIN_SIZE

def drawTriangle(ax, ay, bx, by, cx, cy):
    if isTooSmall(ax, ay, bx, by, cx, cy):
        # BASE CASE
        return
    else:
        # Recursive case that draws the triangle
        t.penup()
        t.goto(ax, ay)
        t.pendown()
        t.goto(bx, by)
        t.goto(cx, cy)
        t.goto(ax, ay)
        t.penup()
        
        # Calculate midpoint between points A, B and C
        mid_ab = midpoint(ax, ay, bx, by)
        mid_bc = midpoint(bx, by, cx, cy)
        mid_ca = midpoint(cx, cy, ax, ay)

        # Draw the three inner triangles
        drawTriangle(ax, ay, mid_ab[0], mid_ab[1], mid_ca[0], mid_ca[1])
        drawTriangle(mid_ab[0], mid_ab[1], bx, by, mid_bc[0], mid_bc[1])
        drawTriangle(mid_ca[0], mid_ca[1], mid_bc[0], mid_bc[1], cx, cy)
        return
    
# Draw an equilateral Sierpinski Triangle
    
# drawTriangle(50, 50, 350, 650, 650, 50)
    
drawTriangle(80, 80, 150, 650, 650, 150)

t.exitonclick()

