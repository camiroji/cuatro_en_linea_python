import unittest
from flaskr.game.game import Game
class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_board_has_6_rows(self):
        self.assertEqual(len(self.game.board), 6)

    def test_rows_has_7_columns(self):
        self.assertEqual(len(self.game.board[0]), 7)

    def test_get_last_row_emtpy(self):
        row_index = self.game.get_last_row_empty(1)
        self.assertEqual(row_index, 5)
        self.game.board[5][1] = 'B'
        row_index = self.game.get_last_row_empty(1)
        self.assertEqual(row_index, 4)

    def test_move_in_empty_column(self):
        player = 1
        column = 0
        palyer_mark = self.game.tokens_mark[player]
        self.game.make_move(player, column)
        self.assertEqual(self.game.board[5][0], palyer_mark)

    def test_two_moves_in_same_column(self):
        player0 = 0
        player1 = 1
        column = 0
        self.game.make_move(player1, column)       
        self.game.make_move(player0, column)
        self.assertEqual(self.game.board[5][0], 'R') # R is the board mark for player 1
        self.assertEqual(self.game.board[4][0], 'B') # B es the board mark for the player 0