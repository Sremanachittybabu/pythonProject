from turtle import Turtle
STARTING_POSITIONS = [(0,  0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            t1 = Turtle("square")
            t1.color("white")
            t1.penup()
            t1.goto(position)
            self.segments.append(t1)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[i - 1].xcor()
            y_pos = self.segments[i - 1].ycor()
            self.segments[i].goto(x_pos, y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


