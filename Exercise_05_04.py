# Starting Out With Python 5th Edition: Chapter 5 - Exercise 4
import Formatter


# Main function
def main():
    # Get monthly loan expense
    loan = get_loan_expense()

    # Get monthly insurance expense
    insurance = get_insurance_expense()

    # Get monthly gas expense
    gas = get_gas_expense()

    # Get monthly oil expense
    oil = get_oil_expense()

    # Get monthly tire expense
    tire = get_tire_expense()

    # Get maintenance expense
    maintenance = get_maintenance_expense()

    # Calculate total cost
    total_cost = calculate_total_cost(loan, insurance, gas, oil, tire, maintenance)

    # Calculate monthly cost of all expenses
    calculate_monthly_cost(total_cost)

    # Calculate yearly cost of all expenses
    calculate_yearly_cost(total_cost)


# This function returns the loan expense
def get_loan_expense():
    print('Enter monthly loan expense: ', end='')
    loan_expense = input_validation()
    return loan_expense


# This function returns the insurance expense
def get_insurance_expense():
    print('Enter monthly insurance expense: ', end='')
    insurance_expense = input_validation()
    return insurance_expense


# This function returns the gas expense
def get_gas_expense():
    print('Enter monthly gas expense: ', end='')
    gas_expense = input_validation()
    return gas_expense


# This function returns the oil expense
def get_oil_expense():
    print('Enter monthly oil expense: ', end='')
    oil_expense = input_validation()
    return oil_expense


# This function returns the tire expense
def get_tire_expense():
    print('Enter monthly tire expense: ', end='')
    tire_expense = input_validation()
    return tire_expense


# This function returns the maintenance expense
def get_maintenance_expense():
    print('Enter monthly maintenance expense: ', end='')
    maintenance_expense = input_validation()
    return maintenance_expense


# This functions calculates the total cost of all expenses
def calculate_total_cost(loan, insurance, gas, oil, tire, maintenance):
    return loan+insurance+gas+oil+tire+maintenance


# This function calculates the monthly cost of all expenses
def calculate_monthly_cost(total_cost):
    print(f'\nApproximate monthly cost: {Formatter.dollar_format(total_cost)}')


# This function calculates the yearly cost of all expenses
def calculate_yearly_cost(total_cost):
    print(f'Approximate yearly cost: {Formatter.dollar_format(total_cost * 12)}')


# Input validation function
def input_validation():
    expense = float(input())
    while not(expense > 0):
        print('Expense cannot be negative,try again.')
        expense = float(input())
    return expense


# Call the main function
if __name__ == '__main__':
    main()
