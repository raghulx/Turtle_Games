cord = {'start':(0,-300),'end':(0,300)}
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.reset()
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.left(90)
        self.shapesize(1.3,1.3)
        self.goto(cord['start'])

    def up_movement(self):
        new_x = self.xcor()
        new_y = self.ycor() + 15
        self.goto(new_x,new_y)

    def cordinate_fetch(self):
        print(self.xcor())
        print(self.ycor())

