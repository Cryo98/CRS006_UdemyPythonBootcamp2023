class QuizBrain:

    def __init__(self, questions_list) -> None:
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        question_string = self.format_question(current_question)
        answer = input(question_string)
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def format_question(self, question) -> str:
        return f"Q.{self.question_number}: {question.text} (True/False)?: "
