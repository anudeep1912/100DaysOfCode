from turtle import Turtle
import time
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.total_states = 50
        self.initialize_scores()

    def initialize_scores(self):
        self.goto(150, 245)
        self.write(f"Score: {self.score}/{self.total_states}", align='center', font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.initialize_scores()

    def reset(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write(f"Game Over\n"
                   f"You've Won!\n"
                   f"You Guessed all the states correctly.", align="center", font=FONT)