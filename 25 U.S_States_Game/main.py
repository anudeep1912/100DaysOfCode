from turtle import Turtle, Screen
import pandas
from score_board import ScoreBoard

screen = Screen()

screen.bgpic("blank_states_img.gif")
screen.title("U.S States Quiz")


states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []
scoreboard = ScoreBoard()
tim = Turtle()
tim.penup()
tim.hideturtle()

while scoreboard.score < 50:
    print(guessed_states)
    user_guess = screen.textinput("Enter a state name: ", " ")
    if user_guess.lower() == "exit":
        missed_states = []
        for state in states_list:
            if state.lower() not in guessed_states:
                missed_states.append(state)
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("Missed_states.csv")
        break
    for state in states_list:
        if user_guess.lower() == state.lower() and user_guess.lower() not in guessed_states:
            guessed_states.append(state.lower())
            scoreboard.update_score()
            coordinates= states_data[states_data.state == state]
            x_cor, y_cor = int(coordinates["x"]), int(coordinates["y"])
            tim.goto(x_cor, y_cor)
            tim.write(state)

    if scoreboard.score == 50:
        scoreboard.reset()


screen.exitonclick()