from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("white")
        self.segments.append(new_turtle)

    def extend(self):
        # cur_x = self.segments[len(self.segments) - 1].xcor() - 20
        # cur_y = self.segments[len(self.segments) - 1].ycor()
        # self.add_segments((cur_x, cur_y))
        self.add_segments(self.segments[-1].pos())

    def collision_with_segments(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

