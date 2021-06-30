import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        # print([Card(rank, suit) for suit in self.suits for rank in self.ranks])
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]
def spades_high(Card):
    rank_value = FrenchDeck.ranks.index(Card.rank)
    return rank_value*len(set_values)+set_values[Card.suit]


if __name__ == '__main__':
    # been_card = Card('7', 'diamonds')
    # print(been_card.suit)
    # print(been_card)
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[0])
    # print(deck[-1])
    # print(choice(deck))
    # print(deck[4:])
    # print(deck[12::13])
    # for i in reversed(deck):
    #     print(i)
    set_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    for card in sorted(deck, key=spades_high, reverse=False):
        print(card)
