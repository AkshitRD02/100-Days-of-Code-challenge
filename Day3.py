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
choice1=input("There is a divergence with two paths. Type left or right:")
if choice1.lower()== "left":
    choice2=input("You arrive at a river.Type wait or swim:")
    if choice2.lower()== "wait":
        choice3=input("Three doors appear out of nowhere. Open which one? Type red, yellow or blue")
        if choice3.lower()== "yellow":
            print("The door opens.You got the treasure! You win!")
        elif choice3.lower()== "blue":
            print("The door opens.Ferocious beasts eat you! GAME OVER!")
        elif choice3.lower()== "red":
            print("The door opens.You get burnt by fire! GAME OVER!")
        else:
            print("Incorrect input. GAME OVER!")
    else:
        print("A huge fish monster eats you! GAME OVER!")
else:
    print("The earth beneath you collapses,killing you! GAME OVER!")
