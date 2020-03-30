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
        self.game.make_move(player, column)
        self.assertEqual(self.game.board[5][0], player)

    def test_two_moves_in_same_column(self):
        player0 = 0
        player1 = 1
        column = 0
        self.game.make_move(player1, column)       
        self.game.make_move(player0, column)
        self.assertEqual(self.game.board[5][0], player1) 
        self.assertEqual(self.game.board[4][0], player0) 

    def test_check_up(self):
        player0 = 0
        player1 = 1
        column = 0
        self.game.make_move(player0, column)       
        self.game.make_move(player0, column)
        self.game.make_move(player1, column)
        self.game.make_move(player0, column)
        count_up = self.game.check_up(5, 0, player0)
        self.assertEqual(count_up, 1)

    def test_check_down(self):
        player0 = 0
        player1 = 1
        column = 0
        self.game.make_move(player0, column)       
        self.game.make_move(player0, column)
        self.game.make_move(player1, column)
        self.game.make_move(player0, column)
        count_down = self.game.check_down(4, 0, player0)
        self.assertEqual(count_down, 1)

    def test_four_in_vertical(self):
        player0 = 0
        column = 0
        self.game.make_move(player0, column)       
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        result = self.game.four_in_vertical(4, column, player0)
        self.assertTrue(result)

    def test_check_left(self):
        player0 = 0
        player1 = 1
        self.game.make_move(player0, 0)       
        self.game.make_move(player0, 1)
        self.game.make_move(player1, 2)
        self.game.make_move(player0, 3)
        result = self.game.check_left(5, 1, player0)
        self.assertEqual(result, 1)

    def test_check_right(self):
        player0 = 0
        player1 = 1
        self.game.make_move(player0, 0)       
        self.game.make_move(player0, 1)
        self.game.make_move(player1, 2)
        self.game.make_move(player0, 3)
        result = self.game.check_right(5, 0, player0)
        self.assertEqual(result, 1)

    def test_check_four_horizontal(self):
        player0 = 0
        self.game.make_move(player0, 0)       
        self.game.make_move(player0, 1)
        self.game.make_move(player0, 2)
        self.game.make_move(player0, 3)
        result = self.game.four_in_horizontal(5, 2, player0)
        self.assertTrue(result)
