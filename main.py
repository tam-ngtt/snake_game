from turtle import Screen
from snake import Snake
from food import Food
from scroreboard import ScoreBoard
import time

"""Screen Setup"""
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Hungry Snake")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = 0
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score += 1
        snake.extend()
        food.random_pos()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.update_high_score()

    # Detect collision with the Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            snake.reset()
            scoreboard.update_high_score()

screen.exitonclick()
