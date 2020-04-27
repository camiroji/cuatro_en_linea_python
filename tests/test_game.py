import unittest
from flaskr.game.game import Game
class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_move_in_empty_column(self):
        player = 1
        column = 0        
        self.game.make_move(player, column)
        self.assertEqual(self.game.board.get_cell(5, 0), player)

    def test_two_moves_in_same_column(self):
        player0 = 0
        player1 = 1
        column = 0
        self.game.make_move(player1, column)       
        self.game.make_move(player0, column)
        self.assertEqual(self.game.board.get_cell(5, 0), player1) 
        self.assertEqual(self.game.board.get_cell(4, 0), player0) 

    def test_finish_game_when_winned(self):
        player0 = 0
        self.assertFalse(self.game.finish)
        self.game.make_move(player0, 1)
        self.game.make_move(player0, 2)
        self.game.make_move(player0, 3)
        self.game.make_move(player0, 4)
        self.assertTrue(self.game.finish)

    def test_tokens_decremented(self):
        player0 = 0
        player1 = 1

        self.game.make_move(player0, 1)
        self.game.make_move(player1, 2)
        self.game.make_move(player1, 3)

        self.assertEqual(self.game.tokens_count[player0], 20)
        self.assertEqual(self.game.tokens_count[player1], 19)

    def test_finish_game_when_no_tokens(self):
        player0 = 0
        player1 = 1
        self.game.tokens_count[player0] = 1
        self.game.tokens_count[player1] = 0
        self.game.make_move(player0, 1)
        self.assertEqual(self.game.tokens_count[player0], 0)
        self.assertTrue(self.game.finish)

    def test_raise_exeption_when_column_move_out_of_range(self):
        player0 = 0
        column_out_range = 9
        with self.assertRaises(Exception):
            self.game.make_move(player0, column_out_range)

    def test_raise_exception_when_row_move_out_of_range(self):
        player0 = 0
        column = 0
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        self.game.make_move(player0, column)
        result = self.game.make_move(player0, column)
        self.assertEqual(result.get('error'), 'No empty space')
                    