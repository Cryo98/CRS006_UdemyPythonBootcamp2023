from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Constants
SCREEN_WIDTH = 600  # Width of the window in pixels
SCREEN_HEIGHT = 600  # Height of the window in pixels
TIMESTEP = 1/20  # Time between each movement of the snake

# Initialization window
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")

# Allows to control the refresh rate manually through screen.update
screen.tracer(0)

# Initializes tall the needed classes
snake = Snake()
segment_size = snake.get_segment_size()
food = Food(window_height=SCREEN_HEIGHT, window_width=SCREEN_WIDTH, grid_step=segment_size)
scoreboard = Scoreboard(window_height=SCREEN_HEIGHT, font_size=24)

# Initializes the user commands
screen.listen()
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)


# If True game is running, else it exits the game
is_game_on = True
# Game loop
while is_game_on:
    snake.move()

    # Detect collision with food
    if snake.head.distance(food.pos()) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()

    # Detect collision with wall
    too_far_right = snake.head.xcor() > (SCREEN_WIDTH/2 - segment_size/2)
    too_far_left = snake.head.xcor() < -(SCREEN_WIDTH/2 - segment_size/2)
    too_far_up = snake.head.ycor() > (SCREEN_HEIGHT/2 - segment_size/2)
    too_far_down = snake.head.ycor() < -(SCREEN_HEIGHT/2 - segment_size/2)
    if too_far_right or too_far_left or too_far_up or too_far_down:
        is_game_on = False
        scoreboard.print_game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment.pos()) < segment_size/2:
            is_game_on = False
            scoreboard.print_game_over()

    screen.update()
    time.sleep(TIMESTEP)

screen.exitonclick()
