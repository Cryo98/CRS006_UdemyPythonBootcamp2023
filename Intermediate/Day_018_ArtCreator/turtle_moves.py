from turtle import Turtle
import turtle as t
import random


def draw_square(
        turtle: Turtle,
        size: int = 100,
        ) -> None:
    """Draws a square from the originating point and going counterclockwise

    Parameters
    ----------
    turtle : turtle.Turtle
        turtle object to move.
    size : int, optional
        size of the square side. (Default is 100)
    """
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_dashed_line(
        turtle: Turtle,
        length: int = 500,
        spacing: int = 10
        ) -> None:
    """Draws a dashed line in the heading direction."""
    n_dashes = int(length/spacing)
    for _ in range(n_dashes):
        turtle.pendown()
        turtle.forward(spacing)
        turtle.penup()
        turtle.forward(spacing)


def draw_n_polygon(turtle: Turtle, n_sides: int, side: int = 100):
    """Draws an N-polygon in a counterclockwise rotation"""
    angle = 360/n_sides
    for _ in range(n_sides):
        turtle.forward(side)
        turtle.left(-angle)


def random_walk(
        turtle: Turtle,
        step_size: int = 10,
        max_steps: int = 100,
        colors: str | list[str] = None,
        random_colors: bool = False
        ):
    """Makes the turtle walk in a random manner along cardinal directions"""
    # Handles random colors selection
    apply_random_colors = False
    if type(colors) is str:
        turtle.color(colors)
    elif type(colors) is list or random_colors:
        apply_random_colors = True
        colormode = t.colormode()

    for _ in range(max_steps):
        if apply_random_colors:
            if type(colors) is list:
                turtle.color(random.choice(colors))
            else:
                turtle.color(generate_random_color(colormode))
        angle_rotation = random.choice([0, 90, 180, 270])
        turtle.left(angle_rotation)
        turtle.forward(step_size)


def generate_random_color(colormode: int = 255):
    if colormode == 255:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    elif colormode == 1:
        r = random.uniform(0, 1)
        g = random.uniform(0, 1)
        b = random.uniform(0, 1)
    return (r, g, b)
