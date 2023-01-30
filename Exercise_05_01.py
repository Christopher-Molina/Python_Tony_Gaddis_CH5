# Starting Out With Python 5th Edition: Chapter 5 - Exercise 1
import Formatter


# Main function
def main():
    # Input distance in kilometers
    kilometers = get_kilometers()

    # Calculate kilometers to miles
    km_to_miles = distance_to_miles(kilometers)

    # Display details
    display(kilometers, km_to_miles)


# Function gets kilometers from user
def get_kilometers():
    kilometers = float(input('Enter distance in kilometers: '))
    while kilometers < 0:
        print('Value cannot be negative, try again.')
        kilometers = float(input('Enter distance in kilometers: '))
    return kilometers


# This function converts a distance in kilometers to miles
def distance_to_miles(kilometers):
    return kilometers * 0.6214


# Function displays the final output formatted
def display(kilometers, km_to_miles):
    print(f'{Formatter.general_format(kilometers)} km is {Formatter.general_format(km_to_miles)} miles.')


# Call the main function
if __name__ == '__main__':
    main()
