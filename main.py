from turtle import Screen
from track import Track
from player import Player

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Tartaruga esperta!")
track = Track()
player = Player()
game_on = True
while game_on == True:
    screen.update()
screen.exitonclick()