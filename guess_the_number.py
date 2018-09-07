import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    firstNum = int(input("Enter the lowest number to guess from: "))
    secondNum = int(input("Enter the highest number to guess from: "))
    return firstNum, secondNum


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    # initializes the guess number counter
    number_of_guesses = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)
    # loop to run the program until user chooses to quit
    while 1:
        try:
            # Get user input
            guess = get_guess()
            # check guess
            result = check_guess(guess, secret)
            # increment guess
            number_of_guesses += 1
            # display result
            print(result)
            if result == correct:
                # display number of guesses
                print("It took you " + str(number_of_guesses) + " guesses")
                # if user wants to play again
                play_again_question = input("Would you like to play again? (Y/N)")
                if play_again_question == "N" or play_again_question == "n":
                    quit()
        except ValueError:
            print("Error. Please enter a number.")


if __name__ == '__main__':
    main()
