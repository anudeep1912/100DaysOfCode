from turtle import Turtle
Y_RANGE = 300
X_POSITION = 400


class Paddle(Turtle,):
    def __init__(self, position):
        super().__init__()
        self.paddle_position = position
        self.color('white')
        self.shape('square')
        self.setheading(90)
        self.penup()
        self.turtlesize(stretch_len=3, stretch_wid=0.5)
        self.goto(self.paddle_position)

    def paddle_move_up(self):
        if self.ycor() < 270:
            self.setheading(90)
            self.forward(30)

    def paddle_move_down(self):
        if self.ycor() > -270:
            self.setheading(270)
            self.forward(30)


