# POMODORO TIMER
# A simple timer for short work sessions of 25 minutes, following the
# "Pomodoro Technique".
# ----------------------
# GUI structure:
#       |   Timer    |    
#       |   Canvas   |
# Start |            | Reset
#       | Checkmarks |

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


window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=COLOR_BG)

# Timer label
timer_label = tk.Label(text="Timer", font=FONT_TEXT, fg="red", bg=COLOR_BG)
timer_label.grid(row=0, column=1)

# Add image to GUI
cwd = os.path.dirname(os.path.relpath(__file__))
image_pomodoro_path = cwd + "/" + IMAGE_POMODORO_FILE
# Size approximately the same of image
canvas = tk.Canvas(width=200, height=224, bg=COLOR_BG, highlightthickness=0)
image = tk.PhotoImage(file=image_pomodoro_path)
# The image is not perfectly centered
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 112+FONT_SIZE_TIME/2, fill="white", text="00:00", font=FONT_TIME)
canvas.grid(row=1, column=1)

# Start button
start_button = tk.Button(text="Start", width=10)
start_button.grid(row=2, column=0)

# Reset button
reset_button = tk.Button(text="Reset", width=10)
reset_button.grid(row=2, column=2)

# Checkmarks label
checkmarks_label = tk.Label(text=SYMBOL_CHECKMARK, fg="green", bg=COLOR_BG, font=FONT_TYPE_CHECKMARKS)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
