from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = 0.1    # decreasing makes the ball faster
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.turtlesize(0.5)
        self.dy = 10
        self.dx = 10

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_ball(self):
        self.bounce_x()
        self.goto(0, 0)
        self.speed = 0.1








