ALIGNMENT = "center"
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, align=ALIGNMENT, font=('Arial', 13, 'normal'))



    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()