print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

choice1 = input("You're at a crossroad, where do you want to go? Type 'Left' or 'Right'.").lower()

if choice1=="left":
    choice2 =input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()

    if choice2=="wait":
        choice3 = input("move forward, There are three doors infront of you Yellow, Blue, Red. Which one you want to select?").lower()
        if choice3 =="blue":
            print("Eaten by beasts.")
            print("Gameover")

        if choice3 == "red":
            print("burned by fire.")
            print("Gameover")

        if choice3 == "yellow":
            print("You win.")

        else:
            print("Game Over")
    else:
        print("You were attacked by trout. Game Over.")


else:
    print("Fall into a hole Game Over.")