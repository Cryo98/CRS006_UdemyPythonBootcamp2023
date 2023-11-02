# ETCH-A-SKETCH APP
# Use the keyboard to control a turtle do draw
# ---------------------------------------------
# [X] Make the turtle move forward with "W"
# [X] Make the turtle move backwards with "S"
# [X] Make the turtle turn counter-clockwise with "A"
# [X] Make the turtle turn clockwise with "D"
# [X] Clear the drawing with "C" and return home


from turtle import Turtle, Screen

tim = Turtle()


def move_forward(turtle):
    """Moves the turtle forward by 10 steps"""
    turtle.forward(10)


def move_backwards(turtle):
    """Moves the turtle backwards by 10 steps"""
    turtle.backward(10)


def rotate_counterclockwise(turtle):
    """Rotates the turtle by 5 degrees counter-clockwise"""
    h = turtle.heading()
    turtle.setheading(h+5)


def rotate_clockwise(turtle):
    """Rotates the turtle by 5 degrees clockwise"""
    h = turtle.heading()
    turtle.setheading(h-5)


def reset_screen(turtle):
    """Moves the turtle back to the beginning and clears its drawing"""
    turtle.home()
    turtle.clear()


screen = Screen()
screen.listen()
# Key listeners
screen.onkeypress(key="w", fun=lambda: move_forward(tim))
screen.onkeypress(key="s", fun=lambda: move_backwards(tim))
screen.onkeypress(key="a", fun=lambda: rotate_counterclockwise(tim))
screen.onkeypress(key="d", fun=lambda: rotate_clockwise(tim))
screen.onkey(key="c", fun=lambda: reset_screen(tim))

#
screen.exitonclick()

