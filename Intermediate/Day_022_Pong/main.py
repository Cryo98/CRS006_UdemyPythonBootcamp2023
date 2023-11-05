# PONG
# ----
# [X] Create a moving ball -> Ball class
# [X] Create paddles for players -> Paddle class
# [X] Add control to paddles
# [X] Add ball collision with wall
# [ ] Add ball collision with paddle
# [X] Create visual environment
# [ ] Add scoring system -> Scoreboard class
# [ ] Add detection of miss

from turtle import Screen, Turtle, _Screen
from paddle import Paddle
from ball import Ball
import time

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TIME_STEP = 1/60


def pong():
    """Runs the main script for the game"""
    screen = initialize_screen()
    player_1 = Paddle(initial_pos=((SCREEN_WIDTH/2 - 40), 0), speed=800)
    player_2 = Paddle(initial_pos=(-(SCREEN_WIDTH/2 - 40), 0), speed=800)
    ball = Ball(size=20, speed=600)
    initialize_controls(screen, player_1, player_2)
    is_game_on = True
    while is_game_on:
        ball.move(dt=TIME_STEP)
        detect_ball_wall_collision(height=SCREEN_HEIGHT, width=SCREEN_WIDTH, ball=ball)
        detect_ball_paddle_collision(paddle=player_1, ball=ball)
        detect_ball_paddle_collision(paddle=player_2, ball=ball)
        screen.update()
        time.sleep(TIME_STEP)
    screen.exitonclick()


def initialize_screen() -> _Screen:
    """Initialize the screen to give an appearance similar to pong, returning
    the Screen object."""
    screen = Screen()
    # screen.screensize(canvwidth=SCREEN_WIDTH, canvheight=SCREEN_HEIGHT)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)
    create_dashed_midline(screen_height=SCREEN_HEIGHT, line_color="white")
    create_perimeter(height=SCREEN_HEIGHT, width=SCREEN_WIDTH,
                     line_color="white", line_width=8)
    screen.update()
    return screen


def initialize_controls(screen: _Screen, player_1: Paddle, player_2: Paddle):
    screen.listen()
    screen.onkeypress(key="Up", fun=lambda: player_1.move_up(TIME_STEP))
    screen.onkeypress(key="Down", fun=lambda: player_1.move_down(TIME_STEP))
    screen.onkeypress(key="w", fun=lambda: player_2.move_up(TIME_STEP))
    screen.onkeypress(key="s", fun=lambda: player_2.move_down(TIME_STEP))


def detect_ball_wall_collision(height: int, width: int, ball: Ball):
    """Detects when the ball overcomes one of the walls"""
    if ball.ycor() >= (height/2 - ball.size/2) or ball.ycor() <= -(height/2 - ball.size/2):
        ball.y_bounce()
    if ball.xcor() >= (width/2 - ball.size/2) or ball.xcor() <= -(width/2 - ball.size/2):
        ball.x_bounce()


def detect_ball_paddle_collision(paddle: Paddle, ball: Ball):
    # Distance at which the two objects collide
    x_contact_distance = ball.size/2 + paddle.shapesize()[0] * 20 / 2
    y_contact_distance = ball.size/2 + paddle.shapesize()[1] * 20 / 2
    x_distance = ball.xcor() - paddle.xcor()
    y_distance = ball.ycor() - paddle.ycor()

    if abs(x_distance) <= x_contact_distance and abs(y_distance) <= y_contact_distance:
        # Ensures that the bounce happens only if the ball is going against the paddle
        if x_distance * ball.xvel < 0:
            ball.x_bounce()


def create_perimeter(
        width: int,
        height: int,
        line_color: str = "black",
        line_width: int = 2,
        ) -> None:
    # TODO add docstring
    perimeter_tracer = Turtle(visible=False)
    perimeter_tracer.penup()
    perimeter_tracer.goto(-width/2, -height/2)
    perimeter_tracer.color(line_color)
    perimeter_tracer.pensize(line_width)
    perimeter_tracer.pendown()
    for _ in range(2):
        perimeter_tracer.fd(width)
        perimeter_tracer.left(90)
        perimeter_tracer.fd(height)
        perimeter_tracer.left(90)


def create_dashed_midline(
        screen_height: int,
        line_color: str = "black",
        dash_length: int = 10,
        dash_spacing: int = 10,
        dash_width: int = 3,
        ) -> None:
    """Creates a vertical dashed line in the middle of the screen.

    It creates a turtle that, starting from the bottom-centre of the window,
    it draws a dashed line going towards the top-centre of the window.

    Parameters
    ----------
    screen_height : int
        Height of the screen in pixels.
    line_color : str (optional)
        String representing the color of the line, as per Tkinter standard
        color references (default is 'black').
    dash_length : int (optional)
        Length of the dash in pixels (default is 10).
    dash_spacing : int (optional)
        Spacing between the end of a dash and the beginning of another
        (default is 10).
    dash_width : int (optional)
        Width of the drawn dashes in pixels (default is 3)."""
    # BUG the line is generated lower, it is probably due to the difference
    # between window height and canvas height
    midline_tracer = Turtle(visible=False)
    midline_tracer.color(line_color)
    midline_tracer.pensize(dash_width)
    midline_tracer.speed("fastest")
    midline_tracer.penup()
    midline_tracer.goto(0, -screen_height/2)
    midline_tracer.setheading(90)
    # Dash line loop
    while midline_tracer.ycor() < screen_height/2:
        midline_tracer.pendown()
        midline_tracer.fd(dash_length)
        midline_tracer.penup()
        midline_tracer.fd(dash_spacing)


if __name__ == "__main__":
    pong()
