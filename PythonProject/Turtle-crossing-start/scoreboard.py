from turtle import Turtle

FONT = ("Courier", 18, "normal")
POSITION = (-280, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.level_board = f"Level : {self.level}"
        self.create_level()

    def create_level(self):
        self.setpos(POSITION)
        self.write(self.level_board, align="left", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.level_board = f"Level : {self.level}"
        self.create_level()

