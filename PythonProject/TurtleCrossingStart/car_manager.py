from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
LEFT = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.add_car()

    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setpos(300, random.randint(-250, 250))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def collision_with_car_check(self, moving_turtle):
        for car in self.cars:
            if moving_turtle.distance(car) < 25:
                return True

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

