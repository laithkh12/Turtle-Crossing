# 🐢 Turtle Crossing Game

A fun Turtle Crossing game built in Python, where the player navigates a turtle to cross a busy road. The player must avoid incoming cars to successfully cross and increase their level, with each level adding more speed and challenge. 🛣️🚗

## 🎮 Game Features
- **Player Movement**: Move the turtle upward using the **Up Arrow** key.
- **Randomly Generated Cars**: Cars of various colors move horizontally across the screen.
- **Scoreboard**: Tracks the player's current level.
- **Game Over**: Game ends if the turtle collides with a car.

## 🛠️ Modules and Classes

### `main.py`
The main script that initializes the game environment, controls the game loop, and handles collisions and level-ups.

```python
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()  # Car manager for handling all car operations
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
```

### player.py
Defines the Player class, representing the turtle that the player controls. The turtle moves up and resets to the starting position upon a successful crossing.
```python
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goToStart()
        self.setheading(90)

    def goUp(self):
        self.forward(MOVE_DISTANCE)

    def goToStart(self):
        self.goto(STARTING_POSITION)

    def isAtFinishLine(self):
        return self.ycor() > FINISH_LINE_Y
```

### scoreboard.py
The Scoreboard class manages the game level and displays a game-over message when the turtle collides with a car.
```python
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increaseLevel(self):
        self.level += 1
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
```

### car_manager.py
The CarManager class handles car creation, movement, and increasing the car speed with each level-up.
```python
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        randomChance = random.randint(1, 6)
        if randomChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250, 250)
            newCar.goto(300, randomY)
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT
```

## 📦 Installation and Usage
1. Clone the Repository:
```bash
git clone https://github.com/your-username/turtle-crossing-game.git
cd turtle-crossing-game
```
2. Run the Game: Make sure you have Python installed, then run:
```bash
python main.py
```

## 🚀 How to Play
1. Use the Up Arrow key to move the turtle upwards.
2. Avoid incoming cars and cross to the other side to increase your level.
3. Game ends if you collide with a car.

## 🖼️ Game Preview
<img src="https://github.com/user-attachments/assets/56d151af-b3a7-4a37-8656-d0d7cfb0bf07" alt="Game Preview" width="400"/>




Enjoy the game and have fun crossing! 😄

