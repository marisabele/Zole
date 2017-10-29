from rules import Rules
from constansts import *

class Player:
    def __init__(self, uuid, name, points, client = None):
        self.name = name
        self.uuid = uuid
        self.points = points
        self.client = client
        self._sendToClient("init", [uuid, name, points])

    def newGame(self):
        self.cards = []
        self.contract = Contract.PARTNER
        self.tricks = []

    def addCards(self, cards):
        self.cards.extend(cards)
        self._sendToClient("addCards", cards)

    def updatePoints(self, pointChange):
        self.points += pointChange
        self._sendToClient("pointChange", pointChange)

    def _getContract(self, contract_types):
        return self._sendToClient("selectcontract", contract_types)

    def selectContract(self, contract_types):
        self.contract = self._getContract(contract_types)
        self._sendToPublic("selectcontract", [self.uuid, self.contract])
        return self.contract

    def _getCard(self, requested_suit_card):
        return self._sendToClient("selectcard", Rules.allowedCards(requested_suit_card, self.cards))

    def selectCard(self, requested_suit_card):
        card = self._getCard(requested_suit_card)
        if card in Rules.allowedCards(requested_suit_card, self.cards):
            if len(self.cards)>8:
                self._sendToPublic("selectcard", [self.uuid, None])
            else:
                self._sendToPublic("selectcard", [self.uuid, card])
            self.cards.remove(card)
            return card

    def addTrick(self, trick):
        if len(trick) == 3:
            self._sendToClient("trick", trick)
        self.tricks.append(trick)

    def _sendToClient(self, message, data):
        return None

    def _sendToPublic(self,message, data):
        pass

    def __repr__(self):
        return str({
            "name": self.name,
            "uuid" : self.uuid
        })
