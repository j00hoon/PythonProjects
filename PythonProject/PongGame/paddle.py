import turtle
from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setpos(360, 0)

    def up(self):
        # self.setheading(UP)
        cur_y = self.ycor() + 20
        self.goto(self.xcor(), cur_y)

    def down(self):
        # self.setheading(DOWN)
        cur_y = self.ycor() - 20
        self.goto(self.xcor(), cur_y)
