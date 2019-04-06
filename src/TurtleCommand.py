class TurtleCommand:
    def type(self):
        raise NotImplementedError('Subclasses must override type()')

    def execute_on(self, turtle):
        raise NotImplementedError('Subclasses must override execute_on()')


class ForwardCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "Forward"

    def execute_on(self, turtle):
        turtle.move()


class PushStateAndTurnLeftCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "PushStateAndTurnLeft"

    def execute_on(self, turtle):
        turtle.push_state()
        turtle.turn_left()


class PopStateAndTurnRightCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "PopStateAndTurnRight"

    def execute_on(self, turtle):
        turtle.pop_state()
        turtle.turn_right()


class PushStateCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "PushStateCommand"

    def execute_on(self, turtle):
        turtle.push_state()


class PopStateCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "PopStateCommand"

    def execute_on(self, turtle):
        turtle.pop_state()


class TurnSlightlyRightCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "TurnSlightlyRightCommand"

    def execute_on(self, turtle):
        turtle.turn_slightly_right()


class TurnSlightlyLeftCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "TurnSlightlyLeftCommand"

    def execute_on(self, turtle):
        turtle.turn_slightly_left()


class NoOpCommand(TurtleCommand):
    def __init__(self):
        super().__init__()

    def type(self):
        return "NoOpCommand"

    def execute_on(self, turtle):
        pass
