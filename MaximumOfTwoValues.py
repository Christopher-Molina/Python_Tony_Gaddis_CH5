# Starting Out With Python 5th Edition: Chapter 5 - Exercise 12
# Main function
def main():
    # Input two integer values
    number1 = get_number()
    number2 = get_number()

    # Get max of two numbers
    max_number(number1, number2)


# Function returns a number
def get_number():
    number = int(input('Enter a number: '))
    return number


# Function calculates the greater number
def max_number(number1, number2):
    if number1 == number2:
        print('Numbers are equal.')
    else:
        print(str(max(number1, number2)) + ' is greater.')


# Call the main function
if __name__ == '__main__':
    main()
