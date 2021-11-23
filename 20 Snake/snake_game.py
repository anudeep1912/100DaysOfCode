from turtle import Turtle, Screen
import time
import random
import math


class SnakeGame:
    def __init__(self):
        self.segment_list = []
        self.screen = Screen()
        self.score = 0

    def initialize_screen(self):
        self.screen.bgcolor('black')
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.delay(0)
        self.screen.title("Snake Game!")

    def initialize_snake(self):
        pos = [-20, 0, 20]
        for i in range(3):
            block = Turtle(shape='square')
            block.penup()
            block.color('white')
            block.goto(pos[i], 0)
            self.segment_list.append(block)

    def move_up(self):
        self.segment_list[0].setheading(90)

    def move_down(self):
        self. segment_list[0].setheading(270)

    def move_left(self):
        self.segment_list[0].setheading(180)

    def move_right(self):
        self.segment_list[0].setheading(0)

    def move_snake(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_up, 'w')
        self.screen.onkeypress(self.move_left, 'a')
        self.screen.onkeypress(self.move_down, 's')
        self.screen.onkeypress(self.move_right, 'd')

    def generate_food(self):
        food = Turtle(shape='circle')
        food.turtlesize(0.5)
        food.penup()
        food.color('blue')
        food_x = random.randrange(-280, 280, 20)
        food_y = random.randrange(-280, 280, 20)
        food.goto(food_x, food_y)
        return food

    def is_capture_food(self, food):
        (food_x, food_y) = food.pos()
        (curr_x, curr_y) = self.segment_list[0].pos()
        if round(curr_x) == food_x and round(curr_y) == food_y:
            self.segment_list.append(food)
            food.shape('square')
            food.color('white')
            food.turtlesize(1)
            return True
        return False

    def is_game_over(self):
        curr_pos = self.segment_list[0].pos()
        flag = False
        if -290 < curr_pos[0] < 290 and -290 < curr_pos[1] < 290:
            for segment in self.segment_list[1:]:
                if int(self.segment_list[0].distance(segment)) < 10:
                    flag = True
            print(flag)
        else:
            return True

    def play_game(self):
        game_on = True
        food_obj = self.generate_food()
        while game_on:
            self.screen.update()
            time.sleep(0.1)
            for seg_num in range(len(self.segment_list) - 1, 0, -1):
                x_cor = self.segment_list[seg_num - 1].xcor()
                y_cor = self.segment_list[seg_num - 1].ycor()
                self.segment_list[seg_num].goto(x_cor, y_cor)
            self.move_snake()
            self.segment_list[0].forward(20)
            if self.is_capture_food(food_obj):
                food_obj = self.generate_food()
                self.score += 1
            if self.is_game_over():
                break
        self.screen.exitonclick()


snake_game = SnakeGame()
snake_game.initialize_screen()
snake_game.initialize_snake()
snake_game.play_game()