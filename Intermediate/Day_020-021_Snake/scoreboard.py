from turtle import Turtle
import os

DEFAULT_FONT_NAME = "Arial"
DEFAULT_FONT_SIZE = 12
DEFAULT_FONT_TYPE = "normal"
DEFAULT_ALIGNMENT = "center"
HIGHSCORE_FILE = "highscore.txt"


class Scoreboard(Turtle):
    """Scoreboard that takes care of tracking the current score of the player.

    The score is shown at the top of the window centered along the x axis,
    showing a string of the form 'Score: N, Highscore: M'.
    The 'GAME OVER' text is instead shown in the middle of the canvas, with
    size doubled for the font.

    Parameters
    ----------
    window_height : int
        Height of the window in pixels.
    font_size : int (optional)
        Size of the font used, it is doubled for the 'GAME OVER' text (default
        is 12).
    font_name : str (optional)
        Name of the font used (default is 'Arial').
    font_type : str (optional)
        Type of the font used (default is 'normal').
    text_align : str (optional)
        Alignment of the text (default is 'center').
    """

    def __init__(self,
                 window_height: int,
                 font_size: int = DEFAULT_FONT_SIZE,
                 font_name: str = DEFAULT_FONT_NAME,
                 font_type: str = DEFAULT_FONT_TYPE,
                 text_align: str = DEFAULT_ALIGNMENT,
                 ) -> None:
        super().__init__(visible=False)
        self.font = (font_name, font_size, font_type)
        self.gameover_font = (font_name, font_size*2, font_type)
        self.text_align = text_align
        self.penup()
        self.color("white")
        self.goto(x=0, y=(window_height/2 - 2*font_size))

        # Highscore and score initialization
        self.score = 0
        cwd = os.path.dirname(os.path.abspath(__file__))
        self.highscore_storage = cwd + "/" + HIGHSCORE_FILE
        with open(self.highscore_storage, 'a+') as f:
            f.seek(0)
            highscore_str = f.read()
            if len(highscore_str) > 0:
                self.highscore = int(highscore_str)
            else:
                self.highscore = 0
        self.update_score()

    def update_score(self):
        """Updates text on screen for score."""
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}",
                   align=self.text_align,
                   font=self.font)

    def reset(self):
        """Resets the score and saves highscore."""
        if self.score > self.highscore:
            self.highscore = self.score
            with open(self.highscore_storage, 'w+') as f:
                f.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def print_game_over(self):
        """Prints 'GAME OVER' in the middle of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER",
                   align=self.text_align,
                   font=self.gameover_font)

    def increase_score(self):
        """Increases the score and updates the one shown on screen."""
        self.score += 1
        self.update_score()
