# POMODORO TIMER
# A simple timer for short work sessions of 25 minutes, following the
# "Pomodoro Technique".
# ----------------------
# GUI structure:
#       |   Timer    |
#       |   Canvas   |
# Start |            | Reset
#       | Checkmarks |
# ----------------------
# FOR FUTURE
# TODO Make start of break done through button
# TODO Improve graphics
# TODO Add alarm for countdown end
# TODO Clean timer countdown function (class?)

import tkinter as tk
import os

# CONSTANTS
COLOR_BG = "#FF9130"
FONT_NAME_TIME = "Courier"
FONT_NAME_TEXT = "Arial"
FONT_NAME_CHECKMARKS = "Arial"
FONT_SIZE_TIME = 36
FONT_SIZE_TEXT = 40
FONT_SIZE_CHECKMARKS = 20
FONT_TYPE_TIME = "bold"
FONT_TYPE_TEXT = "normal"
FONT_TYPE_CHECKMARKS = "normal"
FONT_TIME = (FONT_NAME_TIME, FONT_SIZE_TIME, FONT_TYPE_TIME)
FONT_TEXT = (FONT_NAME_TEXT, FONT_SIZE_TEXT, FONT_TYPE_TEXT)
FONT_CHECKMARKS = (FONT_NAME_CHECKMARKS, FONT_SIZE_CHECKMARKS, FONT_TYPE_CHECKMARKS)
IMAGE_POMODORO_FILE = "tomato.png"
TIME_WORK_SESSION_MIN = 25
TIME_SHORT_BREAK_MIN = 5
TIME_LONG_BREAK_MIN = 20
SYMBOL_CHECKMARK = "☑"

# Initialize timer to access it later globally
timer = None
# Initializes number of repetitions
n_repetitions = 0


def start_session():
    """Starts a full 4-stages Pomodoro session, with four 25-minutes study
    session, three 5-minutes breaks and one long 20-minutes final break."""
    global n_repetitions
    n_repetitions += 1
    if n_repetitions == 8:
        timer_countdown(TIME_LONG_BREAK_MIN)
        timer_label.config(text="Break!", fg="red")
        n_repetitions = 0
    elif n_repetitions % 2 == 0:
        timer_countdown(seconds=TIME_SHORT_BREAK_MIN)
        timer_label.config(text="Break!", fg="yellow")
    else:
        timer_countdown(seconds=TIME_WORK_SESSION_MIN)
        timer_label.config(text="Work...", fg="green")


def timer_countdown(minutes: int = 0, seconds: int = 0):
    """Counts down the timer from the given input, calling itself iteratively
    until it reaches 0. It automatically updates the canvas text and the
    checkmarks."""
    global n_repetitions
    global timer

    if seconds < 0:
        minutes -= 1
        seconds += 60
    else:
        # Handles inputs with high seconds number
        while seconds >= 60:
            minutes += 1
            seconds -= 60
    canvas.itemconfig(timer_text, text=f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    if minutes > 0 or seconds > 0:
        timer = window.after(1000, timer_countdown, minutes, seconds - 1)
    else:
        if n_repetitions % 2 != 0:
            prev_checkmarks = checkmarks_label.cget("text")
            checkmarks_label.config(text=prev_checkmarks + SYMBOL_CHECKMARK)
        elif n_repetitions == 0:
            checkmarks_label.config(text="")
        start_session()


def reset_timer():
    """Resets all the parameters to their initial values and stops the
    scheduled timer_countdown function."""
    global n_repetitions
    window.after_cancel(timer)
    n_repetitions = 0
    checkmarks_label.config(text="")
    timer_label.config(text="Timer", fg="white")
    canvas.itemconfig(timer_text, text="00:00")


window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=COLOR_BG)

# Timer label
timer_label = tk.Label(text="Timer", font=FONT_TEXT, fg="white", bg=COLOR_BG)
timer_label.grid(row=0, column=1)

# Add image to GUI
cwd = os.path.dirname(os.path.relpath(__file__))
image_pomodoro_path = cwd + "/" + IMAGE_POMODORO_FILE
# Size approximately the same of image
canvas = tk.Canvas(width=200, height=224, bg=COLOR_BG, highlightthickness=0)
image = tk.PhotoImage(file=image_pomodoro_path)
# The image is not perfectly centered
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 112+FONT_SIZE_TIME/2, fill="white", text="00:00", font=FONT_TIME)
canvas.grid(row=1, column=1)

# Start button
start_button = tk.Button(text="Start", width=10)
start_button.grid(row=2, column=0)
start_button.config(command=start_session)

# Reset button
reset_button = tk.Button(text="Reset", width=10)
reset_button.grid(row=2, column=2)
reset_button.config(command=reset_timer)

# Checkmarks label
checkmarks_label = tk.Label(text="", fg="green", bg=COLOR_BG, font=FONT_TYPE_CHECKMARKS)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
