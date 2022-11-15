from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Enter a color: ")

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_pos = -240
y_pos = -100
i = 0

for _ in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=x_pos, y=y_pos)
    y_pos += 35
    i += 1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Win! The winning color is {winning_color}!!!")
            else:
                print(f"Lose! The winning color is {winning_color}!!!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()