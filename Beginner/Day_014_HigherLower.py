# HIGHER-LOWER
# A game where two celebrities are compared and the user has to guess which
# one has more followers on Instagram.
# -------------------------------------------------------------------------
# Code functionalities:
#    - [X] Show title
#    - [X] ~~Select two random celebrities from the data~~
#    - [X] Select a random entry from the data list
#    - [X] Print the comparison
#    - [X] Compare user's answer with actual answer
#    - [X] Handle scoring system
#    - [X] Game loop
#    - [X] Get user's answer for comparison
#    - [X] Loop for winning
#    - [X] Print result messages
#    - [X] Handle emptied list


from Day_014_HigherLower_resources import LOGO, VS, DATA
from random import randint
import os

DEBUG = False


def higher_lower():
    # To restart the game
    is_game_running = True
    # To continue the game after correct answer
    is_answer_correct = True
    while is_game_running:
        score = 0
        data = DATA.copy()
        previous_entry = None
        print(LOGO)
        print("================================")
        while is_answer_correct:
            # Uses the previous winner if exists
            if previous_entry is None:
                entry_1 = select_random_entry(data)
            else:
                entry_1 = previous_entry
            # NOTE: each time a new entry is picked, that same entry
            # is removed from the list of available entries
            entry_2 = select_random_entry(data)
            print_comparison(entry_1, entry_2)
            print(f"\nCurrent score: {score}\n")
            if DEBUG:
                print(f"Psst, A has {entry_1['follower_count']}M and B has {entry_2['follower_count']}M followers.")
            response = get_user_answer_to_comparison()
            is_answer_correct, previous_winner = validate_response(response, entry_1, entry_2)
            clear_screen()
            print(LOGO)
            print("================================")
            if is_answer_correct:
                score += 1
                print_correct_answer_message(previous_winner)
            else:
                print_losing_message(previous_winner, score)
            if len(data) == 0:
                print_winning_message(previous_winner, score)
                is_answer_correct = False
            previous_entry = entry_2
        is_game_running = get_user_answer_to_retry()
        if is_game_running:
            # Resets the game loop
            is_answer_correct = True
    print("Goodbye!")


def clear_screen() -> None:
    """Clears the output window."""
    os.system("cls")


def select_random_entry(
        data: list[dict]
        ) -> dict:
    """Selects two different random entries from the imported database.
    Outputs them as a tuple of dictionaries"""
    idx = randint(0, len(data)-1)
    entry = data.pop(idx)
    return entry


def print_comparison(
        entry_1: dict,
        entry_2: dict,
        ) -> None:
    """Pretty print of the comparison between the two entries.
    It assumes that the entries are dictionaries containing the parameters
    'name', 'description' and 'country'."""
    vocals = ['A', 'E', 'I', 'O', 'U']
    article_1 = 'an' if entry_1['description'][0] in vocals else 'a'
    article_2 = 'an' if entry_2['description'][0] in vocals else 'a'
    print(f"Compare A: {entry_1['name']},",
          f"{article_1} {entry_1['description']} from {entry_1['country']}.")
    print(VS)
    print(f"Against B: {entry_2['name']},",
          f"{article_2} {entry_2['description']} from {entry_2['country']}.")


def get_user_answer_to_comparison() -> str:
    """Asks the user for an answer regarding who has most followers.
    The accepted answers are 'A' and 'B', both case-insensitive."""
    isAnswered = False
    print("Who has more followers?", end=' ')
    while not isAnswered:
        response = input("Type 'A' or 'B': ").upper()
        if response == "A" or response == "B":
            isAnswered = True
        else:
            print("Sorry I didn't understand the answer, please try again.")
    return response


def get_user_answer_to_retry() -> str:
    """Asks the user for an answer regarding if they want to retry the game,
    and returns True if they want, else False.
    The accepted answers are 'y' and 'n', both case-insensitive."""
    isAnswered = False
    print("Do you want to try again?", end=' ')
    while not isAnswered:
        response = input("Type 'y' or 'n': ").lower()
        if response == "y" or response == "n":
            isAnswered = True
        else:
            print("Sorry I didn't understand the answer, please try again.")
    if response == "y":
        return True
    else:
        return False


def validate_response(
        response: str,
        entry_1: dict,
        entry_2: dict,
        ) -> tuple[bool, dict]:
    """Validates the response from the user by comparing the values in the
    entries, and returning True if the answer is correct, else False, and
    returning the entry with the highest value.
    It assumes both the entries have a 'follower_count' parameter."""
    if entry_1['follower_count'] > entry_2['follower_count']:
        correct_answer = "A"
        winning_entry = entry_1
    else:
        correct_answer = "B"
        winning_entry = entry_2
    return response == correct_answer, winning_entry


def print_losing_message(
        winning_entry: dict,
        score: int,
        ) -> None:
    """Prints a message when the player loses."""
    print(f"Too bad, the answer was {winning_entry['name']}.")
    print(f"You lost, you scored {score} points.")


def print_correct_answer_message(
        winning_entry: dict,
        ) -> None:
    """Prints a message when the player has guessed correctly."""
    print("You got it!")
    print(f"{winning_entry['name']} has",
          f"{winning_entry['follower_count']}M followers!")


def print_winning_message(
        winning_entry: dict,
        score: int
    ) -> None:
    """Prints a message when the player has guessed all the correct answers."""
    print("Incredible, you got them all right!")
    print("The page with the most followers is",
          f"{winning_entry['name']},",
          f"with {winning_entry['follower_count']}M followers.")
    print(f"Your total score is {score}!")


if __name__ == '__main__':
    higher_lower()
