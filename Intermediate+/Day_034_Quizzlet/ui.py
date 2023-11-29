import tkinter as tk
from pathlib import Path

THEME_COLOR = "#375362"

cwd = Path(__file__).parent


class QuizInterface():

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Quizzlet")
        self.window.config(bg=THEME_COLOR)
        # Initialize the visual elements
        self._init_canvas()
        self._init_score()
        self._init_buttons()
        self.window.mainloop()

    def _init_canvas(self):
        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    def _init_score(self):
        self.score = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.config(padx=20, pady=20)
        self.score.grid(row=0, column=1)

    def _init_buttons(self):
        # BUG: does not load the image correctly, should look into it
        button_true_image = tk.PhotoImage(str(cwd/"images"/"true.png"))
        self.button_true = tk.Button(width=40, height=40, image=button_true_image)
        self.button_true.grid(row=2, column=0)


if __name__ == "__main__":
    app = QuizInterface()
