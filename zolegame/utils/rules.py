import copy

class Rules:
    #trumps ["cQ","sQ","hQ","dQ","cJ","sJ","hJ","dJ","dA","d10","dK","d9","d8","d7"]
    TRUMP_DECK = tuple(xrange(14))
    #clubs ["cA","c10","cK","c9"]
    CLUBS_DECK = tuple(xrange(14,18))
    #spades ["sA","s10","sK","s9"]
    SPADES_DECK = tuple(xrange(18,22))
    #hearts ["hA","h10","hK","h9"]
    HEARTS_DECK = tuple(xrange(22,26))

    ALL_DECK = tuple(xrange(26))
    CLUBS_FIRST  = TRUMP_DECK + CLUBS_DECK  + SPADES_DECK + HEARTS_DECK
    SPADES_FIRST = TRUMP_DECK + SPADES_DECK + CLUBS_DECK  + HEARTS_DECK
    HEARTS_FIRST = TRUMP_DECK + HEARTS_DECK + CLUBS_DECK  + SPADES_DECK

    #card points
    CARD_POINTS = [3,3,3,3,2,2,2,2,11,10,4,0,0,0,11,10,4,0,11,10,4,0,11,10,4,0]

    @classmethod
    def card_deck_ranking(self, cards):
        # Return the card ranking set from given set
        # first card is a asked suit

        if cards[0] in self.TRUMP_DECK:
            powerList = self.ALL_DECK
        if cards[0] in self.CLUBS_DECK:
            powerList = self.CLUBS_FIRST
        if cards[0] in self.SPADES_DECK:
            powerList = self.SPADES_FIRST
        if cards[0] in self.HEARTS_DECK:
            powerList = self.HEARTS_FIRST

        return [powerList.index(i) for i in cards]

    @classmethod
    def best_card(self, cards):
        #Return the strongest card from given set
        # assuming that first cards select requisted suit
        powers=self.card_deck_ranking(cards)
        return powers.index(min(powers))

    @classmethod
    def allowed_cards(self,required_card,my_deck):
        # Returns list of playable cards. If in hand does not have requested
        # suit card then return all hand.
        return_list=[]

        if required_card  in self.CLUBS_DECK:
            return_list= list(set(my_deck) & set(self.CLUBS_DECK))
        if required_card  in self.SPADES_DECK:
            return_list= list(set(my_deck) & set(self.SPADES_DECK))
        if required_card  in self.HEARTS_DECK:
            return_list= list(set(my_deck) & set(self.HEARTS_DECK))
        if required_card  in self.TRUMP_DECK:
            return_list= list(set(my_deck) & set(self.TRUMP_DECK))

        if len(return_list) == 0:
            return_list = my_deck
        return sorted(return_list)
