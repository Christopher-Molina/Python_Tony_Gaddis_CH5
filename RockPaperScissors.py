# Starting Out With Python 5th Edition: Chapter 5 - Exercise 21
import random


# Main function
def main():
    # Display header
    name = display_header()

    # Input user choice
    choice = get_choice()

    # Evaluate results
    evaluate_results(choice, name)


# Function displays the header
def display_header():
    print('*********************************')
    print('*   ROCK ** PAPER ** SCISSORS   *')
    print('*********************************\n')
    print('Welcome to the Rock-Paper-Scissors game!')
    name = input('Please, give me your name: ')
    return name


# Function returns choice entered by the user
def get_choice():
    print('\n*** Please, choose an option: ***')
    print('1. Rock\n2. Paper\n3. Scissors\n4. Quit')
    print('\nYour choice: ', end='')
    choice = input_validation()
    return choice


# Function validates the input by the user
def input_validation():
    value = input()
    while value not in ['1', '2', '3', '4']:
        value = input('Error, enter [1] for rock, [2] for paper, [3] for scissors, or [4] to quit: ')
    return int(value)


# Function evaluates the winner
def evaluate_results(choice, name):
    machine_wins = player_wins = draws = 0
    while choice != 4:
        machine = random.randint(1, 4)
        if machine == choice:
            print('\n******************\nDraw!\n******************')
            choice = get_choice()
            draws += 1
        elif choice == 1 and machine == 2:
            print('\n******************\nYou chose: Rock\nMachine chose: Paper')
            print(f'YOU LOSE\n******************')
            choice = get_choice()
            machine_wins += 1
        elif choice == 1 and machine == 3:
            print('\n******************\nYou chose: Rock\nMachine chose: Scissors')
            print(f'YOU WIN, {name}!\n******************')
            choice = get_choice()
            player_wins += 1
        elif choice == 2 and machine == 1:
            print('\n******************\nYou chose: Paper\nMachine chose: Rock')
            print(f'YOU WIN, {name}!\n******************')
            choice = get_choice()
            player_wins += 1
        elif choice == 2 and machine == 3:
            print('\n******************\nYou chose: Paper\nMachine chose: Scissors')
            print(f'YOU LOSE\n******************')
            choice = get_choice()
            machine_wins += 1
        elif choice == 3 and machine == 1:
            print('\n******************\nYou chose: Scissors\nMachine chose: Rock')
            print(f'YOU LOSE\n******************')
            choice = get_choice()
            machine_wins += 1
        elif choice == 3 and machine == 2:
            print('\n******************\nYou chose: Scissors\nMachine chose: Paper')
            print(f'YOU WIN, {name}!\n******************')
            choice = get_choice()
            player_wins += 1
    display_score(machine_wins, player_wins, draws)


# Function displays the final score
def display_score(machine_wins, player_wins, draws):
    print('\n******** FINAL SCORE ********')
    print(f'Your score: {player_wins}')
    print(f'Machine score: {machine_wins}')
    print(f'Draws: {draws}')


# Call the main function
if __name__ == '__main__':
    main()
