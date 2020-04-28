class Players:

    def __init__(self):
        self.players = {}

    def add_player(self, name):
        if len(self.players) >= 2:
            raise Exception('The amount of players is full')
        else:
            if name in self.players:
                raise Exception('Duplicated player name')
            self.players.update({name: len(self.players)})

    def clean_players(self):
        self.players = {}

    def get_player_id(self, name):
        return self.players.get(name)

