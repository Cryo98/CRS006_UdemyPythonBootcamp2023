import random
from Day_012_NumberGuesserGame_resources import LOGO

# Global constants used for easy parameters change
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
MAX_NUMBER = 100
DEBUG = True


def select_difficulty():
    """Asks the user for a difficulty level and returns the amount of attempts
    available"""
    difficulty = ""
    while difficulty != "hard" and difficulty != "easy":
        difficulty_raw = input("Choose a difficulty, type 'easy' or 'hard': ")
        difficulty = difficulty_raw.lower()
        if difficulty != "hard" and difficulty != "easy":
            print("Sorry, I didn't understand, please try again...")
    # Values are set through global parameters
    if difficulty == "easy":
        attempts = EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        attempts = HARD_LEVEL_ATTEMPTS
    return attempts


def reduce_attempts(attempts):
    """Reduces the number of attempts and prints the current ones."""
    attempts -= 1
    print(f"You have {attempts} attempts remaining...")
    return attempts


def compare_numbers(a, b):
    """Compare numbers and prints relative position.
    It returns True if the numbers are equal, else False."""
    if a == b:
        return True
    elif a > b:
        print("Guess too high.")
    else:
        print("Guess too low.")
    return False

def is_number_out_of_range(number):
    """Check if the number is out of range of the available numbers"""
    return number <= 0 or number > MAX_NUMBER


# Print intro
print(LOGO)
print("Welcome to the number guesser game!")
print("I'm thinking about a number between 1 and", MAX_NUMBER)
# Select a random number
selected_number = random.randint(1, MAX_NUMBER)
if DEBUG:
    print(f"Psst, the number is {selected_number}.")
# Select attempts based on difficulty
attempts = select_difficulty()
print(f"You have {attempts} attempts to guess the number, good luck!")
# Game loop until it is guessed or attempts are out
isGuessed = False
while not isGuessed and attempts > 0:
    guessed_number = 0
    while is_number_out_of_range(guessed_number):
        guessed_number = int(input("Guess a number: "))
        if is_number_out_of_range(guessed_number):
            print("Not even close, remember that I am thinking of a number between 0 and", MAX_NUMBER)
    isGuessed = compare_numbers(guessed_number, selected_number)
    # If it is not guessed reduce attempts available
    if not isGuessed:
        attempts = reduce_attempts(attempts)
# Result messages
if isGuessed:
    print("Congratulations! You guessed the number!")
else:
    print("Nice try, but you ran out of attempts.")
print(f"The number was {selected_number}.")
