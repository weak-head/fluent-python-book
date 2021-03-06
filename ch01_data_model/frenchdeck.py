#!/bin/python

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()
    suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def card_rank(card):
    '''
    Evaluates card rank based on card suite and value.
    '''

    rank_value = FrenchDeck.ranks.index(card.rank)
    total_rank = rank_value * len(FrenchDeck.suits) + FrenchDeck.suits_values[card.suit]

    return total_rank


if __name__ == '__main__':
    deck = FrenchDeck()

    # now we can do lots of good and interesting things
    # because we have implemented __len__ and __getitem__
    # and this allows us to work with FrenchDeck
    # as with standard Python sequence

    # we can get the size of the deck
    print(len(deck))

    # get card by position
    print(deck[1])
    print(deck[-1])

    # we can take advantage of the standard library
    for _ in range(4):
        print(choice(deck))

    # also we support slicing because
    # __getitem__ delegates the work to []
    print(deck[:3])
    print(deck[13:18])

    # the deck is also iterable in both directions
    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)

    # and even we dont have __contains__ method
    # 'in' operation can rely on sequential scan
    print( Card('Q', 'hearts') in deck )
    print( Card('7', 'stones') in deck )

    # and ordered by custom criteria
    for card in sorted(deck, key=card_rank):
        print(card)