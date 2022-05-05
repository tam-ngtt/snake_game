from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a snake on the screen"""
        for position in STARTING_POSITION:
            self.create_segment(position)

    def extend(self):
        """Create a new snake segment at the tail of the snake"""
        self.create_segment(self.segments[-1].position())

    def create_segment(self, position):
        """Create a snake segment"""
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        self.segments.append(segment)
        segment.setposition(position)

    def move(self):
        """Move the snake forward"""
        for part_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part_num - 1].xcor()
            new_y = self.segments[part_num - 1].ycor()
            self.segments[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

