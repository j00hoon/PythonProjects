import turtle
from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setpos(x, y)

    def up(self):
        # self.setheading(UP)
        if self.ycor() < 260:
            cur_y = self.ycor() + 20
            self.goto(self.xcor(), cur_y)

    def down(self):
        # self.setheading(DOWN)
        if self.ycor() > -260:
            cur_y = self.ycor() - 20
            self.goto(self.xcor(), cur_y)
