from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # These are initial values set for creating the snake body
    def __init__(self, segments):
        self.snakes = []
        self.createBody(segments)
        self.head = self.snakes[0]

    # This function creates the snake body with a desirable number of segments
    def createBody(self, segments):
        self.snake_part = segments
        # I created snake head outside the list of snakes because i wanted to have to desirable number of snake segments
        snake_head = Turtle(shape="square")
        snake_head.penup()
        snake_head.color("white")
        self.initialpos = snake_head.xcor()
        self.snakes.append(snake_head)
        # This loop creates snake whole body after snake head
        for i in range(self.snake_part):
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            self.initialpos -= 20
            snake.goto(x=self.initialpos, y=0)
            self.snakes.append(snake)
    def extend(self):
        last_position=self.snakes[-1].position()
        segment=  Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(last_position)
        self.snakes.append(segment)



    # This function triggers the movement of snake and it moves like a caterpillar pattern
    def move(self):
        # It first moves the last body segement to its second last segment position and it goes on till the whole body
        # moves
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].xcor(), self.snakes[i - 1].ycor())
        self.head.fd(MOVE_DIST)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def reset(self,segments):
        for parts in self.snakes:
            parts.goto(1000,1000)
        self.__init__(segments)