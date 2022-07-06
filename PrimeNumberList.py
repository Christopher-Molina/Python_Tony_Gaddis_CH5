# Starting Out With Python 5th Edition: Chapter 5 - Exercise 18
MAX = 98


# Main function
def main():
    prime_number_list()  # Call the prime number list function


# Function prints all prime numbers up to 100
def prime_number_list():
    for number in range(2, MAX):
        if is_prime(number):
            print(str(number) + ' ', end='')


# Function determines if number is prime or not
def is_prime(number):
    for i in range(2, number):  # Exclude 1 since number / 1 is always number itself
        if number % i == 0:
            return False
    else:
        return True


# Call the main function
if __name__ == '__main__':
    main()
