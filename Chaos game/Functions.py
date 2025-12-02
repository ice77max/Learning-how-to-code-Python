from turtle import *
import random
import math
import colorsys

# setup
setup(1.0,1.0)

speed(0)
pensize(1)

penup()


# TODO Play with those numbers
# change those numbers to get different shapes
sides = 16
side_size = 2000 / sides
ratio = 0.707
''' Perfect ratios according to wikipedia
Triangle    3   0.5
Carpet      4   2/3 but I find better results going bit above 0.5
Pentagon    5   0.618(golden ratio related)
Hexagon     6   0.667(2/3)
Octagon     8   0.707
'''

no_of_iterations = 82 * 1000


tracer(50, 0) # speed

# TODO Randomly generate initial points  
# TODO 3rd turtle writing how many sides we have and current ratio. Make it as a 3rd turtle so I can draw it once and not redraw it each iteration
turtle_2_writingIterations = Turtle()
turtle_3_writingLabels = Turtle()

# Functions

shapeNames = {
    "3": "Trigon, Sierpiński triangle",
    "4": "Tetragon, Sierpiński carpet",
    "5": "Pentagon",
    "6": "Hexagon",
    "7": "Heptagon",
    "8": "Octagon",
    "9": "Nonagon",
    "10": "Decagon",
    "11": "Hendecagon",
    "12": "Dodecagon",
    "13": "Tridecagon",
    "14": "Tetradecagon",
    "15": "Pendedecagon",
    "16": "Hexdecagpn",
    "17": "Heptdecagon",
    "18": "Octdecagon",
    "19": "Enneadecagon",
    "20": "Icosagon",
    "n-gon": "n-gon",
    
}

# counter

def writingLabels():
    turtle_3_writingLabels.hideturtle()
    turtle_3_writingLabels.penup()
    turtle_3_writingLabels.pencolor("#363636")
    offsetOfCenter = offset()
    additionalOffset = 1.2
    turtle_3_writingLabels.teleport(-offsetOfCenter * additionalOffset * 1.3, -offsetOfCenter * additionalOffset)
    
    # writing labels
    turtle_3_writingLabels.write("Number of \niterations: ", move= False, font=("Arial", 30, "normal"))
    # grab position and offset turtle on Y axis 
    position = turtle_3_writingLabels.position()
    offsetY = -80
    turtle_3_writingLabels.sety(position[1] + offsetY)
    turtle_3_writingLabels.write(f"Ratio: {ratio}", move= False, font=("Arial", 30, "normal"))
    turtle_3_writingLabels.sety(position[1] + offsetY * 2)
    turtle_3_writingLabels.write(f"Number of sides: {sides}", move= False, font=("Arial", 30, "normal"))
    
    turtle_3_writingLabels.sety(position[1] + offsetY * 3)
    if sides <21:
        turtle_3_writingLabels.write(shapeNames[str(sides)], move= False, font=("Arial", 30, "normal"))
    else:
        turtle_3_writingLabels.write(shapeNames["n-gon"], move= False, font=("Arial", 30, "normal"))
        
    
    
def writeIterations(loop_count):
    """
    Writes the current iteration count on the screen using turtle_2_writingIterations.

    Parameters:
        loop_count (int): The current iteration number to display.
    """
    turtle_2_writingIterations.hideturtle()
    offsetOfCenter = offset()
    additionalOffset = 1.2
    turtle_2_writingIterations.teleport(-offsetOfCenter * additionalOffset * 1.3 + 200, -offsetOfCenter * additionalOffset)
    
    if loop_count % 100 == 0:
        turtle_2_writingIterations.clear()
        turtle_2_writingIterations.write(loop_count, move= False, font=("Arial", 30, "normal"))
        # drawScoringUnderline(5, loop_count/100) # draws a growing line under iterations
    turtle_2_writingIterations.hideturtle()
    offsetOfCenter = offset()
    additionalOffset = 1.2
    turtle_2_writingIterations.teleport(-offsetOfCenter * additionalOffset * 1.3 + 200, -offsetOfCenter * additionalOffset)
    
    if loop_count % 100 == 0:
        turtle_2_writingIterations.clear()
        turtle_2_writingIterations.write(loop_count, move= False, font=("Arial", 30, "normal"))
        # drawScoringUnderline(5, loop_count/100) # draws a growing line under iterations

