from turtle import Turtle
from random import randint
import math


class Food(Turtle):

    def __init__(
            self,
            window_width: int,
            window_height: int,
            grid_step: int = 1,
            ) -> None:
        super().__init__(shape="circle")
        # object appearance
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        # area where it can appear
        self.x_bounds = (-window_width/2, window_width/2)
        self.y_bounds = (-window_height/2, window_height/2)
        # space between two adiacent squares, to always have it centered
        self.grid_step = grid_step
        self.refresh()

    def refresh(self):
        """Moves the object in a random location within the allowed area."""
        rnd_x = randint(min(self.x_bounds)+1, max(self.x_bounds)-1)
        rnd_y = randint(min(self.y_bounds)+1, max(self.y_bounds)-1)
        # Aligns the point with the grid used
        aligned_x = math.trunc(rnd_x / self.grid_step) * self.grid_step
        aligned_y = math.trunc(rnd_y / self.grid_step) * self.grid_step
        self.goto(x=aligned_x, y=aligned_y)
