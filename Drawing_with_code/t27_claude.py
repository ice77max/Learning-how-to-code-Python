import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mathematical Patterns")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Pattern 1: Sine Wave Spiral
def sine_wave_spiral():
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"]
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    
    for i in range(500):
        t.color(colors[i % len(colors)])
        angle = math.radians(i * 3)
        x = -200 + i * 0.5
        y = 200 + math.sin(angle) * 30
        t.goto(x, y)

# Pattern 2: Parametric Rose Curve
def rose_curve():
    colors = ["#FF1744", "#F50057", "#D500F9", "#651FFF", "#2979FF"]
    t.penup()
    t.goto(200, 200)
    t.pendown()
    
    k = 7  # Number of petals
    for i in range(360 * k):
        t.color(colors[i % len(colors)])
        angle = math.radians(i)
        r = 80 * math.cos(k * angle)
        x = 200 + r * math.cos(angle)
        y = 200 + r * math.sin(angle)
        t.goto(x, y)

# Pattern 3: Circular Wave Interference
def wave_interference():
    colors = ["#00E676", "#76FF03", "#C6FF00", "#FFEA00", "#FFC400"]
    t.penup()
    
    for angle in range(0, 360, 3):
        rad = math.radians(angle)
        distance = 100 + 30 * math.sin(math.radians(angle * 5))
        x = -200 + distance * math.cos(rad)
        y = -150 + distance * math.sin(rad)
        t.goto(x, y)
        t.dot(5, colors[angle % len(colors)])

# Pattern 4: Lissajous Curve
def lissajous_curve():
    colors = ["#FF6B35", "#F7931E", "#FDC830", "#F37335", "#E84545"]
    t.penup()
    
    a, b = 5, 4  # Frequency parameters
    for i in range(1000):
        t.color(colors[i % len(colors)])
        angle = math.radians(i)
        x = 200 + 100 * math.sin(a * angle + math.pi/2)
        y = -150 + 100 * math.sin(b * angle)
        t.goto(x, y)
        if i == 0:
            t.pendown()

# Pattern 5: Logarithmic Spiral
def logarithmic_spiral():
    colors = ["#E91E63", "#9C27B0", "#673AB7", "#3F51B5", "#2196F3"]
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    a = 0.1
    b = 0.2
    for theta in range(0, 720, 2):
        rad = math.radians(theta)
        r = a * math.exp(b * rad)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        t.color(colors[(theta // 10) % len(colors)])
        t.goto(x, y)

# Draw all patterns
# sine_wave_spiral()
# rose_curve()
wave_interference()
lissajous_curve()
# logarithmic_spiral()


# Keep window open
screen.mainloop()