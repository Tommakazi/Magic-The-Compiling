class Player(object):
    name = ""
    mana = {"White":0, "Blue":0, "Black":0, "Red":0, "Green":0, }
    lifePoints = 20
    hasLost = False


    def __init__(self, name, mana, lifePoints, hasLost):
        self.name = name
        self.mana = mana
        self.lifePoints = lifePoints
        self.hasLost = hasLost

def create_player(name):
    mana = {"White": 0, "Blue": 0, "Black": 0, "Red": 0, "Green": 0, "Total": 0,  }
    lifePoints = 20
    hasLost = False
    player = Player(name, mana, lifePoints, hasLost)
    return player

def gainLife(Player, life):
    Player.lifePoints = Player.lifePoints + life

def loseLife(Player, life):
    Player.lifePoints = Player.lifePoints - life

def lose(Player):
    if Player.lifePoints <= 0:
        Player.hasLost = True

def getLife(Player):
    return Player.lifePoints





