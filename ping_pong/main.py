import turtle
from turtle import Turtle, Screen
from paddle_maker import Paddle
from controls import Controls
from ball import Ball
from Scoreboard import Score
#initialize variable
Game_on = True
Game_turn = 0


def screen_setup():
    """screen setup"""
    window.bgcolor("black")
    window.title("ping pong game")
    window.setup(width=800, height=600)
    window.screensize(canvwidth=1000, canvheight=800)
    window.tracer(0)

window = Screen()
screen_setup() #setting up initial screen
paddle = Paddle() #setting up paddle
ball = Ball(window)
Score = Score()
control = Controls(window, paddle) #takes care of onscreen control and inbuilt loop taking care of paddle movement
ball.goto(310,270)
while Game_on:
    i = 0
    Game_turn += 1
    window.update()

    turtle.ontimer(ball.move(), 1)

    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.booster()
        ball.bounce_y()


    if ball.xcor() >= 380:
        """right wall"""
        ball.reseter()
        Score.r_update()

    if ball.xcor() <= -380:
        """left wall"""
        ball.reseter()
        Score.l_update()

    if ball.distance(paddle.right_paddle) <= 50 and ball.xcor() <= 370 or ball.distance(paddle.left_paddle) <= 50 and ball.xcor() >= -370:
            ball.bounce_x()
            ball.booster()


window.mainloop()
#speed and infinite glitch more






