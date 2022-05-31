FONT = ("Courier", 24, "normal")
from turtle import Screen, Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create()

    def create(self):
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"LEVEL : {self.score}",font=FONT, align="left")

    def increment_score(self):
        self.clear()
        self.score += 1
        self.create()

    def end_game(self):
        self.clear()
        self.goto(-40,0)
        self.write(f"GAME OVER AT LEVEL : {self.score}", font=FONT, align="center")

