from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(
            self,
            color: str = "white",
            size: int = 10,
            speed: int = 20,
            shape: str = "circle"
            ) -> None:
        super().__init__(shape=shape)
        self.size = size
        self.shapesize(size/20.0)
        self.color(color)
        self.penup()
        self.movement = speed
        self.xvel = 0
        self.yvel = 0
        self.refresh()

    def refresh(self, direction: str = "right"):
        if direction == "right":
            self.xvel = self.movement
        elif direction == "left":
            self.xvel = -self.movement
        self.yvel = self.movement * random.choice([1, -1])
        self.goto(0, 0)

    def move(self, dt=1):
        dx = self.xvel * dt
        dy = self.yvel * dt
        x_new = self.xcor() + dx
        y_new = self.ycor() + dy
        self.goto(x_new, y_new)

    def y_bounce(self, speed_multiplier: int = 1):
        self.yvel *= -speed_multiplier
        self.xvel *= speed_multiplier

    def x_bounce(self, speed_multiplier: int = 1):
        self.yvel *= speed_multiplier
        self.xvel *= -speed_multiplier
