import turtle as t
colors = ["white", "black"]

for i in range(100)[::-1]:
    t.dot(i*8)
    t.color(colors[i%2])
t.hideturtle() 
    
t.exitonclick()