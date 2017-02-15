import random
from random import shuffle

class Cards():
    # need suit, value and color
    def __init__(self, rank=1, suits='clubs'):
        self.suits = ['clubs', 'hearts', 'spades', 'diamonds']
        self.rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        # self.rank = 'string'
        self.values = {
            1:  'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
            }

        self.card_deck = []

        for suit in self.suits:

            for value in self.rank:
                # card_deck = []
                this = str(value) + " " + suit
                self.card_deck.append(this)

        print self.card_deck


my_deck = Cards()

print my_deck.card_deck



# x = [[i] for i in range(10)]
# shuffle(x)
# print x

class Deck(Cards):
    # need to make and hold onto 52 cards
    def __init__(self):
        super(Deck, self).__init__()
        print "card deck exists"

    def shuffle(self):
        print 'shuffling deck'
        shuffle(self)




#     def reset():
#         print 'reseting deck'
#
#     def deal():
#         print 'dealing cards'
#
#     def flip():
#         print 'flipping over card'

# print shuffle(my_deck.card_deck)
