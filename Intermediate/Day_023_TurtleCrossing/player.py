from turtle import Turtle


class Player(Turtle):
    """A simple class for a Turtle that can move up and down

    Parameters
    ----------
    initial_pos : tuple[int, int] (optional)
        Initial position of the Turtle (default is (0, 0)).
    color : str (optional)
        Color of the Turtle (defualt is 'white').
    speed : int (optional)
        Movement in pixels for each step taken (default is 20)."""

    def __init__(
            self,
            initial_pos: tuple[int, int] = (0, 0),
            color: str = "white",
            speed: int = 20,
            ) -> None:
        super().__init__(shape="turtle")
        self.setheading(90)
        self.color(color)
        self.bounding_box = (
            (-10 * self.shapesize()[0], 10 * self.shapesize()[0]),
            (-10 * self.shapesize()[1], 10 * self.shapesize()[1]),
        )
        self.speed("fastest")
        self.penup()
        self.initial_pos = initial_pos
        self.goto(self.initial_pos)
        self.movement = speed

    def move_up(self):
        self.fd(self.movement)

    def move_down(self):
        self.bk(self.movement)

    def reset_position(self):
        self.goto(self.initial_pos)
