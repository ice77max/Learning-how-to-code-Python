from turtle import *
import my_functions as f

speed(0)
pensize(2)

diagnal_lenght = 50
square_size = 120

# start
fd(square_size)

# bottom right diagnal
left(45)
fd(diagnal_lenght)
position = pos()
back(diagnal_lenght)

left(45)
fd(square_size)

#top right diagnal
right(45)
fd(diagnal_lenght)
back(diagnal_lenght)

setheading(180)
fd(square_size)

#top left diagnal
right(90 + 45)
fd(diagnal_lenght)
back(diagnal_lenght)

setheading(270)
fd(square_size)

# outside line
teleport(int(position[0]), int(position[1]))
setheading(90)
fd(square_size)
left(90)
fd(square_size)

# dot line
teleport(0,0)
setheading(45)
for i in range(9):
    f.dot_line(3)
position = pos()

# up
setheading(90)
for i in range(20):
    f.dot_line(3)

# right
teleport(int(position[0]), int(position[1]))
setheading(0)
for i in range(20):
    f.dot_line(3)

hideturtle()

exitonclick()