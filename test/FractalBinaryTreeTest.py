
import unittest

from FractalBinaryTree import FractalBinaryTreeCommandsBuilder


class FractalBinaryTreeTest(unittest.TestCase):
    def test_that_gets_first_iteration(self):
        self.assertEqual(FractalBinaryTreeCommandsBuilder().iterate(0), "0")

    def test_that_gets_second_iteration(self):
        self.assertEqual(FractalBinaryTreeCommandsBuilder().iterate(1), "1[0]0")

    def test_that_gets_third_iteration(self):
        self.assertEqual(FractalBinaryTreeCommandsBuilder().iterate(2), "11[1[0]0]1[0]0")

    def test_that_gets_fourth_iteration(self):
        self.assertEqual(FractalBinaryTreeCommandsBuilder().iterate(3), "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0")


if __name__ == '__main__':
    unittest.main()
