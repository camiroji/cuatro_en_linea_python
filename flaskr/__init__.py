import os
from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
from .game.game import Game

count_players = 0

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    game = Game()   

    @app.route('/player')
    def get_player_id():
        global count_players
        if count_players <= 1:
            response = {'player_id': count_players}    
            count_players += 1
            return response
        else: 
            return {'error': 'No players available'}    
    
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
        response = game.make_move(int(data.get('player')), int(data.get('column')))
        return response

    return app
