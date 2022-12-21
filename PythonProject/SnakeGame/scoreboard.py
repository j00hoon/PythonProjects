from turtle import Turtle
from tkinter import messagebox

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    score = -1
    highest_score = 0

    def __init__(self):
        super().__init__()
        with open("highest_score.txt") as file:
            content = file.read()
            if content == "":
                self.highest_score = 0
            else:
                self.highest_score = int(content)
        self.hideturtle()
        self.goto(-25, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}  Highest Score : {self.highest_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        # messagebox.showinfo("Reset game", "Try again!!!")
        options = messagebox.askyesno("Retry or game over", "Retry?", icon="warning")
        if options:
            if self.score >= self.highest_score:
                self.highest_score = self.score
            self.score = -1
            self.update_scoreboard()
            return True
        else:
            return False

    def game_over(self):
        messagebox.showinfo("Game over", "You are dead!!!")
        self.goto(-25, 30)
        self.write("Game over", False, align=ALIGNMENT, font=FONT)
        if self.score >= self.highest_score:
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.score))


