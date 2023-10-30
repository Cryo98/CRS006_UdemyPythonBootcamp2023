import random

# Ascii arts for rock, paper and scissors hand gestures
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def main():
    # Combines the ascii arts in a list for easier access
    graphics = [ROCK, PAPER, SCISSORS]
    # Handles input and printing of choice
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    selection = int(input())
    print(graphics[selection])
    # Selects randomly the action for the computer
    pc_selection = random.randint(0, 2)
    print("The computer chose:")
    print(graphics[pc_selection])
    # Checks whether your selection is after the computer selection, as in this
    # each element wins on the previous one
    if selection == pc_selection + 1 or selection == pc_selection - 2:
        print("You win!")
    # Similar but checks the reversed condition (computer winning)
    elif pc_selection == selection + 1 or pc_selection == selection - 2:
        print("You lose!")
    else:
        print("Draw!")


if __name__ == '__main__':
    main()
