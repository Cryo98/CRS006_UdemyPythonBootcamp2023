import requests

TRIVIA_DATABASE_ENDPOINT = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_questions(n_questions: int = 10, type: str = "boolean"):
    parameters = {
        "amount": n_questions,
        "type": type,
    }

    response = requests.get(url=TRIVIA_DATABASE_ENDPOINT, params=parameters).json()
    # questions = [{"text": question["question"], "answer": question["correct_answer"]} for question in response["results"]]
    questions = response["results"]
    return questions


if __name__ == "__main__":
    print(get_questions(n_questions=5))
