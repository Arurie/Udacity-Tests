import turtle

count = 0

def draw_square(turtles):
    for i in range(1, 5):
        turtles.forward(100)
        turtles.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    clarence = turtle.Turtle()
    clarence.color("red")
    clarence.shape("turtle")
    for i in range(1, 37):
        draw_square(clarence)
        clarence.right(10)

    maria = turtle.Turtle()
    maria.circle(100)
    maria.color("purple")
    maria.shape("arrow")

    window.exitonclick()

draw_square()
draw_circle()
