
import time

from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
game_on=True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
    #Detect collision with wall
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        scoreboard.reset()
        snake.reset()
    #Detect collision with tail
    for i in range(1,len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
