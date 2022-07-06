# Starting Out With Python 5th Edition: Chapter 5 - Exercise 8
import math
import Formatter

# Per 112 sq ft of wall space, 8 hours of labor and 1 gallon of paint are required
SQ_FEET = 112
EIGHT = 8  # 8 hours of labor per 112 sq ft
LABOR_PAY = 35  # $35 per hour
GALLON_OF_PAINT = 1  # 1 gallon of paint per 112 sq feet


# Main function
def main():
    # Input wall space
    wall_space = get_wall_space()

    # Input price of paint per gallon
    price_per_gallon = get_price_per_gallon()

    # Calculate ratio
    ratio = wall_space / SQ_FEET

    # Calculate total gallons of paint required
    paint = calculate_gallons_of_paint(ratio)

    # Calculate total hours of labor required
    labor = calculate_hours_of_labor(ratio)

    # Calculate total cost of paint
    paint_cost = calculate_paint_cost(paint, price_per_gallon)

    # Calculate total cost of labor
    labor_cost = calculate_labor_cost(labor)

    # Calculate total cost
    total_cost = calculate_total_cost(paint_cost, labor_cost)

    # Display details
    display(paint, labor, paint_cost, labor_cost, total_cost)


# Function returns wall space in square feet
def get_wall_space():
    print('Enter wall space in square feet: ', end='')
    wall_space = input_validation()
    return wall_space


# Function returns price per gallon of paint
def get_price_per_gallon():
    print('Enter the price per gallon paint: ', end='')
    price_per_gallon = input_validation()
    return price_per_gallon


# Function calculates total gallons of paint
def calculate_gallons_of_paint(ratio):
    return math.ceil(round(ratio, 2) * GALLON_OF_PAINT)


# Function calculates total hours of labor
def calculate_hours_of_labor(ratio):
    return round(ratio, 2) * EIGHT


# Function calculates cost of paint
def calculate_paint_cost(paint, price_per_gallon):
    return paint * price_per_gallon


# Function calculates cost of labor
def calculate_labor_cost(labor):
    return labor * LABOR_PAY


# Function calculates total cost of paint job
def calculate_total_cost(paint_cost, labor_cost):
    return paint_cost + labor_cost


# Function validates input from the user
def input_validation():
    wall_space = float(input())
    while not(wall_space > 0):
        wall_space = float(input('Wall space can\'t be negative, try again: '))
    return wall_space


# Function displays the final output formatted
def display(paint, labor, paint_cost, labor_cost, total_cost):
    print(f'\nGallons of paint required: {paint}')
    print(f'Hours of labor required: {Formatter.general_format(labor)}')
    print(f'\nPaint cost: {Formatter.dollar_format(paint_cost)}')
    print(f'Labor cost: {Formatter.dollar_format(labor_cost)}')
    print(f'Total cost of paint job: {Formatter.dollar_format(total_cost)}')


# Call the main function
if __name__ == '__main__':
    main()
