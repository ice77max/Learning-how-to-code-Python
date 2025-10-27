from turtle import *

def dash_line(lenght_of_line_and_brake):
    fd(lenght_of_line_and_brake)
    penup()
    fd(lenght_of_line_and_brake)
    pendown()
    
def dot_line(size):
    penup()
    dot(size)
    fd(size *2)
    