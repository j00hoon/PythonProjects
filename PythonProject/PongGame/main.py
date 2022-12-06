import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

paddle_r = Paddle(380, 0)
paddle_l = Paddle(-380, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

direction = "r"
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move(direction)

    # Detect collision with top wall and bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect contact with paddle_r and paddle_l
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 370) or (ball.distance(paddle_l) < 50 and ball.xcor() < -370):
        ball.bounce_x()

    # Detect collision with side wall
    if ball.xcor() > 395:
        ball.detect_sidewall()
        direction = "l"
        scoreboard.score_update("l")
    if ball.xcor() < -395:
        ball.detect_sidewall()
        direction = "r"
        scoreboard.score_update("r")


screen.exitonclick()