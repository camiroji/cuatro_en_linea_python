import os

from flask import Flask
from flaskr.game.game import Game


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    game = Game()

    @app.route('/game')
    def get_game():
        return game.get_game_serialized()

    return app