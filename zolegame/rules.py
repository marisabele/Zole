import copy
from constansts import *

class Rules:

    @classmethod
    def cardDeckRanking(self, cards):
        # Return the card ranking set from given set
        # first card is a asked suit

        if cards[0] in Cards.TRUMPS:
            powerList = Cards.ALL
        if cards[0] in Cards.CLUBS:
            powerList = Cards.CLUBS_FIRST
        if cards[0] in Cards.SPADES:
            powerList = Cards.SPADES_FIRST
        if cards[0] in Cards.HEARTS:
            powerList = Cards.HEARTS_FIRST

        return [powerList.index(i) for i in cards]

    @classmethod
    def bestCard(self, cards):
        #Return the strongest card from given set
        # assuming that first cards select requisted suit
        powers=self.cardDeckRanking(cards)
        return powers.index(min(powers))

    @classmethod
    def allowedCards(self,required_card,my_deck):
        # Returns list of playable cards. If in hand does not have requested
        # suit card then return all hand.
        return_list=[]

        if required_card  in Cards.CLUBS:
            return_list= list(set(my_deck) & set(Cards.CLUBS))
        if required_card  in Cards.SPADES:
            return_list= list(set(my_deck) & set(Cards.SPADES))
        if required_card  in Cards.HEARTS:
            return_list= list(set(my_deck) & set(Cards.HEARTS))
        if required_card  in Cards.TRUMPS:
            return_list= list(set(my_deck) & set(Cards.TRUMPS))

        if len(return_list) == 0:
            return_list = my_deck
        return sorted(return_list)
