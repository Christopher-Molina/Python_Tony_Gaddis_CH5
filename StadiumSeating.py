# Starting Out With Python 5th Edition: Chapter 5 - Exercise 7
import Formatter

CLASS_A = 20  # Class A seats cost $20
CLASS_B = 15  # Class B seats cost $15
CLASS_C = 10  # Class C seats cost $10


# Main function
def main():
    class_a_tickets = get_class_a_tickets()
    class_b_tickets = get_class_b_tickets()
    class_c_tickets = get_class_c_tickets()
    revenue = calculate_revenue(class_a_tickets, class_b_tickets, class_c_tickets)
    display(revenue, class_a_tickets, class_b_tickets, class_c_tickets)


# Function returns amount of class a tickets sold
def get_class_a_tickets():
    print('How many class A tickets were sold? ', end='')
    class_a_tickets = input_validation()
    return class_a_tickets


# Function returns amount of class b tickets sold
def get_class_b_tickets():
    print('How many class B tickets were sold? ', end='')
    class_b_tickets = input_validation()
    return class_b_tickets


# Function returns amount of class c tickets sold
def get_class_c_tickets():
    print('How many class C tickets were sold? ', end='')
    class_c_tickets = input_validation()
    return class_c_tickets


# Function calculates total revenue from sum of all tickets sold
def calculate_revenue(class_a, class_b, class_c):
    return (class_a * CLASS_A) + (class_b * CLASS_B) + (class_c * CLASS_C)


# Function validates user input to ensure value isn't negative
def input_validation():
    tickets = int(input())
    while tickets < 0:
        tickets = int(input('Tickets sold can\'t be negative, try again: '))
    return tickets


# Function displays revenue formatted as a dollar amount
def display(revenue, class_a, class_b, class_c):
    # Display price table
    print(f'\nClass A: {class_a} ticket\\s at ${CLASS_A}')
    print(f'Class B: {class_b} ticket\\s at ${CLASS_B}')
    print(f'Class C: {class_c} ticket\\s at ${CLASS_C}')
    print(f'\nThe total revenue of all tickets sold is {Formatter.dollar_format(revenue)}')


# Call the main function
if __name__ == '__main__':
    main()
