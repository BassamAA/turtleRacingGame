from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.starting_position = STARTING_POSITION

    def move_player(self):
        self.goto(0, self.ycor()+MOVE_DISTANCE)






