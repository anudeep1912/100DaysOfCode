from art import logo
import random


def generate_random_number():
    random_number = random.randint(1, 100)
    return random_number


def easy_or_hard(choice):
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    random_number = generate_random_number()
    print("I am thinking of a number between 1 to 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = easy_or_hard(difficulty)
    print(f"You have {lives} attempts to guess the number")
    while lives != 0:
        try:
            user_choice = int(input("Make a Guess: "))
        except ValueError:
            print("Please choose a proper number between 1 to 100")
            continue
        lives -= 1
        if user_choice > random_number:
            print(f"Too High!\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
        elif user_choice < random_number:
            print(f"Too Low!\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
        else:
            print(f"You win! The number is {random_number}")
            break


play_again = True
while play_again:
    game()
    rerun = input("Do you wanna play again (y or n): ")
    if rerun == 'n':
        play_again = False


