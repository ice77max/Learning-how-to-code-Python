import turtle
import colorsys
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cool Spiral Animation")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(7)  # Line thickness

# Function to draw a colorful spiral
def draw_spiral():
    # Use colorsys to generate smooth color transitions
    for i in range(360):
        hue = i / 360.0  # Hue value from 0 to 1
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Convert HSV to RGB
        t.pencolor(rgb)  # Set pen color
        t.forward(i * 0.4)  # Move forward, increasing distance slightly
        t.left(59)  # Turn angle for spiral effect

# Animation loop
for _ in range(3):  # Repeat the animation 3 times
    t.penup()
    t.goto(0, 0)  # Reset to center
    t.pendown()
    draw_spiral()
    time.sleep(0.5)  # Pause briefly before restarting
    t.clear()  # Clear the drawing for the next iteration

# Exit on click
screen.exitonclick()