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
user_input = input("What word you want to spell?: ").upper()
spelled_input = [alphabet_dict[letter] for letter in user_input]
print(spelled_input)
