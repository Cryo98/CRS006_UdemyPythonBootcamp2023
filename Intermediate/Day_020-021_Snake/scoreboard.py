from turtle import Turtle

DEFAULT_FONT_NAME = "Arial"
DEFAULT_FONT_SIZE = 12
DEFAULT_FONT_TYPE = "normal"
DEFAULT_ALIGNMENT = "center"
HIGHSCORE_FILE = "highscore.txt"


class Scoreboard(Turtle):

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
        self.score = 0
        with open(HIGHSCORE_FILE, 'a+') as f:
            f.seek(0)
            highscore_str = f.read()
            print(highscore_str)
            if len(highscore_str) > 0:
                self.highscore = int(highscore_str)
            else:
                self.highscore = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore: {self.highscore}",
                   align=self.text_align,
                   font=self.font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(HIGHSCORE_FILE, 'w+') as f:
                f.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
                   align=self.text_align,
                   font=self.gameover_font)

    def increase_score(self):
        self.score += 1
        self.update_score()
