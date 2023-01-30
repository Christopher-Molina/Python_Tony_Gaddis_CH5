# Starting Out With Python 5th Edition: Chapter 5 - Exercise 2
# Constants for state sales tax and county sales tax
STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025


# Main function
def main():
    # Input amount of purchase
    amount = ask_for_amount()

    # Calculate state tax, county tax, and total amount
    state_tax = compute_state_sales_tax(amount)
    county_tax = compute_county_sales_tax(amount)
    total_amount = compute_total_amount(amount, state_tax, county_tax)

    # Display state tax, county tax, and total amount
    print_details(state_tax, county_tax, total_amount)


def ask_for_amount():
    amount = float(input('Enter amount of purchase: '))
    return amount


# This function calculates the state sales tax
def compute_state_sales_tax(amount):
    return amount * STATE_SALES_TAX


# This function calculates the county sales tax
def compute_county_sales_tax(amount):
    return amount * COUNTY_SALES_TAX


# This function calculates the total amount
def compute_total_amount(amount, state_tax, county_tax):
    return amount + state_tax + county_tax


def print_details(state_tax, county_tax, total_amount):
    print(f'State sales tax is ${state_tax:,.2f}')
    print(f'County sales tax is ${county_tax:,.2f}')
    print(f'Total amount is ${total_amount:,.2f}')


# Call the main function
if __name__ == '__main__':
    main()
