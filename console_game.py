from flaskr.game.game import Game

game = Game()
player = False
while not game.finish:
    try:
        print(f"Player: {int(player)} Tokens: {game.tokens_count[int(player)]}")
        print(game.board)
        column = int(input('Choose a column form 0 to 6: '))
        game.make_move(int(player), column)        
    except Exception as err:
        print(err)
    finally:
        player = not player
else:
    print(game.board)
    print('END GAME')