import random
from Day_007_Hangman_resources import WORD_LIST, STAGES, LOGO


def main():
    print(LOGO)
    chosen_word = select_random_word()
    lives = 6
    # Initializes the word displayed
    display = len(chosen_word)*["_"]
    complete = False
    # Loops until win or losing conditions are met
    while not complete:
        show_word_state(display, lives)
        letter_guessed = ask_input()
        # Checks every letter of the chosen word and compares it with the
        # guess, updating the display
        hasGuessed = False
        if letter_guessed in display:
            print(f"You've already guessed the letter \"{letter_guessed}\", try another one!")
            continue
        else:
            for idx in range(len(chosen_word)):
                if chosen_word[idx] == letter_guessed:
                    display[idx] = letter_guessed
                    hasGuessed = True
            if not hasGuessed:
                print(f"The letter \"{letter_guessed}\" is not in the word.")
                lives -= 1
            else:
                print(f"Good job! The letter \"{letter_guessed}\" is in the word.")
        complete, won = check_win(display, lives)
    print(f"\nThe word was {chosen_word.upper()}\n")
    if won:
        print("You've guessed it!")
    else:
        print("Better luck next time...")
    print("Game over")


def select_random_word() -> str:
    return random.choice(WORD_LIST)


def show_word_state(
        display: list[str],
        lives: int
        ):
    # Displays both the current stage and the guessed letters
    print(STAGES[lives])
    print(" ".join(display))


def ask_input():
    # Asks the user for a letter
    letter_guessed = input("Guess a letter: ").lower()
    return letter_guessed


def check_win(display: list[str], lives: int) -> tuple[bool, bool]:
    # Checks if all the letters have been displayed or if the lives are zero
    if "_" not in display:
        game_completed = True
        game_won = True
    elif lives == 0:
        game_completed = True
        game_won = False
    else:
        game_completed = False
        game_won = False
    return game_completed, game_won


if __name__ == '__main__':
    main()
