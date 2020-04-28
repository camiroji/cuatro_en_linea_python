import unittest
from flaskr.game.players import Players

class TestPlayers(unittest.TestCase):

    def setUp(self):
        self.players = Players()
    
    def test_add_player(self):
        self.players.add_player('player')
        self.assertEqual(len(self.players.players), 1)

    def test_raise_when_adding_more_than_two(self):
        self.players.add_player('player')
        self.players.add_player('palyer2')
        with self.assertRaises(Exception):
            self.players.add_player('player3')

    def test_raise_when_duplicated_name(self):
        self.players.add_player('player')
        with self.assertRaises(Exception):
            self.players.add_player('player')

    def test_clear_players(self):
        self.players.add_player('Player')
        self.players.clean_players()
        self.assertEqual(len(self.players.players), 0)

    def test_get_players_ids(self):
        self.players.add_player('player1')
        self.players.add_player('player2')
        self.assertEqual(self.players.get_player_id('player1'), 0)
        self.assertEqual(self.players.get_player_id('player2'), 1)