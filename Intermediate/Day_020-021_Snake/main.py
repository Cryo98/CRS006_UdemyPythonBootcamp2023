from turtle import Screen
from snake import Snake
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

# Initializes the Snake
snake = Snake()

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
    screen.update()
    time.sleep(TIMESTEP)

screen.exitonclick()
