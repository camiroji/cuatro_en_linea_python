from flaskr.game.board import Board

class Game():
    
    def __init__(self):
        self.board = Board()
        self.tokens_count = [21, 21]
        self.finish = False

    def get_game_serialized(self):
        board_s = self.board.get_board_serializable()
        response = {
            'tokens_count': self.tokens_count,
            'finish': self.finish
        }
        response.update(board_s)
        return response

    def make_move(self, player, column):
        if column < 0 or column > 6:
            raise Exception(f"Column {column} out of range")

        if self.tokens_count[player] == 0:
            return {'error': 'No tokens available'}

        try:
            updated_row = self.board.update_board(player, column)
        except Exception as err:
            return {'error': str(err)}

        if self.game_winned(updated_row, column, player):
            self.finish = True

        self.tokens_count[player] -= 1

        if self.tokens_count[0] == 0 and self.tokens_count[1] == 0:
            self.finish = True

        return self.get_game_serialized()   

    def game_winned(self, row, column, player):
        return self.board.four_in_vertical(row, column, player) or \
            self.board.four_in_horizontal(row, column, player) or \
            self.board.four_diagonal_right(row, column, player) or \
            self.board.four_diagonal_left(row, column, player)
