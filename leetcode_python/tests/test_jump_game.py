import unittest

from leetcode_python.src.algorithms.arrays.jump_game import JumpGame


class TestJumpGame(unittest.TestCase):

    def test_can_reach_last_index(self):
        game = JumpGame()
        self.assertTrue(game.can_reach_last_index([2, 3, 1, 1, 4]))

    def test_can_reach_last_index_failure(self):
        game = JumpGame()
        self.assertFalse(game.can_reach_last_index([3, 2, 1, 0, 4]))
