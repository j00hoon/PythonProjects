from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        #print("nom nom")
        food.move_random()
        snake.extend()
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        #print("game over")
        if not scoreboard.reset():
            game_is_on = False
            scoreboard.game_over()
        snake.reset_snake()

    # Detect collision with any segments in the tail
    if snake.collision_with_segments():
        if not scoreboard.reset():
            game_is_on = False
            scoreboard.game_over()
        snake.reset_snake()



screen.exitonclick()