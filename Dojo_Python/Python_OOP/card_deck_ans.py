import random
from random import shuffle

class Deck(object):
    # make and hold onto 52 cards with a for loop
    def __init__(self):
        self.deck = []
        self.createDeck()

    def createDeck(self):
        suits = ['clubs', 'hearts', 'spades', 'diamonds']
        faceCards = {
            1:  'Ace',
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: 'Jack',
            12: 'Queen',
            13: 'King'
            }

        for suit in range (0, 4):
            for rank in range(1, 14):
                card = Card(suits[suit], faceCards[rank])
                self.deck.append(card)

    def shuffle(self):
        shuffle(self.deck)
        return self.deck

    def flip(self):
        return self.deck.pop()

    def reset(self):
        self.deck = []
        self.createDeck()

    def deal2Cards(self):
        dealtCards = []
        for count in range(0, 2):
            dealtCards.append(self.deck.pop())
        return dealtCards

    def deal(self):
        pass



class Card(object):
    def __init__(self, suit, value):
        self.suit =  suit
        self.value = value

    def __repr__(self):
        return "{} {}".format(self.value, self.suit)

my_deck = Deck()
# print my_deck.deck[50].suit
print my_deck.deck
# print my_deck.shuffle()
# print my_deck.flip()
# print len(my_deck.deck)
# my_deck.reset()
# print my_deck.deck
# print my_deck.deal2Cards()
