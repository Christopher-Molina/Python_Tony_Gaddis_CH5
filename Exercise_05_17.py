# Starting Out With Python 5th Edition: Chapter 5 - Exercise 17
# Main function
def main():
    # Input a number
    number = int(input('Enter a number: '))

    # Determine if the number is prime
    if is_prime(number):
        print('Prime.')
    else:
        print('Not prime.')


# Function determines if number is prime or not prime and returns true or false
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


# Call the main function
if __name__ == '__main__':
    main()
