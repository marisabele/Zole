
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
    def selectCard(self, requested_suit_card):
        pass

    def __repr__(self):
        return str({
            "name": self.name,
            "uuid" : self.uuid
        })