def drawScoringUnderline(size, length):
    turtle_2_writingIterations.pensize(size)
    turtle_2_writingIterations.forward(length)
    turtle_2_writingIterations.backward(length)

# end of counter   

def offset(center_ratio: float = 0.7):
    offset_to_center = side_size/(2 * math.sin(math.pi/sides)) * -center_ratio # calculate the radius of the polygon 
    return offset_to_center
   
def draw_base_shape(
    sides: int,
    side_size: int = 2000 / sides,
    draw_labels: bool=True,
    draw_lines: bool= False,
    line_size: int = 3,
    label_font: tuple = ("Arial", 14),
    # center_ratio: float = 0.7
    ) -> dict:
    """    Draws a regular polygon centered on the screen, with optional corner labels and connecting lines.
    Args:
        sides (int): Number of sides of the polygon.
        side_size (int): Length of each side. Defaults to 2000 / sides.
        draw_labels (bool): If True, labels each corner with its index.
        draw_lines (bool): If True, draws lines between corners.
        line_size (int): Thickness of the lines if draw_lines is True.
        label_font: tuple = set font
        center_ratio: float = set ratio to offset figure from center

    Returns:
        dict: A dictionary mapping corner to their (x, y) coordinates.

    Notes:
        This is a base for fractal creation. To be used with other functions provided.
    """
    assert sides > 2, "sides must be greater than 2"
    offsetOfCenter = offset()
    teleport(offsetOfCenter,offsetOfCenter) # offset the shape so the result is drawn in the middle
    
    
    if draw_lines: # deals with drawing outlines
        pendown()
        pensize(line_size)
    else:
        penup()
    
    corners = {}
    for i in range(sides):
        forward(side_size)
        pos = position()
        val = (round(pos[0]),round(pos[1]))
        corners[i + 1] = val # saves the corner position into a dictionary 
        if draw_labels: # drawing labels
            write(f"{i+1}", font= label_font)
        left(360/sides)
    penup()
    return corners       

def pythagorean_triangle(current_pos, where_to_go) -> int:
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
    return round(c * ratio)

def fractalDrawing(sides, no_of_iterations, corners):
# fractal drawing
    for i in range(no_of_iterations):
        if i == 1000:
            tracer(i/10,0)
        if i == 5 * 1000:
            tracer(i/5)
        if i == 15 * 1000:
            tracer(i/3)
      
        
        
        dice = random.randrange(1,sides + 1)
        where_to_go = corners[dice]
        x = round(where_to_go[0])
        y = round(where_to_go[1])
        setheading(towards(x,y))

        current_pos = position()
        current_pos_rounded = (round(current_pos[0]), round(current_pos[1]))

        distanceToDraw = pythagorean_triangle(current_pos_rounded, where_to_go)
        forward(distanceToDraw)

        # color and dot drawing 
        if sides == 3:
            hue = define_hue_triangle(dice, distanceToDraw)
        else:
            hue = define_hue(distanceToDraw)
        saturation = define_saturation(distanceToDraw)
        
        draw_dot(hue, saturation)
        
        writeIterations(i)
           
def define_hue_triangle(dice, distance):
    # band_1 = random.uniform(0.25, 0.36)
    band_1 = distance/1000
    if band_1 > 0.3:
        band_1 == 0.3
    band_2 = distance/1000 + 0.4
    if band_2 > 0.7:
        band_2 == 0.7
    band_3 = distance/1000 + 0.8
    if band_3 > 1.0:
        band_3 == 1.0
    
    hue = 0.0
    if dice == 1:
        hue = band_1
    elif dice == 2:
        hue = band_2
    else:
        hue = band_3
       
    return hue
    
def define_hue(distance):
    normalized = distance / 1000
    if normalized < 0.5:
        normalized += 0.3
    return normalized    

def define_saturation(distance):
    normalized = distance / 1000
    if normalized < 0.5 :
        normalized += 0.3
    return normalized

def draw_dot(hue, saturation):
    rgb = colorsys.hsv_to_rgb(hue, saturation, 0.7)
    dot(3, rgb)

def main(sides, side_size, no_of_iterations, draw_labels=True, draw_lines=True):
    # Draw initial shape
    corners = draw_base_shape(sides, side_size, draw_labels, draw_lines)
    writingLabels()    

    fractalDrawing(sides, no_of_iterations, corners)

    hideturtle()
    update()

if __name__ == "__main__":
    main(sides, side_size, no_of_iterations, draw_labels=False, draw_lines=False)



exitonclick()