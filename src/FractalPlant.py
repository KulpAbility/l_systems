from LSystemCommandsBuilder import LSystemCommandsBuilder
from TurtleCommand import ForwardCommand, PushStateCommand, PopStateCommand, TurnSlightlyRightCommand, \
    TurnSlightlyLeftCommand, NoOpCommand


class FractalPlantCommandsBuilder(LSystemCommandsBuilder):
    def __init__(self):
        pass

    def axiom(self):
        return "X"

    def next_iteration(self, s):
        return s.replace("F", "FF").replace("X", "F+[[X]-X]-F[-FX]+X")


class FractalPlantStartingPositionCalculator(object):
    def calculate(self, commands):
        i = 0
        for c in commands:
            if c != "F":
                break
            i += 1
        return 0, -i


class FractalPlantCommandsInterpreter:
    def __init__(self):
        pass

    @classmethod
    def from_char(cls, char):
        if char == "[":
            return PushStateCommand()
        elif char == "]":
            return PopStateCommand()
        elif char == "+":
            return TurnSlightlyRightCommand()
        elif char == "-":
            return TurnSlightlyLeftCommand()
        elif char == "F":
            return ForwardCommand()
        else:
            return NoOpCommand()
