from turtle import Turtle
import random

# TODO add variations to the speeds
# TODO add a way to specify car colors
# TODO add lanes (?)

TOTAL_CARS = 20
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CARS_BASE_SPEED = 5


class CarManager():

    def __init__(
            self,
            spawn_region_y: tuple[int, int] = (100, -100),
            movement_region_x: tuple[int, int] = (100, -100),
            ) -> None:
        self.y_min = min(spawn_region_y)
        self.y_max = max(spawn_region_y)
        self.x_min = min(movement_region_x)
        self.x_max = max(movement_region_x)
        self.car_shapesize = (2, 1)
        self.car_bounding_box = (
            (-10 * self.car_shapesize[0], 10 * self.car_shapesize[0]),
            (-10 * self.car_shapesize[1], 10 * self.car_shapesize[1]),
        )
        self.initialize_cars()
        self.movement_speed = CARS_BASE_SPEED

    def initialize_cars(self):
        """Creates the list of cars for the car manager."""
        self.cars = list()
        for _ in range(TOTAL_CARS):
            car = Turtle(shape="square")
            car.color(random.choice(CAR_COLORS))
            car.setheading(180)
            car.penup()
            car.shapesize(
                stretch_wid=self.car_shapesize[1],
                stretch_len=self.car_shapesize[0]
                )
            self.initialize_car_position(car)
            self.cars.append(car)

    def restart_cars(self):
        """Resets all cars' position and color"""
        for car in self.cars:
            car.color(random.choice(CAR_COLORS))
            self.initialize_car_position(car)

    def initialize_car_position(self, car: Turtle):
        """Initializes car position"""
        y_pos = random.randint(self.y_min, self.y_max)
        x_pos = random.randint(self.x_min, self.x_max)
        car.goto(x=x_pos, y=y_pos)

    def move_cars(self):
        """Move all the cars at the same time"""
        for car in self.cars:
            car.forward(self.movement_speed)
            if car.xcor() < self.x_min:
                self.restart_car(car)

    def restart_car(self, car: Turtle):
        """Make the car reappear at the beginning of the movement region"""
        car.color(random.choice(CAR_COLORS))
        height = random.randint(self.y_min, self.y_max)
        car.goto(x=self.x_max, y=height)

    def increase_cars_speed(self, multiplier: float):
        self.movement_speed *= multiplier
