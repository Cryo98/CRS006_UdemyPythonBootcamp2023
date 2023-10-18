# NOTE: This script works within the Reeborg environment found at
# https://reeborg.ca/, specifically the Maze challenge
# (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
# and will therefore not work in a normal python IDE.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def follow_right(right_turns:int):
    # Tries to follow the wall on the right, but if it turns in a circle it
    # goes another direction.
    if right_is_clear() and right_turns < 4:
        turn_right()
        move()
        return right_turns + 1
    elif front_is_clear():
        move()
        return 0
    else:
        turn_left()
        return 0
       
right_turns = 0
while not at_goal():
    right_turns = follow_right(right_turns)