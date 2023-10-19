def main():
    print_treasure()
    print("Welcome to the Treasure Island!")
    print("You have to find the treasure hidden within the island, where do you want to go? Type 'left' or 'right'")
    direction_1 = input("> ").lower()
    if direction_1 == "left":
        print("There was an hidden trap, you felt inside it!")
        print("Game over")
    else:
        print("You come across a river flowing fast, what do you want to do? Type 'cross' or 'search'")
        direction_2 = input("> ").lower()
        if direction_2 == "cross":
            print("The current was too strong! You tried to fight it but it brought you to the sea.")
            print("Game over")
        else:
            print("After walking for a bit you find a point where you can ford it, good job!")
            print("In front of you you see three holes into which you can lower yourself down, which one do you want to try? Type 'left', 'middle' or 'right'")
            direction_3 = input("> ").lower()
            if direction_3 == "left":
                print("The hole is incredibly deep, you start to feel heat coming from underneath, and before you can notice it the lava is at your feet.")
                print("Game over")
            elif direction_3 == "right":
                print("You find yourself in an extremely big cave, you start exploring it.")
                print("What could be hours pass, and you find yourself back at the beginning, and from the anger you scream.")
                print("The echo makes the cavern tremble, and a huge rock falls and blocks the entrance.")
                print("Game over")
            else:
                print("A glimmering light hurts your eyes, mountains of gold and jewelry are in front of you.")
                print_jewel()
                print("You did it! You've found the island's treasure!")


def print_treasure():
    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
    
def print_jewel():
    print('''                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
      jgs     . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .''')


if __name__ == '__main__':
    main()
