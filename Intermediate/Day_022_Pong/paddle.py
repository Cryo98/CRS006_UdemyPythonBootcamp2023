from turtle import Turtle


class Paddle(Turtle):

    def __init__(
            self,
            initial_pos: tuple[int, int] = (0, 0),
            color: str = "white",
            speed: int = 200,
            ) -> None:
        super().__init__(shape="square")
        # Visuals & configuration
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.color(color)
        self.speed("fastest")
        self.penup()
        self.goto(initial_pos)
        # BUG as of now the movement is jittery at the beginning, need to fix
        self.movement = speed

    def move_up(self, dt: float = 1):
        self.fd(self.movement * dt)

    def move_down(self, dt: float = 1):
        self.bk(self.movement * dt)

    def y_top(self):
        # Return y coordinate of top of the paddle
        return self.ycor() + 20*self.shapesize()[1]/2
    
    def y_btm(self):
        # Return y coordinate of bottom of the paddle
        return self.ycor() - 20*self.shapesize()[1]/2
