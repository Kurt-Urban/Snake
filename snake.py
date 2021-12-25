from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(-20 * segment, 0)
            self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(
                self.segments[i - 1].xcor(), self.segments[i - 1].ycor()
            )
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_pos = self.segments[(len(self.segments) - 1)].pos()
        new_segment.goto(new_pos)
        self.segments.append(new_segment)

    def left(self):
        hding = self.head.heading()
        if hding != 0:
            self.head.setheading(180)

    def right(self):
        hding = self.head.heading()
        if hding != 180:
            self.head.setheading(0)

    def up(self):
        hding = self.head.heading()
        if hding != 270:
            self.head.setheading(90)

    def down(self):
        hding = self.head.heading()
        if hding != 90:
            self.head.setheading(270)
