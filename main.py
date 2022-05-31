import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
cars = CarManager()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.move_player)

while game_is_on:
    cars.createCars()
    time.sleep(0.1)
    screen.update()
    cars.createCars()
    cars.moveCars()

    if player.ycor() > 280:
        player.goto(player.starting_position)
        scoreboard.increment_score()
        cars.levelUp()


    for car in cars.carArr:
        if player.distance(car) < 20:
            scoreboard.end_game()
            game_is_on = False

screen.exitonclick()



