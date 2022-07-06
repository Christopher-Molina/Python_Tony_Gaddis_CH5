# Starting Out With Python 5th Edition: Chapter 5 - Exercise 16
import random


# Main function
def main():
    # Calculate numbers that are even and odd
    even_count, odd_count = odd_even_counter()

    # Display even and odd counts
    display_count(even_count, odd_count)


# Function generates 100 random numbers
# counts which are even and odd, and returns the count.
def odd_even_counter():
    even_count = odd_count = 0
    print('Generating random numbers...')
    for number in range(100):
        number = random.randint(1, 101)
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


# Function displays the even and odd count
def display_count(even_count, odd_count):
    print('Odd: ' + str(even_count))
    print('Even: ' + str(odd_count))


# Call the main function
if __name__ == '__main__':
    main()
