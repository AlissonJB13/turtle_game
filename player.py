from turtle import Turtle

class Player(Turtle): 
    def __init__(self): 
        super(Player, self).__init__()
        self.shape('turtle')
        self.shapesize(3,3)
        self.setheading(90)
        self.penup()
        self.goto(0, -220)
        
    def move_right(self): 
        new_pos = self.xcor()+60
        self.goto(new_pos, self.ycor())
    
    def move_left(self): 
        new_pos = self.xcor()-60
        self.goto(new_pos, self.ycor())