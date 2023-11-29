import requests

TRIVIA_DATABASE_ENDPOINT = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_questions(n_questions: int = 10, type: str = "boolean"):
    parameters = {
        "amount": n_questions,
        "type": type,
    }

    response = requests.get(url=TRIVIA_DATABASE_ENDPOINT, params=parameters)
    response_json = response.json()
    questions = response_json["results"]
    return questions


if __name__ == "__main__":
    print(get_questions(n_questions=5))
