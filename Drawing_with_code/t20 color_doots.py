import turtle as t
import colors
from random import randint, choice

screen = t.Screen()
screen.setup(1.0,1.0)

for i in range(200)[::-1]:
    print(i)
    t.teleport(randint(-300, 300),randint(-300, 300))
    t.dot(i, choice(colors.specific_shades))

t.exitonclick()