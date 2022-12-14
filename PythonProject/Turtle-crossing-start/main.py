import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_over import Gameover

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

loopCheck = 0
game_is_on = True
while game_is_on:
    time.sleep(speedLevel)
    screen.update()
    cars.move_cars()

    if loopCheck % 6 == 0:
        cars.create_cars()
    if not moving_turtle.check_location():
        levelBoard.update_level()
    if cars.distance_check(moving_turtle):
        game_is_on = False

    loopCheck += 1

game_over = Gameover()
screen.exitonclick()
