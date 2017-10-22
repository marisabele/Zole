class BasePlayer(object):
    def __init__(self):
        pass

    def newGame(self, players, contract_types, bet_size):
        # Start new game
        pass

    def add_cards(self, cards):
        # Deal cards to the player
        pass

    def select_contract(self, types):
        # Player must select a contract type
        raise NotImplemented

    def contract_selected(self, game_type):
        pass

    def select_card(self, card_on_table):
        # Player must select card to play
        raise NotImplemented

    def update_cards_on_table(self, cards_on_table):
        pass

    def trick_end(self, winner, trick_cards):
        pass

    def game_end(self, winner):
        pass

    def receive_message(self, message):
        # Called from game server
        message_type = message["message_type"]
        response = []
        if message_type == "create":
            self.newGame(message["users"], message["type"], message["bet"])
            return response
        if message_type == "start":
            self.add_cards(message["cards"])
            return response
        if message_type == "choose":
            return self.select_contract(message["types"])
        if message_type == "contract_selected":
            self.contract_selected(message["type"])
            return response
        if message_type == "addcards":
            self.add_cards(message["cards"])
            return response
        if message_type == "selectcard":
            return self.select_card(message["table"])
        if message_type == "trick":
            self.trick_end(message["trick"])
            return response
        if message_type == "gameend":
            self.trick_end(message["winner"])
            return response
