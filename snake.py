from turtle import Turtle

starting_position = [(0,0), (-20,0), (-40,0)]
move_distance = 20
class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        bor = Turtle()
        bor.shape("square")
        bor.penup()
        bor.color("red")
        bor.goto(position)
        self.segments.append(bor)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(move_distance)

    def turn_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_south(self):
        if self.head.heading() !=90 :
            self.head.setheading(270)

    def turn_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
