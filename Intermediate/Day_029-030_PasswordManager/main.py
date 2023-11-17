# PASSWORD MANAGER
# Small program with GUI that allows to save passwords locally for a given
# site, while also giving access to a random generator and copy to clipboard
# the password.
# ---------------------------------------------------------------------------
# [X] Add logo
# [X] Add GUI elements
# [X] Generate random password
# [X] Save data into file as JSON
# [X] Save password into clipboard
# [X] Add search function

import tkinter as tk
from tkinter import messagebox
import os
import random
import pyperclip
import json


# CONSTANTS
LOGO_FILE = "logo.png"
LOGO_WIDTH = 200
LOGO_HEIGHT = 200
PADDING = 50
# Email inserted at program opening
COMMON_EMAIL = "test@testmail.com"
DATABASE_FILE = "database.txt"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Amount of letters, symbols and numbers to be picked during password
# generation
PASSWORD_N_LETTERS = 10
PASSWORD_N_NUMBERS = 3
PASSWORD_N_SYMBOLS = 1


def save_credentials():
    """Save credentials into a local database."""
    database_path = cwd + "/" + DATABASE_FILE
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Error message for empty fields
    if password == "" or email == "" or website == "":
        messagebox.showerror(
            title="Missing credentials",
            message="Please fill all the credentials.")
        return

    # Confirmation requested
    confirmed_save = messagebox.askokcancel(
        title=website,
        message=f"These are the credentials entered\n"
        f"Email: {email}\nPassowrd: {password}\n"
        f"Do you want to save them?")

    # Saving credentials in the database and clearing GUI elements
    if confirmed_save:
        # Handles non-existent file
        try:
            with open(database_path, "r") as db:
                data = json.load(db)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        with open(database_path, "w") as db:
            json.dump(data, db, indent=4)
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        messagebox.showinfo(
            title="Save completed",
            message="The credentials have been saved in the database.")


def generate_password():
    """Generate a random password.

    It generates a random password with letters, symbols and numbers in a
    randomized order, inserting it into the password entry element of the GUI
    and saving it into the clipboard to be pasted directly.
    The amount of letters, symbols and numbers are based on the constants at
    the beginning of the scripts."""
    password_list = [random.choice(LETTERS) for _ in range(PASSWORD_N_LETTERS)]
    symbols_list = [random.choice(SYMBOLS) for _ in range(PASSWORD_N_SYMBOLS)]
    numbers_list = [random.choice(NUMBERS) for _ in range(PASSWORD_N_NUMBERS)]
    password_list.extend(symbols_list)
    password_list.extend(numbers_list)
    random.shuffle(password_list)
    password_str = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_str)
    pyperclip.copy(password_str)


def search_database():
    """Search within the database for password and email for the website
    present in the website entry.

    It loads from the database, showing an error window if the database has
    yet to be created.
    Loading and searching within the data, it shows an info window if the
    credentials for the required website are not available, else it copies
    the credentials in the entries and the password within the clipboard.
    """
    database_path = cwd + "/" + DATABASE_FILE
    website = website_entry.get().title()
    try:
        with open(database_path, "r") as db:
            data = json.load(db)
    except FileNotFoundError:
        messagebox.showerror(
            title="Empty Database",
            message="The database is currently empty, "
                    "add credentials to start."
        )
    else:
        if website in data:
            website_data = data[website]
            # Inserts loaded data into entries and clipboard
            email_entry.delete(0, tk.END)
            email_entry.insert(0, website_data["email"])
            password_entry.delete(0, tk.END)
            password_entry.insert(0, website_data["password"])
            pyperclip.copy(website_data["password"])
            messagebox.showinfo(
                title="Credentials loaded",
                message=f"Credentials loaded for website '{website}'"
            )
        else:
            messagebox.showinfo(
                title="Unavailable credentials",
                message="No credentials are saved for the website"
                        f" '{website}' within the database."
            )


# Initialize window
cwd = os.path.dirname(os.path.relpath(__file__))
window = tk.Tk()
window.title("Password Manager")
window.config(padx=PADDING, pady=PADDING)

# Logo
canvas = tk.Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT)
logo_path = cwd + "/" + LOGO_FILE
image = tk.PhotoImage(file=logo_path)
canvas.create_image((LOGO_WIDTH/2, LOGO_HEIGHT/2), image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# Entries
website_entry = tk.Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tk.Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, sticky="e")
email_entry.insert(0, COMMON_EMAIL)
password_entry = tk.Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tk.Button(text="Generate Password", width=15)
generate_password_button.grid(row=3, column=2)
generate_password_button.config(command=generate_password)
add_to_database_button = tk.Button(text="Add", width=43)
add_to_database_button.grid(row=4, column=1, columnspan=2, sticky="e")
add_to_database_button.config(command=save_credentials)
search_in_database_button = tk.Button(text="Search", width=15)
search_in_database_button.grid(row=1, column=2)
search_in_database_button.config(command=search_database)

width = window.winfo_width()
height = window.winfo_height()
print(width)
print(height)
window.minsize(width, height)


window.mainloop()
