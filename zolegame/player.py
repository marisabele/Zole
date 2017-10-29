from rules import Rules
from constansts import *

class Player:
    def __init__(self, uuid, name, points):
        self.name = name
        self.uuid = uuid
        self.points = points

    def newGame(self):
        self.cards = []
        self.contract = Contract.PARTNER
        self.tricks = []

    def addCards(self, cards):
        self.cards.extend(cards)

    def updatePoints(self, pointChange):
        self.points += pointChange

    def _getContract(self, contract_types):
        return None

    def selectContract(self, contract_types):
        self.contract = self._getContract(contract_types)
        # send to other players contract select message
        return self.contract

    def _getCard(self, requested_suit_card):
        return None

    def selectCard(self, requested_suit_card):
        card = self._getCard(requested_suit_card)
        if card in Rules.allowedCards(requested_suit_card, self.cards):
            self.cards.remove(card)
            return card
        
    def addTrick(self, trick):
        self.tricks.append(trick)

    def __repr__(self):
        return str({
            "name": self.name,
            "uuid" : self.uuid
        })
