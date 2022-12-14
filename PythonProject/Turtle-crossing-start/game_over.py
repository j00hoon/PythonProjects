from turtle import Turtle

FONT = ("Courier", 18, "normal")
POSITION = (-10, 0)


class Gameover(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_over()

    def game_over(self):
        self.setpos(POSITION)
        self.write("GAME OVER", align="center", font=FONT)