import os
from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
from .game.game import Game
from .game.players import Players

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    game = Game() 
    players = Players()  

    @app.route('/player', methods = ['POST'])
    def set_player_id():        
        try:
            data = request.get_json()
            name = data.get('name')
            players.add_player(name)
            return {'Ok': name}
        except Exception as e:
            print(e)
            return {'error': str(e)}

    
    @app.route('/start')
    def start_game():
        global game
        game = Game()
        return game.get_game_serialized()

    @app.route('/game')
    def get_game():
        return game.get_game_serialized()

    @app.route('/move', methods = ['POST'])
    def make_move():
        data = request.get_json()
        name = data.get('player')
        player_id = players.get_player_id(name)
        response = game.make_move(player_id, int(data.get('column')))
        return response

    return app
