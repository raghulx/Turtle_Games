from turtle import Turtle
from unittest import skipIf
import random

x, y = 0, 0
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
class Snake:

    def __init__(self):

        self.segment = []
        self.initial_cord = 0
        self.create_snake()
        self.head = self.segment[0]
        self.initial_color = 0


    def create_snake(self):

        new_body = Turtle(shape="square")
        new_body.color("green")
        new_body.penup()
        new_body.teleport(x, y)
        self.segment.append(new_body)


    def extend(self):
        #add a new segment to the snake
        new_body = Turtle(shape="square")
        new_body.hideturtle()
        new_body.color("green")
        new_body.penup()
        self.segment.append(new_body)
        self.initial_cord += 20


    def move(self): #segments moves from the last box following the previous box and first one initializes the way

        for seg_num in range(len(self.segment) - 1, 0, -1):
            self.segment[seg_num].showturtle()
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_reset(self):
        for box in self.segment:
            box.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


