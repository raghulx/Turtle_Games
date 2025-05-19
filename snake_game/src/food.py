from turtle import Turtle
import random

static_x = 0
static_y = 0

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.color("blue")
        self.speed("fastest")
        self.x = 20
        self.y = 0
        self.tester()



    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)


    def tester(self):

        self.teleport(self.x,self.y)
        self.x += 20

