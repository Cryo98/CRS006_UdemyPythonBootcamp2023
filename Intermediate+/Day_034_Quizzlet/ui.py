import tkinter as tk
from pathlib import Path
from quiz_brain import QuizBrain
from question_model import Question

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 14, "bold")
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
PADDING = 20
BLINK_LENGTH_MS = 500

cwd = Path(__file__).parent


class QuizInterface():

    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quizzlet")
        self.window.config(bg=THEME_COLOR)
        # Initialize the visual elements
        self._init_canvas()
        self._init_score()
        self._init_buttons()
        self.next_question()
        self.window.mainloop()

    def _init_canvas(self):
        self.canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=PADDING,
            pady=PADDING,
            )
        self.question_text = self.canvas.create_text(
            CANVAS_WIDTH/2,
            CANVAS_HEIGHT/2,
            text="Example text.",
            font=QUESTION_FONT,
            width=CANVAS_WIDTH-PADDING,
            )

    def _init_score(self):
        self.score = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.config(font=SCORE_FONT)
        self.score.grid(row=0, column=1, padx=PADDING, pady=PADDING)

    def _init_buttons(self):
        button_true_image_path = cwd/"images/true.png"
        # NOTE: the image must be stored in memory, so its scope has to be the
        # same as the object
        self.button_true_image = tk.PhotoImage(file=button_true_image_path)
        self.button_true = tk.Button(image=self.button_true_image)
        self.button_true.config(highlightthickness=0)
        self.button_true.config(command=lambda: self.check_answer("True"))
        self.button_true.grid(row=2, column=0, padx=PADDING, pady=PADDING)

        button_false_image_path = cwd/"images/false.png"
        # NOTE: the image must be stored in memory, so its scope has to be the
        # same as the object
        self.button_false_image = tk.PhotoImage(file=button_false_image_path)
        self.button_false = tk.Button(image=self.button_false_image)
        self.button_false.config(highlightthickness=0)
        self.button_false.config(command=lambda: self.check_answer("False"))
        self.button_false.grid(row=2, column=1, padx=PADDING, pady=PADDING)

    def next_question(self):
        question_text = self.quiz.next_question()
        self.update_text(question_text)

    def update_score(self, score: int):
        self.score.config(text=f"Score: {score}")

    def update_text(self, text: str):
        self.canvas.itemconfig(self.question_text, text=text)

    def check_answer(self, answer: str):
        is_answer_correct = self.quiz.check_answer(answer)
        if is_answer_correct:
            self.blink_color_canvas("green")
            self.update_score(self.quiz.score)
        else:
            self.blink_color_canvas("red")
        if self.quiz.still_has_questions():
            self.window.after(BLINK_LENGTH_MS, self.next_question)
        else:
            end_text = "Congratulations!\nYou've completed the quiz!"
            self.window.after(
                BLINK_LENGTH_MS,
                lambda: self.update_text(end_text)
                )

    def blink_color_canvas(self, color: str):
        self.canvas.config(bg=color)
        self.window.after(
            BLINK_LENGTH_MS,
            lambda: self.canvas.config(bg="white")
            )


if __name__ == "__main__":
    quiz = QuizBrain([Question("Empty text", "True")])
    app = QuizInterface(quiz)
