from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from divider import Divider
import time

BALL_SPEED = 0.05

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong-game")
screen.tracer(0)
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
l_scoreboard = ScoreBoard((-70, 190))
r_scoreboard = ScoreBoard((70, 190))
divider = Divider()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(BALL_SPEED)
    ball.move_ball()
    if not 289 > ball.ycor() > -289:
        ball.setheading(360 - ball.heading())
        ball.move_ball()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 326.40 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -326.40:
        if ball.distance(right_paddle) < 50 and ball.xcor() > 326.40:
            r_scoreboard.increase_score()
        elif ball.distance(left_paddle) < 50 and ball.xcor() < -326.40:
            l_scoreboard.increase_score()
        ball.right(180)
        ball.setheading(360 - ball.heading())
        ball.move_ball()
        BALL_SPEED *= 0.9

    if ball.xcor() < -390 or ball.xcor() > 390:
        if ball.xcor() < -390:
            r_scoreboard.increase_score()
        elif ball.xcor() > 390:
            l_scoreboard.increase_score()
        ball.goto(0, 0)
        ball.right(180)
        BALL_SPEED = 0.05

screen.exitonclick()
