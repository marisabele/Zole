from zolegame.game import BaseGame
from zolegame.player import Player

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
        winner = 0;

        while (last_round == False):
            print "Start"
            game = BaseGame(self.room_type, self.bet_size)
            game.addPlayers(Player(0, "name_1",100, self.players[winner], game),
                            Player(1, "name_2",100, self.players[self.nextPlayer(winner)], game),
                            Player(2, "name_3",100, self.players[self.nextPlayer(winner+1)], game)
                            )
            game.play()
            last_round = True
