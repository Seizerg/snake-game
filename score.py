from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",20,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(arg=f"Score:{self.score}",move=False,align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def add(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)
    def gameOver(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)


