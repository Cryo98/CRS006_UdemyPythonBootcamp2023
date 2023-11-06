from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(
            self,
            color: str = "white",
            pos: tuple = (0, 0),
            font_size: int = 24,
            font_name: str = "Arial") -> None:
        super().__init__(visible=False)
        self.penup()
        self.color(color)
        self.font = (font_name, font_size, "normal")
        # Makes it so that the text is at the correct position
        self.goto(x=pos[0], y=pos[1] - font_size/2)
        self.score = [0, 0]
        self.update_score()

    def update_score(self):
        self.clear()
        score_string = f"{self.score[0]}      {self.score[1]}"
        self.write(score_string, align="center", font=self.font)

    def increment_score(self, score_updates: tuple):
        self.score[0] += score_updates[0]
        self.score[1] += score_updates[1]
        self.update_score()
