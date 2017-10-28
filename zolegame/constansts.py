

class Cards:
    #trumps ["cQ","sQ","hQ","dQ","cJ","sJ","hJ","dJ","dA","d10","dK","d9","d8","d7"]
    TRUMPS = tuple(xrange(14))
    #clubs ["cA","c10","cK","c9"]
    CLUBS = tuple(xrange(14,18))
    #spades ["sA","s10","sK","s9"]
    SPADES = tuple(xrange(18,22))
    #hearts ["hA","h10","hK","h9"]
    HEARTS = tuple(xrange(22,26))

    ALL = list(xrange(26))

    CLUBS_FIRST  = TRUMPS + CLUBS  + SPADES + HEARTS
    SPADES_FIRST = TRUMPS + SPADES + CLUBS  + HEARTS
    HEARTS_FIRST = TRUMPS + HEARTS + CLUBS  + SPADES

    #card points
    POINTS = [3, 3, 3, 3, 2, 2, 2, 2, 11, 10, 4, 0, 0, 0,
              11, 10, 4, 0,
              11, 10, 4, 0,
              11, 10, 4, 0]

class Contract:
    TABLE = 't'     #player pick table cards and play one against two
    BIG = 'b'       #player play against two without table cards
    SMALL = 's'     #small cannot winn any trick
    PARTNER = 'p'   # player play with partner
    DESK = 'd'      # desk game winner is a player with less trick or less points
