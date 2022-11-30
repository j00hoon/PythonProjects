from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 5
        self.y_move = 5

    def create_ball(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)

    def move(self, direction):
        print(f"direction : {direction}")
        if direction == "r":
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
        else:
            new_x = self.xcor() - self.x_move
            new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def remove_ball(self):
        self.clear()

    def detect_sidewall(self):
        self.remove_ball()
        self.create_ball()



    # def up_bounce(self, screen):
    #     new_x = self.xcor()
    #     while new_x <= 390:
    #         new_x = self.xcor() + 5
    #         new_y = self.ycor() - 5
    #         screen.update()
    #         time.sleep(0.005)
    #         self.goto(new_x, new_y)
    #         if new_x > 390:
    #             return False
    #     return True
    #
    # def bottom_bounce(self, screen):
    #     new_y = self.ycor()
    #     while new_y >= -290:
    #         new_x = self.xcor() - 5
    #         new_y = self.ycor() + 5
    #         screen.update()
    #         time.sleep(0.005)
    #         self.goto(new_x, new_y)
    #         if new_y < -290:
    #             return False
    #     return True

