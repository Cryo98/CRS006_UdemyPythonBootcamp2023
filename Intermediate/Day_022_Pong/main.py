# PONG
# ----
# [X] Create a moving ball -> Ball class
# [X] Create paddles for players -> Paddle class
# [X] Add control to paddles
# [X] Add ball collision with wall
# [X] Add ball collision with paddle
# [X] Create visual environment
# [X] Add scoring system -> Scoreboard class
# [X] Add detection of miss

from turtle import Screen, Turtle, _Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TIME_STEP = 1/60
SCORE_FONT_SIZE = 36
PADDLE_BOUNCE_MULTIPLIER = 1.05


def pong():
    """Runs the main script for the game"""
    screen = initialize_screen()
    # Objects initialization
    player_1 = Paddle(initial_pos=((SCREEN_WIDTH/2 - 40), 0), speed=800)
    player_2 = Paddle(initial_pos=(-(SCREEN_WIDTH/2 - 40), 0), speed=800)
    ball = Ball(size=20, speed=300, shape="square")
    scoreboard = Scoreboard(pos=(0, SCREEN_HEIGHT/2 - 3*SCORE_FONT_SIZE/2), font_size=SCORE_FONT_SIZE)
    initialize_controls(screen, player_1, player_2)

    # Main gameloop
    is_game_on = True
    while is_game_on:
        # Update objects position
        ball.move(dt=TIME_STEP)

        # Collision detection
        detect_ball_wall_collision(height=SCREEN_HEIGHT, width=SCREEN_WIDTH, ball=ball)
        detect_ball_paddle_collision(paddle=player_1, ball=ball)
        detect_ball_paddle_collision(paddle=player_2, ball=ball)
        has_scored, score, new_direction = detect_ball_out_of_bounds(ball, player_2, player_1)

        # Score update
        if has_scored:
            ball.refresh(new_direction)
            scoreboard.increment_score(score)
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
    """Initialize the event listener and associate controls to the different
    functions"""
    screen.listen()
    screen.onkeypress(key="Up", fun=lambda: move_paddle_up(player_1, SCREEN_HEIGHT/2, TIME_STEP))
    screen.onkeypress(key="Down", fun=lambda: move_paddle_down(player_1, -SCREEN_HEIGHT/2, TIME_STEP))
    screen.onkeypress(key="w", fun=lambda: move_paddle_up(player_2, SCREEN_HEIGHT/2, TIME_STEP))
    screen.onkeypress(key="s", fun=lambda: move_paddle_down(player_2, -SCREEN_HEIGHT/2, TIME_STEP))
    screen.onkeypress(key="Escape", fun=screen.bye)


def detect_ball_wall_collision(height: int, width: int, ball: Ball):
    """Detects when the ball reaches one of the horizontal walls and makes it
    bounce"""
    if ball.ycor() >= (height/2 - ball.size/2) or ball.ycor() <= -(height/2 - ball.size/2):
        ball.y_bounce()
    # if ball.xcor() >= (width/2 - ball.size/2) or ball.xcor() <= -(width/2 - ball.size/2):
    #     ball.x_bounce()


def detect_ball_paddle_collision(paddle: Paddle, ball: Ball):
    """Detects when the ball touches a paddle and makes it bounce"""
    # Distance at which the two objects collide
    x_contact_distance = ball.size/2 + paddle.shapesize()[0] * 20 / 2
    y_contact_distance = ball.size/2 + paddle.shapesize()[1] * 20 / 2
    x_distance = ball.xcor() - paddle.xcor()
    y_distance = ball.ycor() - paddle.ycor()

    if abs(x_distance) <= x_contact_distance and abs(y_distance) <= y_contact_distance:
        # Ensures that the bounce happens only if the ball is going against the paddle
        if x_distance * ball.xvel < 0:
            ball.x_bounce(speed_multiplier=PADDLE_BOUNCE_MULTIPLIER)


def detect_ball_out_of_bounds(ball: Ball, left_player: Paddle, right_player: Paddle):
    """Detects if the ball surpasses one of the players and is not reachable,
    returning the if it has scored, the score update and the next direction of
    throw when the ball resets."""
    if ball.xcor() < left_player.xcor() - ball.size:
        has_scored = True
        score = (0, 1)
        new_direction = "right"
    elif ball.xcor() > right_player.xcor() + ball.size:
        has_scored = True
        score = (1, 0)
        new_direction = "left"
    else:
        has_scored = False
        score = None
        new_direction = None
    return has_scored, score, new_direction


def move_paddle_up(paddle: Paddle, limit: int = 100, dt: float = 1.0):
    """Moves the paddle up if does not surpass the specified region.

    Parameters
    ----------
    paddle : paddle.Paddle
        Paddle object to move
    limit : int (optional)
        Upper limit to movement (default is 100).
    dt : float (optional)
        Time step to consider for movement (default is 1.0)."""
    if paddle.y_top() < limit:
        paddle.move_up(dt)


def move_paddle_down(paddle: Paddle, limit: int = -100, dt: float = 1.0):
    """Moves the paddle down if does not surpass the specified region.

    Parameters
    ----------
    paddle : paddle.Paddle
        Paddle object to move
    limit : int (optional)
        Lower limit to movement (default is -100).
    dt : float (optional)
        Time step to consider for movement (default is 1.0)."""
    if paddle.y_btm() > limit:
        paddle.move_down(dt)


def create_perimeter(
        width: int,
        height: int,
        line_color: str = "black",
        line_width: int = 2,
        ) -> None:
    """Creates a rectangular perimeter centered around (0, 0).

    Parameters
    ----------
    width : int
        Width of the perimeter.
    height : int
        Height of the perimeter.
    line_color : str (optional)
        Color of the line (default is 'black').
    line_width : int (optional)
        Width of the line drawn (default is 2).
    """
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
