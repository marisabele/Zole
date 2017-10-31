from rules import Rules
from constansts import *

class Player:
    def __init__(self, uuid, name, points, client = None, game = None):
        self.name = name
        self.uuid = uuid
        self.points = points
        self.client = client
        self.game = game
        self.sendToClient("init", [uuid, name, points])

    def newGame(self):
        self.cards = []
        self.contract = Contract.PARTNER
        self.tricks = []

    def addCards(self, cards):
        self.cards.extend(cards)
        self.sendToClient("addCards", cards)

    def updatePoints(self, pointChange):
        self.points += pointChange
        self.sendToClient("pointChange", pointChange)

    def _getContract(self, contract_types):
        return self.sendToClient("selectcontract", contract_types)

    def selectContract(self, contract_types):
        self.contract = self._getContract(contract_types)
        self._sendToPublic("selectcontract", [self.uuid, self.contract])
        return self.contract

    def _getCard(self, requested_suit_card):
        return self.sendToClient("selectcard", Rules.allowedCards(requested_suit_card, self.cards))

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
            self._sendToPublic("trick", trick)
        self.sendToClient("trick", trick)
        self.tricks.append(trick)

    def sendToClient(self, message, data):
        if self.client != None:
            self.client.receiveMessage(message, data)

    def _sendToPublic(self,message, data):
        if self.game != None:
            self.game.sendToPlayers(self.uuid, message, data)

    def __repr__(self):
        return str({
            "name": self.name,
            "uuid" : self.uuid
        })
