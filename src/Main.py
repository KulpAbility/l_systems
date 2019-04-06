from turtle import *

from FractalBinaryTree import FractalBinaryTreeCommandsBuilder, FractalBinaryTreeCommandInterpreter, \
    FractalBinaryTreeStartingPositionCalculator
from FractalPlant import FractalPlantCommandsBuilder, FractalPlantCommandsInterpreter, \
    FractalPlantStartingPositionCalculator
from TurtleInterface import *


def sun_thing():
    t = Turtle()
    t.color('red', 'yellow')
    t.begin_fill()
    t.speed(10)
    while True:
        t.forward(200)
        t.left(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()


def fractal_binary_tree(n):
    commands = FractalBinaryTreeCommandsBuilder().iterate(n)
    starting_position = FractalBinaryTreeStartingPositionCalculator().calculate(commands)
    turtle = TurtleInterface(Turtle(), starting_position)
    for char in commands:
        command = FractalBinaryTreeCommandInterpreter.from_char(char)
        command.execute_on(turtle)
    turtle.home()


def fractal_plant(n):
    commands = FractalPlantCommandsBuilder().iterate(n)
    starting_position = FractalPlantStartingPositionCalculator().calculate(commands)
    turtle = TurtleInterface(Turtle(), starting_position)
    for char in commands:
        command = FractalPlantCommandsInterpreter.from_char(char)
        command.execute_on(turtle)
    turtle.home()
