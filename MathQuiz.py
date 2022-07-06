# Starting Out With Python 5th Edition: Chapter 5 - Exercise 11
import random

# Generate  two random global numbers to be added
random_number1 = random.randint(1, 1000)
random_number2 = random.randint(1, 1000)


# Main function
def main():
    # Input sum of two random numbers
    user_answer = input_sum()

    # Validate the answer
    check_answer(user_answer)


# This function returns the sum inputted by the user
def input_sum():
    global random_number1
    global random_number2
    user_answer = int(input(f'What is {random_number1} + {random_number2}? '))
    return user_answer


# This function checks the answer inputted by the user
def check_answer(user_answer):
    global random_number1
    global random_number2

    # Validate the answer
    if user_answer == random_number1 + random_number2:
        print('Correct!')  # Output correct if user answer equals right sum
    else:
        print(f'Incorrect, correct answer is {random_number1 + random_number2:,.0f}')  # Else, output incorrect


# Call the main function
if __name__ == '__main__':
    main()
