from turtle import Turtle, Screen

l = [(100,200),(-100,200)]


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_paddle = 0
        self.r_paddle = 0
        self.screen_update()

    def screen_update(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.l_paddle, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.r_paddle, align="center", font=("Courier", 80, "normal"))

    def l_update(self):
        self.l_paddle += 1
        self.screen_update()

    def r_update(self):
        self.r_paddle += 1
        self.screen_update()








