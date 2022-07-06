# Starting Out With Python 5th Edition: Chapter 5 - Exercise 10
import Formatter

FOOT_TO_INCHES = 12  # One foot equals 12 inches


# Main function
def main():
    # Input feet
    feet = get_feet()

    # Calculate feet to inches
    inches = feet_to_inches(feet)

    # Display output
    display(feet, inches)


# Function returns amount of feet entered by user
def get_feet():
    print('Enter amount of feet to convert to inches: ', end='')
    feet = input_validation()
    return feet


# Function converts feet to inches
def feet_to_inches(feet):
    return feet * FOOT_TO_INCHES


# Function displays output formatted
def display(feet, inches):
    print(f'{Formatter.general_format(feet)} feet = {Formatter.general_format(inches)} inches')


# Function validates input by the user
def input_validation():
    value = float(input())
    while not(value > 0):
        value = float(input('Value can\'t be negative, try again: '))
    return value


# Call the main function
if __name__ == '__main__':
    main()
