from turtle import Turtle
from tkinter import messagebox

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    score = -1

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-25, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        messagebox.showinfo("Game over", "You are dead!!!")
        self.goto(-25, 30)
        self.write("Game over", False, align=ALIGNMENT, font=FONT)


