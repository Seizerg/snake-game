from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("highscore.txt") as file:
            content= file.read()
        self.highscore = int(content)

    def score_rewrite(self):
        self.clear()
        self.goto(-80, 260)
        self.write(arg=f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(80, 260)
        self.write(arg=f"HighScore:{self.highscore}", move=False, align=ALIGNMENT, font=FONT)


    def add(self):
        self.score += 1


    def reset_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

        self.score=0

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
