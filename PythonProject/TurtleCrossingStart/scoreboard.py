from turtle import Turtle

FONT = ("Courier", 18, "normal")
POSITION = (-280, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.setpos(POSITION)
        self.create_scoreboard()

    def create_scoreboard(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_scoreboard(self):
        self.clear()
        self.level += 1
        self.create_scoreboard()

    def game_over(self):
        self.clear()
        self.setpos(-10, 0)
        self.write("Game Over", align="center", font=FONT)