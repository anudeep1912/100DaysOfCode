# TODO: Create a Blank Screen.
# TODO: Create Paddles
# TODO: Move Paddles with key strokes
# TODO: Score Keeping
# TODO: Ball Movement
# TODO: Ball interaction with Paddles
# TODO: Game Over Scenarios
# TODO: ball bounce on cross limits.

from turtle import Screen
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()

screen.tracer(0)
screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.title("PONG!")

paddle_l = Paddle((-430, 0))
paddle_r = Paddle((430, 0))
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(paddle_l.paddle_move_up, 'w')
screen.onkeypress(paddle_l.paddle_move_down, 's')
screen.onkeypress(paddle_r.paddle_move_up, 'Up')
screen.onkeypress(paddle_r.paddle_move_down, 'Down')

while scoreboard.is_game_on:

    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Collision with paddle.
    if ball.distance(paddle_l) < 50 and ball.xcor() < -410 or ball.distance(paddle_r) < 50 and ball.xcor() > 410:
        ball.bounce_x()
        if ball.speed != 0.01:
            ball.speed -= 0.01
        else:
            ball.speed -= 0.001

    # right paddle misses
    if ball.xcor() > 435:
        scoreboard.update_score_board_l()
        ball.reset_ball()

    # left paddle misses
    if ball.xcor() < -435:
        scoreboard.update_score_board_r()
        ball.reset_ball()

    scoreboard.is_game_over()

screen.exitonclick()
