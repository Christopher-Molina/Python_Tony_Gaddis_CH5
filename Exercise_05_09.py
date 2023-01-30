# Starting Out With Python 5th Edition: Chapter 5 - Exercise 9
import Formatter

STATE_TAX = 0.05  # State sales tax is 5%
COUNTY_TAX = 0.025  # County tax is 2.5%


# Main function
def main():
    # Input total sales for the month
    monthly_sales = get_monthly_sales()

    # Calculate state sales tax
    sales_tax = get_sales_tax(monthly_sales)

    # Calculate county sales tax
    county_tax = get_county_tax(monthly_sales)

    # Calculate total tax
    total_tax = total_sales_tax(sales_tax, county_tax)

    # Display details
    display(sales_tax, county_tax, total_tax)


# This function returns the monthly sales
def get_monthly_sales():
    print('Enter the monthly sales: ', end='')
    monthly_sales = input_validation()
    return monthly_sales


# This function calculates the state sales tax
def get_sales_tax(monthly_sales):
    return monthly_sales * STATE_TAX


# This function calculates the county sales tax
def get_county_tax(monthly_sales):
    return monthly_sales * COUNTY_TAX


# This function calculates the total sales tax
def total_sales_tax(state_tax, county_tax):
    return state_tax + county_tax


# This function displays the final output formatted
def display(state_tax, county_tax, total_tax):
    print(f'\nCounty sales tax is {Formatter.dollar_format(county_tax)}')
    print(f'State sales tax is {Formatter.dollar_format(state_tax)}')
    print(f'Total sales tax is {Formatter.dollar_format(total_tax)}')


# This function validates user input
def input_validation():
    value = float(input())
    while value < 0:
        value = float(input('Value can\'t be negative, try again: '))
    return value


# Call the main function
if __name__ == '__main__':
    main()
