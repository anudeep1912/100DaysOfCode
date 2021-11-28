from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
SCORE_POSITIONS = [(-75, 225), (50, 225)]


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.level = 0
        self.hideturtle()
        self.initialize_scores()

    def initialize_scores(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"{self.level}", align='center', font=FONT)

    def update_score_board(self):
        self.level += 1
        self.initialize_scores()

    def is_game_over(self):
        if self.level < 10:
            self.goto(0, 0)
            self.write(f"GAME OVER! Your Current Score is {self.level}", align='center', font=('Ariel', 50, 'normal'))
        else:
            self.write("GAME OVER!", align='center', font=('Ariel', 50, 'normal'))