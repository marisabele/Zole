from rules import Rules

class Player:
    def __init__(self, uuid, name, points):
        self.name = name
        self.uuid = uuid
        self.points = points
        self.cards = []

    def addCards(self, cards):
        self.cards.extend(cards)

    def updatePoints(self, pointChange):
        self.points += pointChange

    def selectContract(self, contract_types):
        #send message to the player template
        #return contract_types[0]
        pass
    def onContract(self, uuid, contract):
        pass

    def _getCard(self, requested_suit_card):
        return None

    def selectCard(self, requested_suit_card):
        card = self._getCard(requested_suit_card)
        if card in Rules.allowedCards(requested_suit_card, self.cards):
            self.cards.remove(card)
            return card
        pass

    def __repr__(self):
        return str({
            "name": self.name,
            "uuid" : self.uuid
        })
