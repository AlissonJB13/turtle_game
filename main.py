from turtle import Screen
from track import Track
from player import Player
from car import CarConfig
from score import Score
import time
import turtle

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Tartaruga esperta!")
screen.listen()
screen.bgcolor("beige")

track = Track()

player = Player()

score = Score()

car_config = CarConfig()

screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

game_on = True

while game_on == True:
    time.sleep(0.1)
    car_config.appear_car()
    car_config.move_car()
    if player.xcor() > 120 or player.xcor() < -120:
        turtle.write(f"Game Over!", align="center", font=("arial", 20, "bold"))
        game_on = False
    for car_index in car_config.cars: 
        if abs(player.xcor() - car_index.xcor()) < 1 and player.distance(car_index) < 65:
            turtle.write(f"Game Over!", align="center", font=("arial", 20, "bold"))
            game_on=False
        if car_index.ycor() < -230:
            score.increase_score()
            car_index.hideturtle()
            car_config.cars.remove(car_index)
    screen.update()
    
screen.exitonclick()