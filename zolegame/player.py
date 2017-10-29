from rules import Rules
from constansts import *

class Player:
    def __init__(self, uuid, name, points):
        self.name = name
        self.uuid = uuid
        self.points = points
        #send to player init message [uuid, name, points]

    def newGame(self):
        self.cards = []
        self.contract = Contract.PARTNER
        self.tricks = []

    def addCards(self, cards):
        self.cards.extend(cards)
        #send to player API "addCards"

    def updatePoints(self, pointChange):
        self.points += pointChange

    def _getContract(self, contract_types):
        #request from API "selectContract"
        return None

    def selectContract(self, contract_types):
        self.contract = self._getContract(contract_types)
        # send to other players contract select message [uuid, contract]
        return self.contract

    def _getCard(self, requested_suit_card):
        # request from API "selectCard"
        return None

    def selectCard(self, requested_suit_card):
        card = self._getCard(requested_suit_card)
        if card in Rules.allowedCards(requested_suit_card, self.cards):
            if len(self.cards)>8:
                # send to other players card message [uuid, Null]
                pass
            else:
                # send to other players card message [uuid, card]
                pass
            self.cards.remove(card)
            return card

    def addTrick(self, trick):
        if len(trick)==3:
            #send to public trick message [uuid, trick]
            pass
        self.tricks.append(trick)

    def __repr__(self):
        return str({
            "name": self.name,
            "uuid" : self.uuid
        })
