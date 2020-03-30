class Game():
    
    def __init__(self):

        self.board = [ [None for _ in range(7)] for _ in range(6)]
        self.tokens_count = [21, 21]
        self.tokens_mark = ['B', 'R']
        self.finish = False

    def get_game_serialized(self):
        return {
            'board': self.board,
            'tokens_count': self.tokens_count,
            'finish': self.finish
        }

    def make_move(self, player, column):
        if self.tokens_count[player] == 0:
            return {'error': 'No tokens available'}

        self.update_board(self.tokens_mark[player], column)
        if self.game_winned():
            self.finish = True

        self.tokens_count[player] -= 1

        return self.get_game_serialized()

    def update_board(self, mark, column):
        row = self.get_last_row_empty(column)
        self.board[row][column] = mark

    def get_last_row_empty(self, column):
        for raw_index in range(5, 0, -1):
            if self.board[raw_index][column] == None:
                return raw_index

    def game_winned(self):
        return False