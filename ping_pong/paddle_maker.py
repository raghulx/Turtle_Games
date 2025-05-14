#Default values
cords = [(-350,0),(350,0)]



from turtle import Turtle

class Paddle:

    def __init__(self):
        self.paddle_list = []
        self.make_paddle()
        self.left_paddle = self.paddle_list[0]
        self.right_paddle = self.paddle_list[1]


    def make_paddle(self):
        for cord in cords:
            pa = Turtle()
            pa.speed("fast")
            pa.penup()
            pa.color("white")
            pa.speed("fast")
            pa.shape("square")
            pa.shapesize(stretch_wid=5, stretch_len=1)
            pa.goto(cord)
            self.paddle_list.append(pa)

    def left_up(self):
        if self.left_paddle.ycor() <= 270:
            self.left_paddle.sety(self.left_paddle.ycor() + 25)


    def left_down(self):
        if self.left_paddle.ycor() >= -270:
            self.left_paddle.sety(self.left_paddle.ycor() - 25)

    def right_up(self):
        if self.right_paddle.ycor() <= 270:
            self.right_paddle.sety(self.right_paddle.ycor() + 25)

    def right_down(self):
        if self.right_paddle.ycor() >= -270:
            self.right_paddle.sety(self.right_paddle.ycor() - 25)
