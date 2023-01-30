# Starting Out With Python 5th Edition: Chapter 5 - Exercise 3
import Formatter

# Minimum amount of insurance is 80% of replacement cost
MIN_PERCENT = 0.80


# Main function
def main():
    replacement_cost = prompt_input()
    minimum_insurance = calculate_minimum_insurance(replacement_cost)
    display(replacement_cost, minimum_insurance)


# This function returns the replacement cost of a structure
def prompt_input():
    replacement_cost = float(input('Enter the replacement cost of a building: '))
    while replacement_cost < 0:
        print('Replacement cost cannot be negative, try again.')
        replacement_cost = float(input('Enter the replacement cost of a building: '))
    return replacement_cost


# This function calculates the minimum insurance cost at 80%
def calculate_minimum_insurance(replacement_cost):
    return replacement_cost * MIN_PERCENT


# This function displays the replacement cost and minimum insurance
def display(replacement_cost, minimum_insurance):
    print('\nReplacement cost:', Formatter.dollar_format(replacement_cost))
    print('Minimum insurance:', Formatter.dollar_format(minimum_insurance))


# Call the main function
if __name__ == '__main__':
    main()
