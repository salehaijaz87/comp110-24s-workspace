"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730664950"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
ship_box: str = ""

user_input: int = int(input("Pick a secret boat location between 1 and 4: "))

if user_input < 1:
    print(f"Error! {str(user_input)} too low!") 
    exit()
if user_input > 4:
    print(f"Error! {str(user_input)} too high!")
    exit()

user_guess: int = int(input("Guess a number between 1 and 4:"))

if user_guess < 1:
    print(f"Error! {str(user_guess)} too low!")
    exit()
if user_guess > 4:
    print(f"Error! {str(user_guess)} too high!")
    exit()

if user_input == user_guess:
    if user_guess == 1:
        ship_box = ship_box + RED_BOX
    else: ship_box = ship_box + BLUE_BOX
    if user_guess == 2:
        ship_box = ship_box + RED_BOX
    else: ship_box = ship_box + BLUE_BOX
    if user_guess == 3:
        ship_box = ship_box + RED_BOX
    else: ship_box = ship_box + BLUE_BOX
    if user_guess == 4:
        ship_box = ship_box + RED_BOX
    else: ship_box = ship_box + BLUE_BOX
    print(ship_box)
    print("Correct! You hit the ship.")

else: 
    if user_input != user_guess:
        if user_guess == 1:
            ship_box = ship_box + WHITE_BOX
        else: ship_box = ship_box + BLUE_BOX
        if user_guess == 2:
            ship_box = ship_box + WHITE_BOX
        else: ship_box = ship_box + BLUE_BOX
        if user_guess == 3:
            ship_box = ship_box + WHITE_BOX
        else: ship_box = ship_box + BLUE_BOX
        if user_guess == 4:
            ship_box = ship_box + WHITE_BOX
        else: ship_box = ship_box + BLUE_BOX
        print(ship_box)
        print("Incorrect! You missed the ship.")
