import game
import player

class Room(object):

    def __init__(self, room_type, bet_size):
        # init new room with room_type contracts
        self.room_type = room_type
        self.bet_size = bet_size
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def nextPlayer(self, firstIndex):
        seq=[0,1,2,0,1,2]
        return seq[firstIndex+1]

    def play(self):
        last_round = False
        firstPlayer = 0;

        while (last_round == False):
            game = BaseGame(self.room_type, self.bet_size)
            game.addPlayers(self.players[winner],
                            self.players[self.nextPlayer(winner)],
                            self.players[self.nextPlayer(winner+1)])
            game.play()
            last_round = True
