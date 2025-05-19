import turtle
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



def update():
    screen.update()
    time.sleep(0.1)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_on = True
food = Food()
score = ScoreBoard()

while is_game_on:

    update()
    snake.move()

    #detech food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detect wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280  or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.snake_reset()
        score.game_reset()

    #head collision

    for segment in snake.segment[1:]:
         if segment == snake.head:
             pass

         elif snake.head.distance(segment) < 10:
             snake.snake_reset()
             score.game_reset()



turtle.done()
screen.exitonclick()


