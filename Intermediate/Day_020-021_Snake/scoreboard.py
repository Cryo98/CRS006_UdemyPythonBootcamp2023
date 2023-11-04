from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self,
                 window_height: int,
                 font_size: int = 12,
                 font_name: str = "Arial",
                 font_type: str = "normal",
                 text_align: str = "center",
                 ) -> None:
        super().__init__(visible=False)
        self.font = (font_name, font_size, font_type)
        self.gameover_font = (font_name, font_size*2, "normal")
        self.text_align = text_align
        self.penup()
        self.color("white")
        self.goto(x=0, y=(window_height/2 - 2*font_size))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=self.text_align, font=self.font)

    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=self.text_align, font=self.gameover_font)

    def increase_score(self):
        self.score += 1
        self.update_score()
