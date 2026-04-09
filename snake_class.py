from typing import List, Any

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle

TURTLE_SHAPE = "square"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    segments: List[Any]

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")
        self.last_move = RIGHT

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_move = self.head.heading()

    def add_segment(self, position):
        new_segment = Turtle(TURTLE_SHAPE)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.last_move != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_move != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.last_move != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_move != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")
