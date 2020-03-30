class Game():
    
    def __init__(self):

        self.board = [ [None for _ in range(7)] for _ in range(6)]
        self.tokens_player_1 = 21
        self.tokens_player_2 = 21
        self.finish = False

    def get_game_serialized(self):
        return {
            'board': self.board,
            'tokens_player_1': self.tokens_player_1,
            'tokens_player_2': self.tokens_player_2,
            'finish': self.finish
        }
