

class Player(object):

    def __init__(self):
        self.name = ""
        self.mana = {"White": 0, "Blue": 0, "Black": 0, "Red": 0, "Green": 0, "CM": 0}
        self.lifePoints = 20
        self.hasLost = False
        self.controlled = []

    def create_player(self, name):
        player = Player()
        player.mana = {"White": 0, "Blue": 0, "Black": 0, "Red": 0, "Green": 0, "Total": 0}
        player.lifePoints = 20
        player.hasLost = False
        return player

    def gainLife(self, Player, life):
        Player.lifePoints = Player.lifePoints + life

    def loseLife(self, Player, life):
        Player.lifePoints = Player.lifePoints - life

    def lose(self, Player):
        if Player.lifePoints <= 0:
            Player.hasLost = True

    def getLife(self, Player):
        return Player.lifePoints





