from turtle import Turtle

UP = 0
DOWN = 270


class Paddle(Turtle):

    def __init__(self, initial_position=(0, 0)):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.seth(UP)
        self.shapesize(5, 1)
        self.position(initial_position)

    def position(self, pos):
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)