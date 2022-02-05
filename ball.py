from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(x=0, y=0)
        self.setheading(45)

    def move_ball(self):
        self.forward(10)
