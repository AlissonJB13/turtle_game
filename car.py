from turtle import Turtle
import random

class CarConfig: 
    def __init__ (self):
        self.cars = []
        self.local = [(0,100), (60,100), (120, 100), (-60, 100), (-120, 100)]
        self.create_car()
        
    def create_car(self): 
        new_car = Turtle()
        colors = ['brown', 'white', 'black', 'cyan', 'grey', 'green', 'yellow', 'purple']    
        new_car.shape('square')
        new_car.penup()
        new_car.shapesize(3, 2.5)
        new_car.setheading(270)
        new_car.color(random.choice(colors))
        new_car.goto(random.choice(self.local))
        self.cars.append(new_car)
    
    def move_car(self): 
        for car in self.cars:
            car.forward(20)