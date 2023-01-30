# Starting Out With Python 5th Edition: Chapter 5 - Exercise 20
import random
MAX = 100  # Max range


# Main function
def main():
    # Generate a random number
    print('Generating a random number...')
    number = random_number()

    # Prompt user for guess number
    print('Guess the random number: ', end='')
    guess = get_guess()

    # Evaluate guess
    evaluate_guess(number, guess)


# Function evaluates whether the user entered the right number
def evaluate_guess(number, guess):

    flag = True
    guess_count = 1  # Initially guess count is 1
    while flag:
        if number == guess:
            print('Congratulations! You guessed the number.')
            flag = False  # Set flag to false and exit while loop
        else:
            if guess > number:
                print('Too high, try again: ', end='')
                guess = get_guess()
                guess_count += 1  # Increment guess count per each guess
            else:
                print('Too low, try again: ', end='')
                guess = get_guess()
                guess_count += 1  # Increment guess count per each guess

    # Display results
    display_results(number, guess_count)


# Function returns a random number
def random_number():
    return random.randint(1, MAX+1)


# Function returns the guess number entered by the user
def get_guess():
    guess = (input())

    # Input validation
    flag = True
    while flag:
        if str(guess).isdigit():
            guess = int(guess)
            flag = False
        else:
            guess = int(input('Invalid input, enter a numerical value and try again: '))
    return guess


# Function displays the results
def display_results(number, guess_count):
    print('\nRandom Number: ' + str(number))
    print('Guess Count: ' + str(guess_count))


# Call the main function
if __name__ == '__main__':
    main()
