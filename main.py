from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # code used to show the screen
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.snake_reset()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.reset()
            snake.snake_reset()

with open("data.txt") as score_score:
    content = score_score.read()
    type(content)
screen.exitonclick()

# For more of my projects, fun games and useful applicatons, 
# please visit: https://github.com/thlouieshi?tab=repositories
