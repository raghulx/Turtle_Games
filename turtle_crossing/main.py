import time
import turtle
from turtle import Screen
from player import Player
from gen_car import Car
from scoreboard import Score
screen = Screen()

def window():

    screen.setup(700,700)
    screen.bgcolor("black")
    screen.screensize(600,600)
    screen.tracer(0)

window()
player = Player()
game_on = True
car = Car()
score = Score()

screen.listen()
screen.onkeypress(player.up_movement, "w")

while game_on:
    time.sleep(0.1)
    screen.update()

    car.make_car()
    car.move_car()

    for out in car.cars:
        if out.distance(player) <= 15:
            game_on = False
            score.game_over()

        if player.ycor() >= 280:
            player.create()
            score.level_up()


screen.exitonclick()