from turtle import Screen, _Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# CONSTANTS
# Screen width and height in pixels
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# Time step used for gameloop
TIME_STEP = .05
PLAYER_MOVEMENT = 20
# Region on top and bottom of screen where no cars appear
EMPTY_REGION = 80
# Difficulty level multiplier
CARS_SPEED_MULTIPLIER = 1.2


def main():
    # Initialize screen parameters
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    # Initialize game objects
    player = Player(
        initial_pos=(0, -SCREEN_HEIGHT/2 + 20),
        color="black",
        speed=PLAYER_MOVEMENT
        )
    cars = CarManager(
        movement_region_x=(-SCREEN_WIDTH/2 - 20, SCREEN_WIDTH/2 + 20),
        spawn_region_y=(-SCREEN_HEIGHT/2 + EMPTY_REGION, SCREEN_WIDTH/2 - EMPTY_REGION))
    scoreboard = Scoreboard(
        x_pos=-SCREEN_WIDTH/2 + 20,
        y_pos=SCREEN_HEIGHT/2 - 40,
        text_align="left",
        text_color="black"
    )
    scoreboard.increase_score()
    initialize_controls(screen, player)

    is_game_on = True
    while is_game_on:
        cars.move_cars()
        player_has_won = check_top_collision(player, y_threshold=SCREEN_HEIGHT/2)
        if player_has_won:
            player.reset_position()
            cars.restart_cars()
            cars.increase_cars_speed(CARS_SPEED_MULTIPLIER)
            scoreboard.increase_score()
        car_hit = check_car_collision(player, cars)
        if car_hit:
            scoreboard.print_game_over()
            is_game_on = False
        screen.update()
        time.sleep(TIME_STEP)
    screen.exitonclick()


# CONTROLS
def initialize_controls(screen: _Screen, player: Player):
    screen.listen()
    screen.onkey(key="Up", fun=player.move_up)


# CHECKS
def check_top_collision(player: Player, y_threshold: int = 100):
    """Returns True if the player has surpassed the threshold"""
    unilateral_size = player.shapesize()[1] * 20 / 2
    if player.ycor() + unilateral_size > y_threshold:
        has_collision_happened = True
    else:
        has_collision_happened = False
    return has_collision_happened


def check_car_collision(player: Player, cars: CarManager):
    player_bb_rel = player.bounding_box
    player_bb_abs = (
        (player_bb_rel[0][0] + player.xcor(), player_bb_rel[0][1] + player.xcor()),
        (player_bb_rel[1][0] + player.ycor(), player_bb_rel[1][1] + player.ycor()),
    )
    for car in cars.cars:
        car_bb_rel = cars.car_bounding_box
        car_bb_abs = (
            (car_bb_rel[0][0] + car.xcor(), car_bb_rel[0][1] + car.xcor()),
            (car_bb_rel[1][0] + car.ycor(), car_bb_rel[1][1] + car.ycor()),
        )
        if not (player_bb_abs[0][0] > car_bb_abs[0][1] or player_bb_abs[0][1] < car_bb_abs[0][0]):
            if not (player_bb_abs[1][0] > car_bb_abs[1][1] or player_bb_abs[1][1] < car_bb_abs[1][0]):
                return True
    return False

# It was called too many times, but kept here for future reference
# def obtain_bounding_box(obj: Turtle) -> tuple[tuple, tuple]:
#     x_bounds = (-10 * obj.shapesize[1], 10 * obj.shapesize[1])
#     y_bounds = (-10 * obj.shapesize[0], 10 * obj.shapesize[0])
#     if obj.heading() == 90 or obj.heading() == 270:
#         x_bounds, y_bounds = y_bounds, x_bounds
#     bounding_box = (x_bounds, y_bounds)
#     return bounding_box


if __name__ == "__main__":
    main()