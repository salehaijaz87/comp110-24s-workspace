"""ex01_one_shot_battleship!"""

__author__ = "730664950"

grid_size: int = 4
secret_row: int  = 3
secret_column: int = 2
result_box = ""
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

guess_row: int = int(input("Guess a row: "))

while guess_row < 1 or guess_row > 4:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    
guess_column: int = int(input("Guess a column: "))

while guess_column < 1 or guess_column > 4:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))


counter_row: int = 1

if (guess_row == secret_row) and (guess_column == secret_column):
    result_box = RED_BOX
else:
    result_box = WHITE_BOX
    

while counter_row <= grid_size:
    emojis = ""
    column_count = 1
    if (guess_row == counter_row):
        while(column_count <= grid_size):
            if(guess_column == column_count):
                emojis += result_box
            else:
                emojis += BLUE_BOX
            column_count += 1
    else:
        while(column_count <= grid_size):
            emojis += BLUE_BOX
            column_count += 1
    print(emojis)
    counter_row += 1

if (guess_row == secret_row) and (guess_column == secret_column):
    print("Hit!")
elif (guess_row == secret_row) and (guess_column != secret_column):
    print ("Close! correct row, wrong column")
elif (guess_row!= secret_row) and (guess_column == secret_column):
    print ("Close! correct column, wrong row")
else:
    print("Miss!")