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
        self.is_turning = False

    def move_up(self):
        if not self.is_turning and self.head.heading() != DOWN:
            self.head.setheading(UP)
        self.is_turning = True

    def move_down(self):
        if not self.is_turning and self.head.heading() != UP:
            self.head.setheading(DOWN)
        self.is_turning = True

    def move_left(self):
        if not self.is_turning and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self.is_turning = True

    def move_right(self):
        if not self.is_turning and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self.is_turning = True

    def get_segment_size(self):
        return SEGMENT_SIZE
