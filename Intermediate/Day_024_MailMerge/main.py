# MAIL MERGE
# Generates letters with custom names based on a template and a list of names
# saved in files.
# ---------------------------------------------------------------------------
# [X] Load names
# [X] Load letter template
# [X] Substitute name within letter
# [X] Save customized letters in folder

import os

# CONSTANTS
# Where letter template is
NAMES_FOLDER_PATH = "./Input/Names/"
LETTERS_FOLDER_PATH = "./Input/Letters/"
PLACEHOLDER = "[name]"
# Where names list is
NAMES_FILE = "invited_names.txt"
LETTER_FILE = "starting_letter.txt"
# Where the custom letter should be
OUTPUT_FOLDER = "./Output/ReadyToSend/"
OUTPUT_FILE = f"letter_for_{PLACEHOLDER}.txt"


def main():
    # Extract file directory
    cwd = os.path.dirname(os.path.relpath(__file__))

    # Extract names from file
    names_path = cwd + NAMES_FOLDER_PATH + NAMES_FILE
    with open(names_path, "r") as f_names:
        names = list()
        for name in f_names.readlines():
            name = name.strip("\n")
            names.append(name)

    # Load letter template
    letter_template_path = cwd + LETTERS_FOLDER_PATH + LETTER_FILE
    with open(letter_template_path, "r") as f_templ:
        template = f_templ.read()

    # Customize letter and save
    for name in names:
        output_file = OUTPUT_FILE.replace(PLACEHOLDER, name)
        custom_letter = template.replace(PLACEHOLDER, name)
        output_path = cwd + OUTPUT_FOLDER + output_file
        with open(output_path, "w") as f_out:
            f_out.write(custom_letter)


if __name__ == "__main__":
    main()
