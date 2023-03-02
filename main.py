print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You enter a cave on the deserted island")
print("As you enter you see two paths")

path_choice = input("Which path do you choose? left or right?(choose left or right)\n")
if path_choice.lower() == "right":
    print("You enter the path through the right and it caves in on top of you")
    print("YOU DIED")
elif path_choice.lower() == "left":
    print("You progress through the left path and it eventually leads you outside, "
          "you find yourself at the edge of a river just outside the cave")
    river_choice = input("The river is choppy and is moving very fast, "
                         "do you risk it and swim to the other side or do you wait and hope a boat comes by?"
                         "(choose swim or wait)\n")
    if river_choice == 'swim':
        print("You try to swim across the river but its current is too strong and you get swept under.")
        print("YOU DIED")
    elif river_choice == "wait":
        print("You wait by river until a fishing boat sails by and stops, the fishman agrees to help you across")
        print("After you cross the the river you enter an abandoned stronghold")
        door_choice = input("Within the stronghold there are three doors ahead."
                            " Red, Yellow, and Blue. Which do you choose?\n")
        if door_choice.lower() == "red":
            print("You enter the room only for the ceiling to cave in onto of you.")
            print("YOU DIED")
        elif door_choice.lower() == "yellow":
            print("You open the door and see a chest, you walk up and open it.....")
            print("CONGRATULATIONS!! YOU FOUND THE TREASURE!!")
        elif door_choice.lower() == "blue":
            print("You open the door and see a chest, you walk up and open it.....")
            print("But once you do the chest suddenly grows arms, legs and teeth. "
                  "It grabs you and swallows you whole in seconds!")
            print("YOU DIED")
