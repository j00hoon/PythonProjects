from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.create_cars()

    def create_cars(self):
        self.add_cars()

    def add_cars(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(COLORS[randint(0, len(COLORS) - 1)])
        new_car.setpos(290, randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for i in range(0, len(self.cars) - 1):
            self.cars[i].setheading(LEFT)
            if -320 < self.cars[i].xcor():
                new_x = self.cars[i].xcor() - MOVE_INCREMENT
                self.cars[i].goto(new_x, self.cars[i].ycor())

    def distance_check(self, moving_turtle):
        for car in self.cars[1:]:
            if moving_turtle.distance(car) < 25:
                return True

    def increase_speed(self):
        MOVE_INCREMENT += 1

