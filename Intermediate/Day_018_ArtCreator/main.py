import colorgram
import turtle as t
import random

# Extracts the first N most common colors from the given image
# image source: https://www.vangoghgallery.com/img/starry_night_full.jpg
colors_obj = colorgram.extract("starry_night_full.jpg", 20)
# Converts the Color object from colorgram into a list of tuples usable by
# turtle
colors_rgb = list()
for color_obj in colors_obj:
    colors_rgb.append(color_obj.rgb)

# Number of rows and columns of dots
SIZE = (10, 10)
# Space between each dot
SPACING = 50
# Average size of dot
DOT_SIZE = 20

# Initialize turtle and its properties
timmy = t.Turtle()
timmy.hideturtle()
t.colormode(255)
timmy.speed("fastest")
timmy.penup()

# Sets the center of the drawing to the center of the window
# NOTE: the center of the window has coordinates (0, 0)
offset_x = -(SPACING*(SIZE[0]-1))/2
offset_y = -(SPACING*(SIZE[1]-1))/2
timmy.setpos(offset_x, offset_y)

# Loop to draw the dots
for _ in range(SIZE[1]):
    for _ in range(SIZE[0]):
        timmy.color(random.choice(colors_rgb))
        # Randomize dot size in range [50%, 150%)
        dot_multiplier = (0.5 + random.random())
        timmy.dot(DOT_SIZE*dot_multiplier)
        timmy.forward(SPACING)
    # Return to beginning of the line and goes up one line
    timmy.setheading(180)
    timmy.forward(SPACING*SIZE[0])
    timmy.setheading(90)
    timmy.forward(SPACING)
    timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()
