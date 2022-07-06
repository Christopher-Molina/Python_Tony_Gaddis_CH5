# Starting Out With Python 5th Edition: Chapter 5 - Exercise 13
# Constant for G = 9.8
G = 9.8


# Main function
def main():
    # Call the function to display distance fallen in meters
    display_distance()


# Function displays distance in meters
def display_distance():
    # Display header
    print('Seconds\tMeters')
    for i in range(10):
        # Display numbers evenly in a column
        if i + 1 == 10:
            print(f'{i+1}{falling_distance(i+1):>12.2f}')
        else:
            print(f'{i+1}{falling_distance(i+1):>13.2f}')


# Function returns distance in meters
# that object has fallen during time interval in seconds
def falling_distance(t):
    return (1/2)*G*(t**2)


# Call the main function
if __name__ == '__main__':
    main()
