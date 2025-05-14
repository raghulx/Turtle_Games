from turtle import Turtle,Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 500, height= 400)

user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race. Enter the color")
colors = ["red","orange","green","blue","yellow","purple"]

turtlez = []
temp = 0

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230 , y=-110 + temp)
    temp += 50
    turtlez.append(tim)
race_is_on = True
if user_bet:
    i = 0
    winner_turtle = ""
    while race_is_on:

        for turtle in turtlez:
            turtle.forward(random.randrange(1, 10))
            if round(turtle.xcor(), 2) >= 190:
                race_is_on = False
                winner_turtle = turtle
                break

    if user_bet == winner_turtle.color()[0]:
        print(f"You are right, the color {winner_turtle.color()[0]} you chose has won")
    else:
        print(f"You have lost, the color which won is {winner_turtle.color()[0]}")
        print(f"Your choice of color was {user_bet}")

screen.exitonclick()
