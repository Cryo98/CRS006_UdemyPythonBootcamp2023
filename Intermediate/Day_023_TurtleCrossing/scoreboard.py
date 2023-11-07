from turtle import Turtle

# TODO allow for string formatting
# TODO add separate customization  of game over text

DEFAULT_FONT_NAME = "Arial"
DEFAULT_FONT_SIZE = 12
DEFAULT_FONT_TYPE = "normal"
DEFAULT_ALIGNMENT = "center"
DEFAULT_COLOR = "white"


class Scoreboard(Turtle):
    """Class that stores a score and writes

    Parameters
    ----------
    x_pos : tuple[int, int] | int (optional)
        If given a tuple it considers it as x and y coordinates respectively,
        else if given an integer it considers that as the reference x
        coordinate of the text (default is 0).
    y_pos : int (optional)
        Reference y coordinate where the text center is (default is 0).
    font_size : int (optional)
        Size of the font used, it is doubled for the 'GAME OVER' text (default
        is 12).
    font_name : str (optional)
        Name of the font used (default is 'Arial').
    font_type : str (optional)
        Type of the font used (default is 'normal').
    text_align : str (optional)
        Alignment of the text (default is 'center').
    text_color : str (optional)
        Color of the text (default is 'white').
    """

    def __init__(self,
                 x_pos: tuple[int, int] | int = (0, 0),
                 y_pos: int = None,
                 font_size: int = DEFAULT_FONT_SIZE,
                 font_name: str = DEFAULT_FONT_NAME,
                 font_type: str = DEFAULT_FONT_TYPE,
                 text_align: str = DEFAULT_ALIGNMENT,
                 text_color: str = DEFAULT_COLOR,
                 ) -> None:
        super().__init__(visible=False)
        self.font = (font_name, font_size, font_type)
        self.gameover_font = (font_name, font_size*2, font_type)
        self.text_align = text_align
        self.penup()
        self.color(text_color)

        # Handles different inputs, similar to Turtle.pos()
        if type(x_pos) is tuple:
            y_pos = x_pos[1] - font_size/2
            x_pos = x_pos[0]
        elif type(x_pos) is int:
            if y_pos is None:
                y_pos = 0
        self.goto((x_pos, y_pos))

        self.score = 0
        self.update_score()

    def update_score(self):
        """Updates the score on the screen"""
        self.clear()
        self.write(f"Level: {self.score}",
                   align=self.text_align,
                   font=self.font)

    def print_game_over(self):
        """Prints 'GAME OVER' in the middle of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER",
                   align="center",
                   font=self.gameover_font)

    def increase_score(self):
        """Increases the score and updates it automatically on screen."""
        self.score += 1
        self.update_score()
