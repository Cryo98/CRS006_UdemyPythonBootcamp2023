# NATO PHONETIC ALPHABET
# Converts a given word into the spelled version with the NATO phonetic
# alphabet
# ---------------------------------------------------------------------
# [X] Load phonetic alphabet
# [X] Convert the alphabet into a dictionary with dict comprehension
# [X] Get user input
# [X] Convert input into phonetic list
# [X] Add KeyError handling for non-alphabetical input

import os
import pandas as pd

# CONSTANTS
ALPHABET_FILE = "nato_phonetic_alphabet.csv"


# Load phonetic alphabet into dictionary
cwd = os.path.dirname(os.path.relpath(__file__))
alphabet_path = cwd + "/" + ALPHABET_FILE
phonetic_alphabet_df = pd.read_csv(alphabet_path)
alphabet_dict = {row["letter"]: row["code"] for (index, row) in phonetic_alphabet_df.iterrows()}

# Convert user input into phonetic
is_running = True
while is_running:
    try:
        user_input = input("What word you want to spell?: ").upper()
        spelled_input = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_running = False
print(spelled_input)
