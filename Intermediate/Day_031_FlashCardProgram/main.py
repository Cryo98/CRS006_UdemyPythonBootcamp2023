# FLASH CARD PROGRAM
# Uses words from a CSV file to show flash cards, the user has to say if they
# recalled the correct word and through that a selection is done.
# ----------------------------------------------------------------------------
# [X] Add canvas for card
# [X] Add buttons
# [ ] Rotation between languages function
# [ ] Correct guess function
# [ ] Wrong guess function
# [ ] Load data from csv

import pandas as pd
import os
import tkinter as tk
from random import randint

# CONSTANTS
DATA_FOLDER = "data"
VOCABULARY = "french_words.csv"
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


def update_word():
    n_words = vocabulary.shape[0]
    selected_language = "French"
    idx = randint(0, n_words)
    canvas.itemconfig(word, text=vocabulary.iloc[idx][selected_language])
    canvas.itemconfig(language, text=selected_language)


cwd = os.path.dirname(os.path.relpath(__file__))

# Load vocabulary from data
vocabulary_path = os.path.join(cwd, DATA_FOLDER, VOCABULARY)
vocabulary = pd.read_csv(vocabulary_path, header=0)

window = tk.Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=COLOR_BACKGROUND)

# Canvas containing the card
canvas = tk.Canvas(width=800, height=526, bg=COLOR_BACKGROUND, highlightthickness=0)
card_front_path = os.path.join(cwd, IMAGES_FOLDER, IMAGE_CARD_FRONT)
card_background = tk.PhotoImage(file=card_front_path)
canvas.create_image((400, 263), image=card_background)
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
right_button.config(command=update_word)
wrong_button = tk.Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
wrong_button.config(command=update_word)


window.mainloop()
