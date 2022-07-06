# Starting Out With Python 5th Edition: Chapter 5 - Exercise 6
import Formatter


# Main function
def main():
    # Input grams from fat
    fat_grams = get_grams_from_fat()

    # Input grams from carbohydrates
    carb_grams = get_grams_from_carbs()

    # Calculate calories from fat
    calories_from_fat = calculate_calories_from_fat(fat_grams)

    # Calculate calories from carbs
    calories_from_carbs = calculate_calories_from_carbs(carb_grams)

    # Display details
    display(calories_from_fat, calories_from_carbs)


# This function gets the input for fat grams from the user
def get_grams_from_fat():
    print('Enter grams from fat: ', end='')
    fat_grams = input_validation()  # Validate the input
    return fat_grams


# This function gets the input for carb grams from the user
def get_grams_from_carbs():
    print('Enter grams from carbs: ', end='')
    carb_grams = input_validation()
    return carb_grams


# This function validates the value entered for proper input
def input_validation():
    grams = float(input())
    while grams < 0:
        print('Grams cannot be negative, try again.')
        grams = float(input('Enter a positive gram amount: '))
    return grams


# This function calculates calories from fat
def calculate_calories_from_fat(fat_grams):
    return fat_grams * 9


# This function calculates calories from carbs
def calculate_calories_from_carbs(carb_grams):
    return carb_grams * 4


# This function displays the final output formatted
def display(calories_from_fat, calories_from_carbs):
    print('Calories from fat:', Formatter.general_format(calories_from_fat))
    print(f'Calories from carbs:', Formatter.general_format(calories_from_carbs))


# Call the main function
if __name__ == '__main__':
    main()
