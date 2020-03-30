class Game():
    
    def __init__(self):

        self.board = [ [None for _ in range(7)] for _ in range(6)]
        self.tokens_count = [21, 21]
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

        updated_row = self.update_board(player, column)
        if self.game_winned(updated_row, column, player):
            self.finish = True

        self.tokens_count[player] -= 1

        return self.get_game_serialized()

    def update_board(self, mark, column):
        row = self.get_last_row_empty(column)
        self.board[row][column] = mark
        return row

    def get_last_row_empty(self, column):
        for raw_index in range(5, 0, -1):
            if self.board[raw_index][column] == None:
                return raw_index

    def game_winned(self, row, column, player):
        return self.four_in_vertical(row, column, player) or \
            self.four_in_horizontal(row, column, player) or \
            self.four_diagonal_right(row, column, player) or \
            self.four_diagonal_left(row, column, player)

    def four_in_vertical(self, row, column, player):
        count = 1
        cant_up = self.check_up(row, column, player)
        cant_down = self.check_down(row, column, player)
        return count + cant_up + cant_down >= 4

    def check_up(self, row, column, player):
        count = 0
        for row_index in range(row - 1, -1, -1):
            if self.board[row_index][column] == player:
                count += 1
            else:
                break
        return count

    def check_down(self, row, column, player):
        count = 0
        for row_index in range(row + 1, 6):
            if self.board[row_index][column] == player:
                count += 1
            else:
                break
        return count

    def four_in_horizontal(self, row, column, player):
        count = 1
        count_left = self.check_left(row, column, player)
        count_right = self.check_right(row, column, player)
        return count + count_left + count_right >= 4

    def check_left(self, row, column, player):
        count = 0
        for column_index in range(column - 1, -1, -1):            
            if self.board[row][column_index] == player:
                count += 1
            else:
                break
        return count

    def check_right(self, row, column, player):
        count = 0
        for column_index in range(column + 1, 7):
            if self.board[row][column_index] == player:
                count += 1
            else:
                break
        return count

    def four_diagonal_right(self, row, column, player):
        count = 1
        count_right_diagonal_up = self.check_right_diagonal_up(row, column, player)
        count_left_diagonal_down = self.check_left_diagonal_down(row, column, player)
        return count + count_right_diagonal_up + count_left_diagonal_down >= 4

    def check_right_diagonal_up(self, row, column, player):
        count = 0
        if column > 6 or row < 0:
            return count
        
        pos_col = column + 1
        for row_index in range(row - 1, -1, -1):            
            if self.board[row_index][pos_col] == player:
                count += 1
                pos_col += 1
            else:
                break
        return count

    def check_left_diagonal_down(self, row, column, player):
        count = 0
        if column < 0 or row > 6:
            return count

        pos_col = column -1
        for row_index in range(row + 1, 6):
            if self.board[row_index][pos_col] == player:
                count += 1
                pos_col -= 1
            else:
                break
        return count

    def four_diagonal_left(self, row, column, player):
        count = 1
        count_left_up = self.check_diagonal_left_up(row, column, player)
        count_right_down = self.check_diagonal_right_down(row, column, player)
        return count + count_left_up + count_right_down >= 4

    def check_diagonal_left_up(self, row, column, player):
        count = 0
        pos_col = column - 1

        if column < 0 or row < 0:
            return count

        for row_index in range(row - 1, - 1, -1):
            if self.board[row_index][pos_col] == player:
                count += 1
                pos_col -= 1
            else:
                break
        return count

    def check_diagonal_right_down(self, row, column, player):
        count = 0
        pos_col = column + 1

        if row > 6 or column > 7:
            return count

        for row_index in range(row + 1, 6):
            if self.board[row_index][pos_col] == player:
                count += 1
                pos_col += 1
            else:
                break
        return count