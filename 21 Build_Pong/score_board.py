from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
SCORE_POSITIONS = [(-75, 225), (50, 225)]


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.is_game_on = True
        self.color('white')
        self.penup()
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.initialize_scores()

    def initialize_scores(self):
        self.clear()
        self.goto(-75, 225)
        self.write(f"{self.score_l}",align='center', font=FONT)
        self.goto(+75, 225)
        self.write(f"{self.score_r}", align='center', font=FONT)

    def update_score_board_l(self):
        self.score_l += 1
        self.initialize_scores()

    def update_score_board_r(self):
        self.score_r += 1
        self.initialize_scores()

    def is_game_over(self):
        if self.score_r >= 10 or self.score_l >= 10:
            self.is_game_on = False
            self.goto(0, 0)
            self.write("GAME OVER!", align='center', font=('Ariel', 50, 'normal'))