"""Function Battleship."""
__author__ = "739664950"
import random


def input_guess(grid_size: int, placement: str) -> int:
    """This function deals in user row and column guess."""
    assert placement == "row" or placement == "column" 
    if (placement == "row"):
        guess_row: int = int(input("Guess a row: "))
        while guess_row > grid_size or guess_row == 0:
            guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return (guess_row) 
    elif (placement == "column"):
        guess_column: int = int(input("Guess a column: "))
        while guess_column > grid_size or guess_column == 0:
            guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return (guess_column)
    return 0


def print_grid(grid_size: int, row_guess: int, column_guess: int, valid: bool) -> None:
    """Prints out emoji grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result_box = ""
    counter_row: int = 1
    if (valid):
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX
    while counter_row <= grid_size:
        emojis = ""
        column_count = 1
        if (row_guess == counter_row):
            while (column_count <= grid_size):
                if (column_guess == column_count):
                    emojis += result_box
                else:
                    emojis += BLUE_BOX
                column_count += 1
        else:
            while (column_count <= grid_size):
                emojis += BLUE_BOX
                column_count += 1
        print(emojis)
        counter_row += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Determines if user guess is correct."""
    if (row_guess == secret_row) and (column_guess == secret_column):
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Determine if hit or miss."""
    turn: int = 1
    while turn <= 5:
        print(f"=== Turn {turn}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        isvalid = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, isvalid)
        if isvalid:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            return
        else:
            print("Miss!")
            turn += 1
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))