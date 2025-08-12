from turtle import Screen
from track import Track
from player import Player
from car import CarConfig
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Tartaruga esperta!")
screen.listen()
track = Track()
player = Player()
car_config = CarConfig()
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
game_on = True
while game_on == True:
    time.sleep(0.1)
    car_config.move_car()
    screen.update()
screen.exitonclick()