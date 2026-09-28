# Create a random number guessing game

import random

num = random.randint(1,10)

tries = 0

while True:
    guess = int(input("Please guess your number: "))

    if num == guess:
        tries += 1
        print(f"you are right, you guessed the number in {tries} tries")
        break

    elif num < guess:
        tries += 1
        print("Go a little lower")

    elif num > guess:
        tries += 1
        print("Go a little heigher")
        
    else:
        tries += 1
        print("You are wrong")