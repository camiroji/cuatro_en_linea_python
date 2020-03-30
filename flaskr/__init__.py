import os
from flask import Flask, request
from flaskr.game.game import Game


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    game = Game()

    @app.route('/game')
    def get_game():
        if game.finish:
            game = Game()
        return game.get_game_serialized()

    @app.route('/move', methods = ['POST'])
    def make_move():
        data = request.get_json()
        response = game.make_move(int(data.get('player')), int(data.get('column')))
        return response

    return app