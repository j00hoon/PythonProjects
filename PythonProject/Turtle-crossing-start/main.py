import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

moving_turtle = Player()

screen.listen()
screen.onkey(moving_turtle.up, "Up")

levelBoard = Scoreboard()
speedLevel = 0.1

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(speedLevel)
    screen.update()
    cars.move_cars()

    cars.create_car()

    # Detect successful crossing
    if moving_turtle.success_to_finish_line():
        levelBoard.increase_scoreboard()

    # Detect collision with car
    if cars.collision_with_car_check(moving_turtle):
        game_is_on = False


levelBoard.game_over()
screen.exitonclick()
