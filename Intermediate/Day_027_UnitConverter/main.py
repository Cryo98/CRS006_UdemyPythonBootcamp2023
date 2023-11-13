# MILES-TO-KM CONVERTER
# Simple GUI to convert miles into kilometers
#
# GUI structure:
#               | Entry  | Miles
#   is equal to | Result | Km
#               | Button |

import tkinter as tk


window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=10)

miles_value = tk.Entry(width=8)
miles_value.grid(row=0, column=1)

miles_text = tk.Label(text="Miles")
miles_text.grid(row=0, column=2)

is_equal_to_text = tk.Label(text="is equal to")
is_equal_to_text.grid(row=1, column=0)

kilometers_value = tk.Label(text=0)
kilometers_value.grid(row=1, column=1)

kilometers_text = tk.Label(text="Km")
kilometers_text.grid(row=1, column=2)


def convert_miles_to_km():
    miles_str = miles_value.get()
    if miles_str != "":
        miles = float(miles_str)
        kilometers = miles * 1.609
        kilometers_value.config(text=f"{round(kilometers, 1)}")
    else:
        kilometers_value.config(text=0)


calculate_button = tk.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)


window.mainloop()
