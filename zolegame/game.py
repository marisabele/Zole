import itertools
import random
from constansts import *
from rules import Rules

class BaseGame(object):

    def __init__(self, game_types, bet_size):
        self.game_types = game_types
        self.bet_size = bet_size
        self.players = []
        self.table_cards = []
        self.player_roles = [Contract.PARTNER,
                             Contract.PARTNER,
                             Contract.PARTNER]
        self.selected_game = None
        self.tricks = {}

    def addPlayers(self, playerA, playerB, playerC):
        self.players.append(playerA)
        self.players.append(playerB)
        self.players.append(playerC)

        for p in self.players:
            self.tricks[p.uuid] = []

    def play(self):
        self._dealCards()
        self.selectContract()

    def selectContract(self, contracts = None):
        # Ask for game type and deside what to do with table cards

        for p in self.players:
            contract = p.selectContract(self.game_types)
            if contract not in self.game_types:
                raise IndentationError
            p.onContract(p.uuid, contract)
            print ("Player %s selected game type: %s"%(p.uuid, self.game_types))

            if contract == Contract.TABLE:  #Start normal Solo game with table cards
                self.selected_game = Contract.TABLE

                #Add table cards to solo player
                table = self.table_cards
                p.addCards(table)

                #Ask solo player to place 2 cards
                self._playTrick([p.uuid])
                self._playTrick([p.uuid])
                break

            if contract == Contract.BIG:  #Start Solo game without table cards
                self.selected_game = Contract.BIG
                break

            if contract == Contract.SMALL: #Start Null game when solo palyer cannot winn a trick
                self.selected_game = Contract.SMALL
                break

        if  self.selected_game == None:  #Start to table game the looser is with moust tricks
            if Contract.DESK in self.game_types:
                self.selected_game = Contract.DESK
            else:
                self.selected_game = Contract.PARTNER


    def _playTrick(self,player_list):
        trick =[]
        first_card = None
        for pIndex in player_list:
            p = next(x for x in self.players if x.uuid == pIndex)
            card = p.selectCard(first_card)
            #card = p.selectCard(rules.allowCards(requiredCard, self.state.cards[pIndex]))  #ask for card
            #print ("%s Selected card: %s"%(p,card))
            #if card not in self.state.cards[pIndex]:            #check if card is allowed
            #    raise NotImplementedError

            trick.append(card)

            #self.state.cards[pIndex].remove(card)
            #on first hand update requested cards
            if first_card == None:
                first_card = card

        winner = player_list[Rules.bestCard(trick)]
        #print ("winner from : %s is a %d"%(trick,winner))

        #Add trick cards to player
        self.tricks[winner].append(trick)

        '''
        #For special game type check status
        if self.state.gameType == 's':
            winnP = next(x for x in self.players if x.index == winner)
            if 's' == winnP.gameRole:
                print ("Trick winner is a SMALL!!!")
                return winner, 1    #game over
        '''
        return winner, 0

    def _dealCards(self, card_deck = None):
        #mix up the deck
        if card_deck == None:
            card_deck = list(Cards.ALL)
            random.shuffle(card_deck)

        for p in self.players:
            cards = card_deck[:8]
            del card_deck[:8]
            p.addCards(cards)

        self.table_cards = card_deck       #remaining cards to the table
