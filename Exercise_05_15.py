# Starting Out With Python 5th Edition: Chapter 5 - Exercise 15
SCORES = 5  # Amount of test scores


# Main function
def main():
    # Input five test scores
    print('Enter test score 1: ', end='')
    test_score_1 = get_test_score()
    print('Enter test score 2: ', end='')
    test_score_2 = get_test_score()
    print('Enter test score 3: ', end='')
    test_score_3 = get_test_score()
    print('Enter test score 4: ', end='')
    test_score_4 = get_test_score()
    print('Enter test score 5: ', end='')
    test_score_5 = get_test_score()

    # Calculate the average of all test scores
    average = calc_average(test_score_1, test_score_2, test_score_3, test_score_4, test_score_5)

    # Display results
    display_results(average, test_score_1, test_score_2, test_score_3, test_score_4, test_score_5)


# Function displays the average and all test score letter grades
def display_results(average, test_score_1, test_score_2, test_score_3, test_score_4, test_score_5):

    # Calculate grade for each test score and display
    i = 0
    print()
    for score in [test_score_1, test_score_2, test_score_3, test_score_4, test_score_5]:
        print(f'Test score {i+1}: {determine_grade(score)}')
        i += 1

    # Display the average
    print(f'\nAverage score: {average:.2f}')


# Function returns a test score
def get_test_score():
    test_score = input_validation()
    return test_score


# Function validates the input
def input_validation():
    test_score = float(input())
    while test_score < 0 or test_score > 100:
        test_score = float(input('Test score can\'t be negative or greater than 100, try again: '))
    return test_score


# Function returns the average of all test scores
def calc_average(test_score_1, test_score_2, test_score_3, test_score_4, test_score_5):
    total = 0
    for score in [test_score_1, test_score_2, test_score_3, test_score_4, test_score_5]:
        total += score
    return total / SCORES


# Function determines letter grade of each test score
def determine_grade(test_score):
    if (test_score >= 90) and (test_score <= 100):
        return 'A'
    elif (test_score >= 80) and (test_score < 90):
        return 'B'
    elif (test_score >= 70) and (test_score < 80):
        return 'C'
    elif (test_score >= 60) and (test_score < 70):
        return 'D'
    else:
        return 'F'


# Call the main function
if __name__ == '__main__':
    main()
