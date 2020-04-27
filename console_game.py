from flaskr.game.game import Game

game = Game()
player = 0
while (not game.finish):
    try:
        print(f"Player: {player} Tokens: {game.tokens_count[player]}")
        print(game.board)
        column = int(input('Choose a column form 0 to 6: '))
        game.make_move(int(player), column)
        player = not player
    except Exception as err:
        print(err)
    