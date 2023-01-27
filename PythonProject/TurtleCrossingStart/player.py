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
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def success_to_finish_line(self):
        if self.ycor() < FINISH_LINE_Y:
            return False
        else:
            self.setpos(STARTING_POSITION)
            return True



