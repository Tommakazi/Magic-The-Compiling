import json
import csv
import Deck

colors = ['G', 'B', 'U', 'R', 'W']
mtgEvergreenAbilities = ['Deathtouch', 'Defender', 'Double Strike', 'Enchant', 'Equip', 'First Strike', 'Flash',
                         'Flying', 'Haste', 'Hexproof', 'Indestructible', 'Lifelink', 'Menace', 'Prowess',
                         'Reach', 'Trample', 'Vigilance']
mtgLocations = ['Deck', 'Hand', 'Land', 'Battlefield', 'Graveyard', 'Exile', 'OOP']

mtgControllers = ['Player1', 'Player2']

mtgOtherAbilities = ['UpkeepPay', 'PreventDMG', 'constAttack']

cat = ["targetPow", "targetLoc", "targetAttr", "targetCounter", "targetCopy", "targetControl", "targetDestroy",
       "targetExile", "targetAttach", "targetDamage", "targetTap", "selfPow",
       "selfLoc", "selfAttr", "selfCounter", "selfTap", "batPow", "batAttr", "batCounter", "batOther", "batLand",
       "playerLife", "playerDiscard", "playerMana", "playerDraw", "playerSac",
       "playerRet", "playerMill", "playerScry"]

data = open('TrainingKey.json')
key = json.load(data)

temp = []

class Ability(object):


    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.activate = ""
        self.type = ""
        self.modifier = []
        self.keywords = []

    def set_type(self, Card):

        ability = []

        if 'Creature' or 'Planeswalker' or 'Enchantment' in Card['types']:
            ability.append("Summon Battlefield")

        if 'Land' in Card['types']:
            ability.append("Summon Land")

        if Card.text == "":
            return ability

        with open('trainingSet.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[0] in Card.text:
                    temp.append(row[1])
                else:
                    continue

        categories = []
        for item in temp:
            categories.append(key[item])
        for ab in categories:
            if ab in cat:
                ability.append(ab)

        return Card, ability

    def execute_ability(self, Card, ability):

        data2 = open("tokenData.json")
        token = json.load(data2)

        NLPtext = token[Card.name]

        categories = []
        for item in temp:
            categories.append(key[item])
        for ab in categories:
            if ab == cat[0]:
                target = []
                if '+' in NLPtext['CD'][0]:
                    Card.power += int(NLPtext['CD'][0][-1:])

                print()
            if ab == cat[1]:
                print()
            if ab == cat[2]:
                print()
            if ab == cat[3]:
                print()
            if ab == cat[4]:
                print()
            if ab == cat[5]:
                print()
            if ab == cat[0]:
                print()
            if ab == cat[6]:
                print()
            if ab == cat[7]:
                print()
            if ab == cat[8]:
                print()
            if ab == cat[9]:
                print()
            if ab == cat[10]:
                print()
            if ab == cat[11]:
                print()
            if ab == cat[12]:
                print()
            if ab == cat[13]:
                print()
            if ab == cat[14]:
                print()
            if ab == cat[15]:
                print()
            if ab == cat[16]:
                print()
            if ab == cat[17]:
                print()
            if ab == cat[18]:
                print()
            if ab == cat[19]:
                print()
            if ab == cat[20]:
                print()
            if ab == cat[21]:
                print()
            if ab == cat[22]:
                print()
            if ab == cat[23]:
                print()
            if ab == cat[24]:
                print()
            if ab == cat[25]:
                print()
            if ab == cat[26]:
                print()
            if ab == cat[27]:
                print()
            if ab == cat[28]:
                print()


