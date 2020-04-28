import pytest
from flaskr import create_app

class TestAPI:
    
    def setup_method(self):
        self.app = create_app()
        self.app.testing = True

    def test_set_player(self):
        with self.app.test_client() as c:
            rv = c.post('/player', json={'name': 'test'})
            assert 'Ok' in rv.get_json()


    def test_set_two_players(self):    
        with self.app.test_client() as c: 
            rv1 = c.post('/player', json={'name': 'player1'})
            rv2 = c.post('/player', json={'name': 'player2'})
            assert 'Ok' in rv1.get_json()
            assert 'Ok' in rv2.get_json()

    def test_return_error_when_amount_players_full(self):
        with self.app.test_client() as c: 
            c.post('/player', json={'name': 'player1'})
            c.post('/player', json={'name': 'player2'})
            rv = c.post('/player', json={'name': 'test'})
            assert 'error' in rv.get_json()

    def test_return_error_when_duplicated_name(self):
        with self.app.test_client() as c: 
            c.post('/player', json={'name': 'player1'})
            rv = c.post('/player', json={'name': 'player1'})           
            assert 'error' in rv.get_json()            
            
    def test_start_game(self):
        with self.app.test_client() as c:
            rv = c.get('/start')
            response = rv.get_json()
            assert response.get('finish') == False
            assert response.get('tokens_count') == [21, 21]