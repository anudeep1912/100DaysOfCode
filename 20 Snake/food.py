from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_cor = random.randrange(-280, 280, 20)
        y_cor = random.randrange(-280, 280, 20)
        self.goto(x_cor, y_cor)