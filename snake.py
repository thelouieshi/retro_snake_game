import turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

class Snake:
    def __init__(self):
        self.segments = []
        self.cor_x = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for n in range(0, 3):
            new_segment = turtle.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.cor_x, 0)
            self.segments.append(new_segment)
            self.cor_x = self.cor_x - 20

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def snake_reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position()) # last segment's position