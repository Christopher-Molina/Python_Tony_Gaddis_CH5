# Starting Out With Python 5th Edition: Chapter 5 - Exercise 19
import Formatter


# Main function
def main():
    # Input present value
    print('Enter the present value: ', end='')
    present_value = get_value()

    # Input the monthly interest
    print('Enter the monthly interest: ', end='')
    interest = get_value() / 100

    # Input the number of months
    print('Enter the number of months: ', end='')
    months = get_value()

    # Calculate future value
    future_value = calculate_future_value(present_value, interest, months)

    # Display future value
    display_future_value(future_value)


# Function returns user input
def get_value():
    value = input_validation()
    return value


# Function calculates future value
def calculate_future_value(p, i, t):
    return p * (1 + i)**t


# Function displays future value formatted
def display_future_value(fv):
    print(f'\nFV = {Formatter.dollar_format(fv)}')


# Function validates user input
def input_validation():
    value = float(input())
    while value < 0:
        value = float(input('Value cannot be negative, try again: '))
    return value


# Call the main function
if __name__ == '__main__':
    main()
