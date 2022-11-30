from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.create_score(self.l_score, -100, 200)
        self.create_score(self.r_score, 100, 200)

    def create_score(self, score, x, y):
        self.goto(x, y)
        self.write(score, align="center", font=("Courier", 50, "normal"))

    # def create_r_score(self):
    #     self.goto(100, 200)
    #     self.write(self, align="center", font=("Courier", 50, "normal"))

    def score_update(self, direction):
        self.clear()
        if direction == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.create_score(self.l_score, -100, 200)
        self.create_score(self.r_score, 100, 200)




