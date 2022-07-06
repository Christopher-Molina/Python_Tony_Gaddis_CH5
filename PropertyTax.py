# Starting Out With Python 5th Edition: Chapter 5 - Exercise 5
import Formatter

PERCENTAGE = 0.60  # 60% of property's actual value
PROPERTY_TAX = 0.72  # 72 cents for each $100


# Main function
def main():
    # Input actual value of a piece of property
    actual_value = get_actual_value()

    # Calculate assessment value
    assessment_value = calculate_assessment_value(actual_value)

    # Calculate property tax
    property_tax = calculate_property_tax(assessment_value)

    # Display details
    display(actual_value, assessment_value, property_tax)


# Function gets actual value from the user
def get_actual_value():
    print('Enter actual value of a piece of property: ', end='')
    actual_value = input_validation()  # Validate input
    return actual_value


# Function validates value entered for proper input
def input_validation():
    actual_value = float(input())
    while actual_value < 0:
        print('Value cannot be negative, try again.')
        actual_value = float(input('Enter actual value of a piece of property: '))
    return actual_value


# Function calculates assessment value as 60% of actual value
def calculate_assessment_value(actual_value):
    return actual_value * PERCENTAGE


# Function calculates property tax as .72 cents per $100 of assessment value
def calculate_property_tax(assessment_value):
    return PROPERTY_TAX * assessment_value / 100


# Function displays final output formatted
def display(actual_value, assessment_value, property_tax):
    # Display header
    print('\nAssessment value: 60% of property\'s actual value.')
    print('Property tax: .72¢ per each $100 of assessment value.\n')
    print('Actual value:', Formatter.dollar_format(actual_value))
    print('Assessment value:', Formatter.dollar_format(assessment_value))
    print('Property tax:', Formatter.dollar_format(property_tax))


# Call the main function
if __name__ == '__main__':
    main()
