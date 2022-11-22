import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

paddle_r = Paddle()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()