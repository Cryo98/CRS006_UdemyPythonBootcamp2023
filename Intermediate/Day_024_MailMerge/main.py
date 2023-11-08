import os

# CONSTANTS
NAMES_FOLDER_PATH = "./Input/Names/"
LETTERS_FOLDER_PATH = "./Input/Letters/"

NAMES_FILE = "invited_names.txt"
LETTER_FILE = "starting_letter.txt"

OUTPUT_FOLDER = "./Output/ReadyToSend/"


def main():
    cwd = os.path.dirname(os.path.relpath(__file__))
    print(cwd)
    names_path = cwd + NAMES_FOLDER_PATH + NAMES_FILE
    with open(names_path, "r") as f_names:
        names = list()
        for name in f_names.readlines():
            name = name.strip("\n")
            names.append(name)
    print(names)


if __name__ == "__main__":
    main()
