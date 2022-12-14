from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setpos(STARTING_POSITION)
        self.left(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def check_location(self):
        if self.ycor() < 290:
            return True
        else:
            self.setpos(STARTING_POSITION)
            return False



