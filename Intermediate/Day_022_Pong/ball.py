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
        # TODO convert from hardcoded to adaptive
        # if y_new > (300 - self.size/2):
        #     y_new = 600 - self.size - y_new
        #     self.yvel *= -1
        # elif y_new < (-300 + self.size/2):
        #     y_new = -600 + self.size - y_new
        #     self.yvel *= -1
        # if x_new > (400 - self.size/2):
        #     x_new = 800 - self.size - x_new
        #     self.xvel *= -1
        # elif x_new < (-400 + self.size/2):
        #     x_new = -800 + self.size - x_new
        #     self.xvel *= -1
        # print("X:", x_new, ", Y:", y_new)
        self.goto(x_new, y_new)

    def y_bounce(self):
        self.yvel *= -1

    def x_bounce(self):
        self.xvel *= -1
