from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.shape('turtle')
        self.color("green")
        self.setheading(90)
        self.penup()
        self.player_reset()

    def move(self):
        self.forward(20)

    def player_reset(self):
        self.goto(0, -250)