import unittest

from FractalBinaryTree import FractalBinaryTreeCommandInterpreter


class TurtleCommandTest(unittest.TestCase):
    def test_that_0_means_forward(self):
        self.assertEqual(FractalBinaryTreeCommandInterpreter.from_char("0").type(), "Forward")

    def test_that_lsquare_means_push_state_and_turn_left(self):
        self.assertEqual(FractalBinaryTreeCommandInterpreter.from_char("[").type(), "PushStateAndTurnLeft")

    def test_that_rsquare_means_pop_state_and_turn_right(self):
        self.assertEqual(FractalBinaryTreeCommandInterpreter.from_char("]").type(), "PopStateAndTurnRight")

    def test_that_1_means_forward(self):
        self.assertEqual(FractalBinaryTreeCommandInterpreter.from_char("1").type(), "Forward")
