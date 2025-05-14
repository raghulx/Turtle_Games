from turtle import Turtle
from types import new_class
import time

class Ball(Turtle):

    def __init__(self,screen):
        super().__init__()
        self.scree = screen
        self.make_ball()
        self.x_move = 4
        self.y_move = 4
        self.l_win = 0
        self.r_win = 0


    def make_ball(self):

        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(60)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1


    def bounce_y(self):
        self.y_move *= -1

    def booster(self):
        for i in range(20):
            if self.ycor() >= 270 or self.ycor() <= -270:
                continue
            else:
                self.move()

    def reseter(self):
        self.goto(0,0)
        self.bounce_x()












