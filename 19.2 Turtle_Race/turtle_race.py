from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets: ", prompt="Please choose a colour which will win the race: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_cor = -60
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_cor)
    y_cor += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} is the winner.]")
            else:
                print(f"You Lose! The {winning_turtle} is the winner.]")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
