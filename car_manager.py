from turtle import Turtle
import time
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEVEL = 10
CAR_Y_POSITION = [-210,-170,-140,-110,-50,-20,30,70,100,130,160,190,240]


class CarManager(Turtle):
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.carArr = []

    def createCars(self):
        randomChance = random.randint(1,9)
        if randomChance == 1:
            turtle = Turtle()
            turtle.shapesize(1, 2)
            turtle.penup()
            turtle.shape("square")
            turtle.color(random.choice(COLORS))

            turtle.setposition(250, random.randint(-235, 250))
            self.carArr.append(turtle)


    def moveCars(self):
        for c in self.carArr:
            c.backward(self.car_speed)

    def levelUp(self):
        self.car_speed += 1




