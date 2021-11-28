from turtle import Turtle
import random
COLORS = ["red", "green", "blue", "yellow", "maroon", "indigo", "violet"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.obstacle_list = []
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(270)
        self.turtlesize(stretch_wid=2, stretch_len=1.5)
        self.generate_obstacles()
        self.change_in_x = 10

    def generate_obstacles(self):
        x_cor = random.randint(300, 1500)
        y_cor = random.randint(-150, 200)
        self.goto(x_cor, y_cor)

    def move_obstacle(self):
        self.setx(self.xcor()-self.change_in_x)

    def level_up(self):
        self.change_in_x += 10
