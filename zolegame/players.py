class PlayerInterface(object):
    def newGame(self, uuid, name , points):
        # Start new game
        pass
    def addCards(self, cards):
        # Deal cards to the player
        pass
    def updatePoints(self, points):
        # Update points
        pass
    def selectContract(self, types):
        # Player must select a contract type
        raise NotImplementedError("Your client does not implement selectContract method")
    def contractSelected(self, uuid, game_type):
        # player selected contract type
        pass
    def selectCard(self, cards):
        # Player must select card to play
        raise NotImplementedError("Your client does not implement selectCard method")
    def cardPlaced(self, uuid, card):
        # player placed card on table
        pass
    def trickEnd(self, winner, trick_cards):
        # Announce trick winner
        pass
    def __init__(self):
        pass
    def receiveMessage(self, message, data):
        # Called from game server
        response = []
        if message == "init":
            self.newGame(data[0], data[1], data[2])
            return None
        if message == "addCards":
            self.addCards(data)
            return None
        if message == "updatePoints":
            self.updatePoints(data)
            return None
        if message == "selectContract":
            return self.selectContract(data)
        if message == "contractSelected":
            self.contractSelected(data[0], data[1])
            return None
        if message == "selectCard":
            return self.selectCard(data)
        if message == "cardPlaced":
            return self.cardPlaced(data[0], data[1])
        if message == "trick":
            self.trickEnd(data[0], data[1])
            return None
