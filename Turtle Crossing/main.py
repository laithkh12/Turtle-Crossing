import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()  # Renamed from `car`
scoreBoard = Scoreboard()

screen.listen()
screen.onkey(player.goUp, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createCar()
    car_manager.moveCars()

    # Detect collision with car
    for car in car_manager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.gameOver()

    # Detect successful crossing
    if player.isAtFinishLine():
        player.goToStart()
        car_manager.levelUp()
        scoreBoard.increaseLevel()

screen.exitonclick()
