from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(self.score, move=False, align="center", font=("Courier", 80, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, move=False, align="center", font=("Courier", 80, "bold"))
