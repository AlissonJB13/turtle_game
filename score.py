from turtle import Turtle

class Score(Turtle):
    def __init__(self): 
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-250, 150)
        self.score_config()
        
    def score_config(self): 
        self.clear()
        self.write(f'Score: \n {self.score}', align="left", font=("arial", 12, "bold"))
    
    def increase_score(self): 
        self.score += 1
        self.score_config()