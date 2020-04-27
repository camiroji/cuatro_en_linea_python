import unittest
from flaskr.game.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_repr_board(self):
        print(self.board)

    def test_board_has_6_rows(self):
        self.assertEqual(len(self.board.board), 6)

    def test_rows_has_7_columns(self):
        self.assertEqual(len(self.board.get_row(0)), 7)

    def test_get_last_row_emtpy(self):
        row_index = self.board.get_last_row_empty(1)
        self.assertEqual(row_index, 5)
        self.board.set_cell(5, 1, 'B')
        row_index = self.board.get_last_row_empty(1)
        self.assertEqual(row_index, 4)

    def test_check_up(self):
        player0 = 0
        player1 = 1
        column = 0
        self.board.set_cell(5, column, player0)
        self.board.set_cell(4, column, player0)
        self.board.set_cell(3, column, player1)
        self.board.set_cell(2, column, player0)
        count_up = self.board.check_up(5, 0, player0)
        self.assertEqual(count_up, 1)

    def test_check_down(self):
        player0 = 0
        player1 = 1
        column = 0
        self.board.set_cell(5, column, player0)
        self.board.set_cell(4, column, player0)
        self.board.set_cell(3, column, player1)
        self.board.set_cell(2, column, player0)
        count_down = self.board.check_down(4, 0, player0)
        self.assertEqual(count_down, 1)

    def test_four_in_vertical(self):
        player0 = 0
        column = 0
        self.board.set_cell(5, column, player0)
        self.board.set_cell(4, column, player0)
        self.board.set_cell(3, column, player0)
        self.board.set_cell(2, column, player0)
        result = self.board.four_in_vertical(4, column, player0)
        self.assertTrue(result)

    def test_check_left(self):
        player0 = 0
        player1 = 1
        row = 5
        self.board.set_cell(row, 0, player0)
        self.board.set_cell(row, 1, player0)
        self.board.set_cell(row, 2, player1)
        self.board.set_cell(row, 3, player0)
        result = self.board.check_left(5, 1, player0)
        self.assertEqual(result, 1)

    def test_check_right(self):
        player0 = 0
        player1 = 1
        row = 5
        self.board.set_cell(row, 0, player0)
        self.board.set_cell(row, 1, player0)
        self.board.set_cell(row, 2, player1)
        self.board.set_cell(row, 3, player0)
        result = self.board.check_right(5, 0, player0)
        self.assertEqual(result, 1)

    def test_check_four_horizontal(self):
        player0 = 0
        row = 5
        self.board.set_cell(row, 0, player0)
        self.board.set_cell(row, 1, player0)
        self.board.set_cell(row, 2, player0)
        self.board.set_cell(row, 3, player0)
        result = self.board.four_in_horizontal(5, 2, player0)
        self.assertTrue(result)

    def test_check_right_diagonal_up(self):
        player0 = 0
        self.board.set_cell(5, 0, player0)
        self.board.set_cell(5, 1, player0)
        self.board.set_cell(4, 1, player0)
        result = self.board.check_right_diagonal_up(5, 0, player0)
        self.assertEqual(result, 1)

    def test_check_left_diagonal_down(self):
        player0 = 0
        self.board.set_cell(5, 0, player0)
        self.board.set_cell(5, 1, player0)
        self.board.set_cell(4, 1, player0)
        result = self.board.check_left_diagonal_down(4, 1, player0)
        self.assertEqual(result, 1)

    def test_check_diagonal_left_up(self):
        player0 = 0
        self.board.set_cell(5, 0, player0)
        self.board.set_cell(4, 0, player0)
        self.board.set_cell(3, 0, player0)
        self.board.set_cell(5, 1, player0)
        self.board.set_cell(4, 1, player0)
        result = self.board.check_diagonal_left_up(5, 1, player0)
        self.assertEqual(result, 1)

    def test_check_diagonal_right_down(self):
        player0 = 0
        self.board.set_cell(5, 0, player0)
        self.board.set_cell(4, 0, player0)
        self.board.set_cell(3, 0, player0)
        self.board.set_cell(5, 1, player0)
        self.board.set_cell(4, 1, player0)
        result = self.board.check_diagonal_right_down(4, 0, player0)
        self.assertEqual(result, 1)