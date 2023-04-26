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

first_choice = input("You wake up on the coast of an island after your ship sunk. You see a decrepit house and a cave. Which one will you enter?\n-> Cave\n-> House\n ")

first_choice_lower = first_choice.lower()

if first_choice_lower == "house":
    house_choice = input("You enter the house and see a red and green door. which will you choose?\n-> red\n-> green\n")
    house_choice_lower = house_choice.lower()
    if house_choice_lower == "red":
        print("GAME OVER! You are trapped")
    else:
        print("You walk in the room and it is full of treasure! YOU WON!")
else:
    cave_choice = input("You enter the cave and there are two paths. left and right. Which will you take?\n-> left\n-> right\n")
    cave_choice_lower = cave_choice.lower()
    if cave_choice_lower == "left":
        print("GAME OVER! You fall into a spike trap!")
    else:
        print("GAME OVER! You get eaten by an angry bear")
