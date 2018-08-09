import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    clarence = turtle.Turtle()
    clarence.forward(100)
    clarence.right(90)
    clarence.forward(100)
    clarence.right(90)
    clarence.forward(100)
    clarence.right(90)
    clarence.forward(100)
    clarence.right(90)

    window.exitonclick()

draw_square()
