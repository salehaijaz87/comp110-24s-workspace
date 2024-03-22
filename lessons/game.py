"""Number Guessing Game"""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while not correct: # correct == False
    guess: int = int(input("Guess a number:"))
    if guess == SECRET:
            print(f"Correct! {guess} is the number")
            #something to help exit
            correct = True
    else: 
         if guess < 1:
                print("Guess too low! ")
         if guess > 10:
                print("Guess too high ")
                print("Guess again!")