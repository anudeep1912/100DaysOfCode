from turtle import Screen
from turtle_player import Player
from cars import Car
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.move, "Up")
object_list = []

for i in range(25):
    new_object = Car()
    object_list.append(new_object)

game_on = True
car_speed = 0.1
level = 1
while game_on:
    time.sleep(car_speed)

    for car in object_list:
        car.move_obstacle()

        # Car collision with turtle
        if player.distance(car) < 20:
            game_on = False

        # Car Reaches Finish line
        if player.ycor() > 280:
            player.player_reset()
            car.level_up()
    print(game_on)
    screen.update()






















screen.exitonclick()