# FLASH CARD PROGRAM
# Uses words from a CSV file to show flash cards, the user has to say if they
# recalled the correct word and through that a selection is done.
# ----------------------------------------------------------------------------
# [X] Add canvas for card
# [X] Add buttons
# [X] Rotation between languages function
# [ ] Correct guess function
# [ ] Wrong guess function
# [X] Load data from csv
# [ ] Save data to csv for next usage

import pandas as pd
import os
import tkinter as tk
from random import randint, choice

# CONSTANTS
DATA_FOLDER = "data"
VOCABULARY = "words_to_learn.csv"
VOCABULARY_INIT = "french_words.csv"
LANGUAGE_TO_LEARN = "French"
LANGUAGE_BASE = "English"
IMAGES_FOLDER = "images"
IMAGE_CARD_BACK = "card_back.png"
IMAGE_CARD_FRONT = "card_front.png"
IMAGE_BUTTON_RIGHT = "right.png"
IMAGE_BUTTON_WRONG = "wrong.png"
FONT_WORD = ("Arial", 60, "bold")
FONT_LANGUAGE = ("Arial", 40, "italic")
COLOR_BACKGROUND = "#B1DDC6"

# # Convert original txt file into csv
# WORDS = 100
# LANGUAGE = "es"
# cwd = os.path.dirname(os.path.relpath(__file__))
# list_path = cwd + f"/{LANGUAGE}_50k.txt"
# with open(list_path, "r", encoding="utf-8") as f:
#     words_list = list()
#     for _ in range(WORDS):
#         line = f.readline()
#         words_list.append(line.split()[0])
# s = pd.Series(words_list, name=LANGUAGE)
# s.to_csv(cwd + f"/{LANGUAGE}_{WORDS}.csv", encoding="utf-8", index=False)

# INITIALIZATION FOR GLOBAL PARAMETERS
# ID for scheduled card flip
auto_flip = ""
# Current card idx from the dataset
current_card_idx = -1


def update_word():
    """Updates the word shown on the flashcard by returning to the front of
    the card with a new word from the language that one is reviewing."""
    global auto_flip
    global current_card_idx
    # At the initialization the auto_flip is None
    try:
        window.after_cancel(auto_flip)
    except ValueError:
        pass
    # BUG: somehow random choice from the index sometimes returns an index
    # that the dataframe considers not available, however it appears within
    # the dataframe, the element that is dropped at the 'correct_guess'
    # function is correctly removed and I am not sure why this happens
    current_card_idx = choice(vocabulary.index)
    # Updates the image and text on the canvas
    canvas.itemconfig(
        background_image,
        image=card_front_background,
        )
    canvas.itemconfig(
        word,
        text=vocabulary.iloc[current_card_idx][LANGUAGE_TO_LEARN],
        fill="black",
        )
    canvas.itemconfig(
        language,
        text=LANGUAGE_TO_LEARN,
        fill="black",
        )
    # Schedules the flip_card function
    auto_flip = window.after(ms=3000, func=flip_card)


def flip_card():
    """Shows the back of the current card, with its translation"""
    canvas.itemconfig(
        background_image,
        image=card_back_background,
        )
    canvas.itemconfig(
        word,
        text=vocabulary.iloc[current_card_idx][LANGUAGE_BASE],
        fill="white",
        )
    canvas.itemconfig(
        language,
        text=LANGUAGE_BASE,
        fill="white",
        )


def correct_guess():
    """Removes the word from the dictionary"""
    vocabulary.drop(current_card_idx, inplace=True)
    update_word()


cwd = os.path.dirname(os.path.relpath(__file__))

# Load vocabulary from data
vocabulary_path = os.path.join(cwd, DATA_FOLDER, VOCABULARY)
try:
    vocabulary = pd.read_csv(vocabulary_path, header=0)
except FileNotFoundError:
    init_vocabulary_path = os.path.join(cwd, DATA_FOLDER, VOCABULARY_INIT)
    vocabulary = pd.read_csv(init_vocabulary_path, header=0)

window = tk.Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=COLOR_BACKGROUND)

# Canvas containing the card
canvas = tk.Canvas(width=800, height=526, bg=COLOR_BACKGROUND, highlightthickness=0)
card_front_path = os.path.join(cwd, IMAGES_FOLDER, IMAGE_CARD_FRONT)
card_front_background = tk.PhotoImage(file=card_front_path)
card_back_path = os.path.join(cwd, IMAGES_FOLDER, IMAGE_CARD_BACK)
card_back_background = tk.PhotoImage(file=card_back_path)
background_image = canvas.create_image((400, 263), image=card_front_background)
canvas.grid(row=0, column=0, columnspan=2)

# Word and language
language = canvas.create_text(400, 150, text="", font=FONT_LANGUAGE)
word = canvas.create_text(400, 263, text="", font=FONT_WORD)
update_word()

# Right/Wrong buttons
right_button_path = os.path.join(cwd, IMAGES_FOLDER, IMAGE_BUTTON_RIGHT)
wrong_button_path = os.path.join(cwd, IMAGES_FOLDER, IMAGE_BUTTON_WRONG)
right_button_image = tk.PhotoImage(file=right_button_path)
wrong_button_image = tk.PhotoImage(file=wrong_button_path)
right_button = tk.Button(image=right_button_image, highlightthickness=0)
right_button.grid(row=1, column=1)
right_button.config(command=correct_guess)
wrong_button = tk.Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
wrong_button.config(command=update_word)


window.mainloop()

save_file_path = os.path.join(cwd, DATA_FOLDER, VOCABULARY)
vocabulary.to_csv(save_file_path, encoding="utf-8", index=False)