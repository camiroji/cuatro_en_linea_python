import unittest
from flaskr.game.game import Game
class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_board_has_6_rows(self):
        self.assertEqual(len(self.game.board), 6)

    def test_rows_has_7_columns(self):
        self.assertEqual(len(self.game.board[0]), 7)