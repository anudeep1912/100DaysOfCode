import random
from game_data import data
import replit
from art import logo,vs


def choose_account():
    user = random.choice(data)
    return user


def clear():
    print("\n"*100)


user_a = choose_account()
user_b = choose_account()
score = 0
game_over = True
while game_over:
    if user_b == user_a:
        user_b = choose_account()
        continue
    print(logo)
    print(f"Compare A. {user_a['name']}, a {user_a['description']}, from {user_a['country']}.")
    print(vs)
    print(f"Compare B. {user_b['name']}, a {user_b['description']}, from {user_b['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a' and user_a['follower_count'] > user_b['follower_count']:
        user_b = choose_account()
        score += 1
        print(f"You're right! Current score: {score}.")
    elif user_choice == 'b' and user_b['follower_count'] > user_a['follower_count']:
        user_a = user_b
        user_b = choose_account()
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"A has {user_a['follower_count']}M followers and B has {user_b['follower_count']}M followers.")
        game_over = False