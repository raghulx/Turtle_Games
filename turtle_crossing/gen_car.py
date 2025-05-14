from turtle import Turtle
import random


color = ["blue","green","orange","red","white"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []


    def make_car(self):
        dice = random.randint(1,6)
        if dice == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(color))
            car.shapesize(1, 2)
            new_y = random.randint(-250, 250)
            car.goto(300, new_y)
            self.cars.append(car)



    def move_car(self):
        for car in self.cars:
            car.backward(5)