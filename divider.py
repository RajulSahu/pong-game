from turtle import Turtle


class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, -290)
        self.setheading(90)
        self.pensize(10)
        for x in range(575):
            if x % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(20)

