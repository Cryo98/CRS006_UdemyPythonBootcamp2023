from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in get_questions(10):
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

app = QuizInterface()

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
