from turtle import *
import random
import math
import colorsys

# of set of
setup(1.0,1.0)

speed(0)
pensize(1)

penup()


# TODO Play with those numbers
# change those numbers to get different shapes
sides = 3
side_size = 2000 / sides
ratio = 0.5
# of set so the shape is in the center of the screen

no_of_iterations = 10000

tracer(0) # speed

# functions

def draw_base_shape(
    sides: int,
    side_size: int = 2000 / sides,
    draw_labels: bool=True,
    draw_lines: bool= False,
    line_size: int = 3,
    label_font: tuple = ("Arial", 14),
    center_ratio: float = 0.7
    ) -> dict:
    """
    Draws a regular polygon centered on the screen, with optional corner labels and connecting lines.

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
    offset_to_center = side_size/(2 * math.sin(math.pi/sides)) * -center_ratio # calculate the radius of the polygon 
    teleport(offset_to_center,offset_to_center) # offset the shape so the result is drawn in the middle
    
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

def fractalDrawing(sides, no_of_iterations, pythagorean_triangle, corners):
# fractal drawing
    for i in range(no_of_iterations):
        dice = random.randrange(1,sides + 1)
        where_to_go = corners[dice]
        x = round(where_to_go[0])
        y = round(where_to_go[1])
        setheading(towards(x,y))

        current_pos = position()
        current_pos_rounded = (round(current_pos[0]), round(current_pos[1]))
    
        forward(pythagorean_triangle(current_pos_rounded, where_to_go))

        band_1 = random.uniform(0.0, 0.33)
        band_2 = random.uniform(0.4, 0.7)
        band_3 = random.uniform(0.75, 1.0)
        hue = 0.0
        if dice == 1:
            hue = band_1
        elif dice == 2:
            hue = band_2
        else:
            hue = band_3
        
        rgb = colorsys.hsv_to_rgb(hue, 0.9, 0.9)
        
        
        dot(3, rgb)

def main():
    # Draw initial shape
    corners = draw_base_shape(sides, side_size, draw_labels=True, draw_lines=True)

    fractalDrawing(sides, no_of_iterations, pythagorean_triangle, corners)

if __name__ == "__main__":
    main()



exitonclick()