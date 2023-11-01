from turtle import Turtle, Screen
import turtle as t
import turtle_moves as tm


timmy = Turtle()

# Challenge 1: Draw a square
# tm.draw_square(timmy)

# Challenge 2: Draw a dashed line
# tm.draw_dashed_line(timmy, length=100, spacing=2)

# Challenge 3: Draw all polygons from triangle to decagon using different
# colors
# for i in range(3, 11):
#     timmy.color(f"gray{i-2}0")
#     tm.draw_n_polygon(timmy, i)

# Challenge 4: Draw in a random walk manner (cardinal) using random colors,
# wider line and faster drawing speed
# t.colormode(255)
# timmy.speed(0)
# timmy.pensize(8)
# tm.random_walk(timmy, random_colors=True, step_size=20, max_steps=300)

# Challenge 5: Draw a spirograph
# segments = 80
# timmy.speed(0)
# angle_step = 360/segments
# for steps in range(segments):
#     timmy.color(tm.generate_random_color(1))
#     timmy.setheading(steps*angle_step)
#     timmy.circle(100)

screen = Screen()
screen.exitonclick()
