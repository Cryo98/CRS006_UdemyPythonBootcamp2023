from turtle import Turtle

# Constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SEGMENT_SIZE = 20
INITIAL_SEGMENTS = 3


class Snake():

    def __init__(self) -> None:
        self.segments = list()
        self.__init_segments()
        self.head = self.segments[0]
        # Flag to avoid quick keystrokes that allow to invert direction
        self.is_turning = False

    def __init_segments(self) -> None:
        for i in range(INITIAL_SEGMENTS):
            section = Turtle(shape="square")
            section.color("white")
            section.penup()
            section.speed("fastest")
            section.goto(-SEGMENT_SIZE*i, 0)
            self.segments.append(section)

    def move(self) -> None:
        """Moves all the segments in a convoy-like manner

        It runs through each segment of the body, moving it and then copying
        the heading of the previous segment."""
        prev_section_heading = self.head.heading()
        for section in self.segments:
            section.forward(SEGMENT_SIZE)
            current_section_heading = section.heading()
            if current_section_heading != prev_section_heading:
                section.setheading(prev_section_heading)
            prev_section_heading = current_section_heading
        # Flag that controls if a change in direction is already on-going,
        # to avoid overlapping commands
        self.is_turning = False

    def move_up(self):
        """Changes the heading of the snake to up direction, unless it has
        already received a command or it is going down"""
        if not self.is_turning and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.is_turning = True

    def move_down(self):
        """Changes the heading of the snake to down direction, unless it has
        already received a command or it is going up"""
        if not self.is_turning and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.is_turning = True

    def move_left(self):
        """Changes the heading of the snake to left direction, unless it has
        already received a command or it is going right"""
        if not self.is_turning and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.is_turning = True

    def move_right(self):
        """Changes the heading of the snake to right direction, unless it has
        already received a command or it is going left"""
        if not self.is_turning and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.is_turning = True

    def get_segment_size(self):
        """Returns the size of a single segment"""
        return SEGMENT_SIZE
