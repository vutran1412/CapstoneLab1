# Number Guessing game
# Author: Vu Tran

# import random
import random

# function to guess random number
def guess_number():
    # generates a random number between 0 and 10 inclusive
    random_number = random.randint(0, 11)
    return random_number

# Loop to keep the game going as long as player wants to play
while True:
    # Prompts user input
    user_guess = int(input("Guess a number between 0 and 11\n"))
    # Calls the function
    random_number = guess_number()
    # If and elif statements to check to see if user guessed correctly
    if user_guess > random_number:
        print("Too high, the number is {}".format(random_number))
    elif user_guess < random_number:
        print("Too low, the number is {}".format(random_number))
    elif user_guess == random_number:
        print("correct!")
    # Gives user option to break out of the loop
    try_again = input("Do you wanna play again ?\n")
    if try_again != "yes" or try_again != "yes":
        break
