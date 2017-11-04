import random
from zolegame.players import PlayerInterface

class RandomPlayer(PlayerInterface):
    def newGame(self, uuid, name , points):
        self.uuid = uuid
        self.name = name
        self.points = points
        self.cards = []

    def addCards(self, cards):
        self.cards.extend(cards)

    def updatePoints(self, points):
        self.points += points
        print "UUID:", self.uuid, " points:",self.points

    def selectContract(self, types):
        return random.choice(types)

    def contractSelected(self, uuid, game_type):
        # player selected contract type
        pass
    def selectCard(self, cards):
        # Player must select card to play
        return random.choice(cards)

    def cardPlaced(self, uuid, card):
        # player placed card on table
        pass
    def trickEnd(self, winner, trick_cards):
        if winner ==  self.uuid:
            print "UUID:", winner, " trick:",trick_cards

    def __init__(self):
        pass
