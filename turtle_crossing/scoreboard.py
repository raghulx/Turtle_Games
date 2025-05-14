from turtle import Turtle

from matplotlib.lines import drawStyles


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200,300)
        self.color("white")
        self.write(arg= f"Game score is {self.level}", move=False, align='left', font=('Arial', 18, 'normal'))


    def game_over(self):

        game_over = Turtle()
        game_over.color("white")
        game_over.write(arg="Game Over", move=False, align='left', font=('Arial', 18, 'normal'))
        game_over.goto(-200,300)

    def update_score(self):
        self.clear()
        self.write(arg= f"Game score is {self.level}", move=False, align='left', font=('Arial', 18, 'normal'))

    def level_up(self):
        self.level +=1
        self.update_score()
