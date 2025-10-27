import turtle
from random import randrange

# setup
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.shape("circle")
t.hideturtle()
turtle.bgcolor("LightBlue")

size_of_the_dice = 400 # size of the dice. Changing it will change the dice size 

# custom functions


def dice_throw():
    return randrange(1,7)

def draw_square(square_size):
    negative_half = square_size / 2 * -1
    t.penup()
    t.goto(negative_half, negative_half)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.penup()
    t.fd(square_size * 0.1)
    t.pendown()
    for _ in range(4):
        t.fd(square_size * 0.8)
        t.circle(square_size * 0.1, 90)
    t.end_fill()

def draw_dot(dot_size):
    t.penup()
    t.setheading(270)
    t.fd(dot_size)
    t.setheading(0)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(dot_size)
    t.end_fill()
    t.hideturtle()

def draw_dice(dice_size, no_of_dots):
    draw_square(dice_size)
    dot_size = dice_size / 10
    third = dice_size / 3.8
    
    t.penup()
    if no_of_dots == 1:
        t.goto(0, 0)
        draw_dot(dot_size)
    elif no_of_dots == 2:
        t.goto(-third, -third)
        draw_dot(dot_size)
        t.goto(third, third)
        draw_dot(dot_size)
        
    elif no_of_dots == 3:
        t.goto(-third, -third)
        draw_dot(dot_size)
        t.goto(0, 0)
        draw_dot(dot_size)
        t.goto(third, third)
        draw_dot(dot_size)
        
    elif no_of_dots == 4:
        t.goto(-third, -third)
        draw_dot(dot_size)
        t.goto(third, third)
        draw_dot(dot_size)
        
        t.goto(-third, third)
        draw_dot(dot_size)
        t.goto(third, -third)
        draw_dot(dot_size)
        
    elif no_of_dots == 5:
        t.goto(-third, -third)
        draw_dot(dot_size)
        t.goto(third, third)
        draw_dot(dot_size)
        
        t.goto(-third, third)
        draw_dot(dot_size)
        t.goto(third, -third)
        draw_dot(dot_size)
        
        # middle dot
        t.goto(0,0)
        draw_dot(dot_size)
    elif no_of_dots == 6:
        t.goto(-third, -third)
        draw_dot(dot_size)
        t.goto(third, third)
        draw_dot(dot_size)
        
        t.goto(-third, 0)
        draw_dot(dot_size)
        t.goto(third, 0)
        draw_dot(dot_size)
                
        t.goto(-third, third)
        draw_dot(dot_size)
        t.goto(third, -third)
        draw_dot(dot_size)
    
def reroll(x, y):
    t.clear()
    draw_dice(size_of_the_dice, dice_throw())
# magic

draw_dice(size_of_the_dice, dice_throw())
turtle.onscreenclick(reroll)
    


# end
turtle.done()