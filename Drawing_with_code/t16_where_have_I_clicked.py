import turtle

def click_handler(x, y):
    print(f"You clicked at: x={x}, y={y}")

turtle.bgcolor("lightblue")

# Register the handler (note: no parentheses!)
turtle.onscreenclick(click_handler)

turtle.done()