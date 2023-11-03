# TURTLE RACE
# The player bets on a turtle, multiple turtles run randomly across the screen.
# -----------------------------------------------------------------------------
# [X] Generate multiple instances of turtles
# [X] Ask user for input on turtle color
# [X] Make turtles move randomly
# [X] Detect if turtle has reached the edge

from turtle import Turtle, Screen
from random import randint

# Constants describing the size of the window
WIDTH = 800
HEIGHT = 400

# Colors of the turtles
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)


def create_turtle(color: str = "black"):
    """Create a non-drawing turtle of a given color and returns it"""
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    return turtle


def has_turtle_reached_end(turtle: Turtle):
    """Checks if turtle has reached the border of the window"""
    return turtle.xcor() >= (WIDTH/2 - 20)


# Spacing between each turtle (from the center of each)
SPACING = 40
turtles = list()
# Initial position from above of the first turtle
initial_pos = len(COLORS)/2 * SPACING - SPACING/2
pos = initial_pos
# Initializes all the turtles based on the amount of colors given
for color in COLORS:
    turtle = create_turtle(color=color)
    turtle.setpos(x=(-WIDTH/2+20), y=pos)
    turtles.append(turtle)
    pos -= SPACING

# Asks the user for a color to bet on
# NOTE: there is no input checking for simplicity
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

# Race loop
is_race_on = True
while is_race_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if has_turtle_reached_end(turtle):
            winner = turtle.pencolor()
            is_race_on = False

# Result messages
if winner == user_bet:
    print("You've won!", end=" ")
else:
    print("You've lost...", end=" ")

print(f"The winner is the {winner} turtle!")



screen.exitonclick()
