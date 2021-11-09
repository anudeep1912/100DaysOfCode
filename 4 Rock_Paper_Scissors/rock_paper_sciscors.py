#Write your code below this line 👇
import random
winning_scenarios = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
user_choice = input("What do you choose? Type Rock, Paper, Scissors: ")
print(user_choice.lower())
opp_choice = random.choice(['scissors', 'rock', 'paper'])
print(opp_choice)

if user_choice == opp_choice:
  print("It is a Draw! Try again")
elif (winning_scenarios[user_choice] == opp_choice):
  print(f"User Wins! {user_choice} beats {opp_choice}")
elif (winning_scenarios[opp_choice] == user_choice):
  print(f"User Loses! {opp_choice} beats {user_choice}")