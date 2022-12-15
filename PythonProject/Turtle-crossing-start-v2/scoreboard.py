from turtle import Turtle

FONT = ("Courier", 18, "normal")
POSITION = (-280, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setpos(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_scoreboard(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.setpos(-10, 0)
        self.write("Game over", align="center", font=FONT)
