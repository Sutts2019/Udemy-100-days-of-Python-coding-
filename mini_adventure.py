print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1 = input("You are at a junction, do you want to go left or right? \n ").lower()
if choice1 == "left":
    choice2 = input("You have come to a jetty on a river, do you swim across or wait for the ferry?" \n).lower()
    if choice2 == "wait":
        choice3 = input("You cross on the ferry and on the other side, come to a wall with 3 doors - red, yellow, blue. Which door do you take?" \n).lower()
        if choice3 == "red":
            print("You enter the room of fiery death, and surprisingly, are burned to death. Game Over")
        elif choice3 == "yellow":
            print("You find the treasure room and can finally pay off your mortgage! You Win!")
        elif choice3 == "blue":
            print("You have been eaten alive by the giant Weasel that resides in this room. Game Over")
        else:
            print("You obviously cannot follow instructions and sit by the doors until you starve to death. Game Over")
    else:
        print("You are too impatient and decide to swim across. On the way you are attacked by a giant trout and pulled under. Game Over")
else:
    print("The road ends abruptly in a cliff edge. Unfortunately in the dim light you do not see this and fall to your doom. Game Over")
    