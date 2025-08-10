from turtle import Turtle

class Track(Turtle): 
    def __init__(self): 
        super().__init__()
        self.pensize(4)
        self.penup()
        self.goto(150, -400)
        self.pendown()
        self.goto(150, 400)
        
        self.draw_line((90, -400))
        self.draw_line((-90, -400))
        
        self.draw_line((30, -400))
        self.draw_line((-30, -400))
        
        self.pensize(4)
        self.penup()
        self.goto(-150, -400)
        self.pendown()
        self.goto(-150, 400)
        
    def draw_line(self, pos): 
        self.setheading(90)
        self.penup()
        self.goto(pos)
        for line in range(30):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
        