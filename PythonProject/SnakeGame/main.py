from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

x_pos = 0
y_pos = 0
all_turtles = []

for _ in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.goto(x_pos, y_pos)
    new_turtle.color("white")
    x_pos -= 20
    all_turtles.append(new_turtle)


# turtle = Turtle(shape="square")
# turtle.goto(0, 0)
# turtle.color("white")
#
# turtle2 = Turtle(shape="square")
# turtle2.goto(-20, 0)
# turtle2.color("white")
#
# turtle3 = Turtle(shape="square")
# turtle3.goto(-40, 0)
# turtle3.color("white")










screen.exitonclick()