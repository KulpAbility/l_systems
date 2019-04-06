class TurtleInterface:
    def __init__(self, turtle, starting_position):
        self.state_stack = StateStack()
        self.color = GreenScale()
        self.turtle = turtle
        self.turtle.pencolor(self.color.rgb())
        self.turtle.setposition(starting_position)
        self.turtle.setheading(90)
        self.turtle.speed(10)

    def move(self):
        self.turtle.forward(2)

    def turn_left(self):
        self.turtle.left(45)

    def turn_slightly_left(self):
        self.turtle.left(25)

    def turn_right(self):
        self.turtle.right(45)

    def turn_slightly_right(self):
        self.turtle.right(25)

    def push_state(self):
        self.color.lighter()
        self.turtle.pencolor(self.color.rgb())
        self.state_stack.push(self.turtle.heading(), self.turtle.position())

    def pop_state(self):
        # self.color.darker()
        # self.turtle.pencolor(self.color.rgb())
        (heading, position) = self.state_stack.pop()
        self.turtle.penup()
        self.turtle.setheading(heading)
        self.turtle.setposition(position)
        self.turtle.pendown()

    def home(self):
        self.turtle.penup()
        self.turtle.home()
        self.turtle.setheading(90)


class GreenScale():
    def __init__(self):
        self.greenness = 10
        self.greening_rate = 2
        self.greening_threshold = 255 / self.greening_rate

    def lighter(self):
        self.greenness += 1

    def darker(self):
        self.greenness = min(self.greenness, 10)

    def rgb(self):
        return self.r() / 255, self.g() / 255, self.b() / 255

    def r(self):
        if self.greenness <= self.greening_threshold:
            return 0
        else:
            return min((self.greenness - self.greening_threshold) * self.greening_rate, 180)

    def g(self):
        return min(self.greenness * self.greening_rate, 255)

    def b(self):
        if self.greenness <= self.greening_threshold:
            return 0
        else:
            return min((self.greenness - self.greening_threshold) * self.greening_rate, 180)


class StateStack:
    def __init__(self):
        self.stack = []

    def push(self, heading, position):
        self.stack.append((heading, position))

    def pop(self):
        return self.stack.pop()
