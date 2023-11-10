# GEO-NAME GUESSER
# A game where the player has to insert the name of all 50 states of the U.S.
# ---------------------------------------------------------------------------
# [X] Load data of states position
# [X] Get user input
# [X] Compare user input to data
# [X] Add guessed state to map

import turtle as t
import os
import pandas as pd

# CONSTANTS
BACKGROUND_IMAGE = "blank_states_img.gif"
STATES_POSITIONS = "50_states.csv"
FONT_NAME = "Arial"
FONT_SIZE = 8

# Initialize window
screen = t.Screen()
screen.title("Geo-name Guesser (U.S. edition)")

# Load background image
cwd = os.path.dirname(os.path.relpath(__file__))
background_image_path = cwd + "/" + BACKGROUND_IMAGE
screen.addshape(background_image_path)
t.shape(background_image_path)

# Read states location from csv
states_positions_path = cwd + "/" + STATES_POSITIONS
states_data = pd.read_csv(states_positions_path)

score = 0
is_previous_wrong = False
is_previous_already_guessed = False
correct_guesses = list()
# Game loop
while len(correct_guesses) < len(states_data):
    title = f"{score}/{len(states_data)} States Correct"
    # Handles different prompts based on the previous guess
    if is_previous_wrong:
        prompt = "Wrong! Try again, what's another state name?"
    elif is_previous_already_guessed:
        prompt = "You already guessed that, try another"
    elif score > 0:
        prompt = "What's another state name?"
    else:
        prompt = "What's a state name?"

    # Handles user inputs, exiting if input is exited
    user_input = screen.textinput(title=title, prompt=prompt)
    if type(user_input) is str:
        user_input = user_input.title()
    else:
        break

    # Answer evaluation
    if user_input in correct_guesses:
        # Guess already tried, updates the flags
        is_previous_already_guessed = True
        is_previous_wrong = False
    if user_input not in states_data["state"].values:
        # Guess not correct, updates the flags
        is_previous_wrong = True
        is_previous_already_guessed = False
    else:
        # Add guessed state to list to check double entries
        correct_guesses.append(user_input)
        # Create text to the correct spot as per data
        text_turtle = t.Turtle(visible=False)
        text_turtle.penup()
        state_data = states_data[states_data["state"] == user_input]
        x_cor = state_data["x"].values[0]
        y_cor = state_data["y"].values[0]
        text_turtle.goto(x=x_cor, y=y_cor-FONT_SIZE/2)
        text_turtle.write(
            user_input,
            align="center",
            font=(FONT_NAME, FONT_SIZE, "normal"))
        # Track score
        score += 1
        # Update flags
        is_previous_wrong = False

if score == len(states_data):
    print("Good job! You guessed every state!")

t.bye()
