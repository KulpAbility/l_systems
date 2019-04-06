from LSystemCommandsBuilder import LSystemCommandsBuilder
from TurtleCommand import ForwardCommand, PushStateAndTurnLeftCommand, PopStateAndTurnRightCommand


class FractalBinaryTreeCommandsBuilder(LSystemCommandsBuilder):
    def __init__(self):
        pass

    def axiom(self):
        return "0"

    def next_iteration(self, s):
        return s.replace("1", "11").replace("0", "1[0]0")


class FractalBinaryTreeStartingPositionCalculator:
    def calculate(self, commands):
        i = 0
        for c in commands:
            if c != "1":
                break
            i += 1
        return 0, -i


class FractalBinaryTreeCommandInterpreter:
    def __init__(self):
        pass

    @classmethod
    def from_char(cls, char):
        if char == "[":
            return PushStateAndTurnLeftCommand()
        elif char == "]":
            return PopStateAndTurnRightCommand()
        return ForwardCommand()
