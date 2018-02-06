# coding: utf-8
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # 生成纸牌对象
    card = Card('10', 'clubs')
    print(card)
    print()
    # 生成一副纸牌
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(deck[:3])
    print(deck[12::13])
    print(list(reversed(deck))[0])
    print()
    # 随机取出纸牌
    from random import choice
    print(choice(deck))
    print(choice(deck))
    print()
    # 排序
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    print(sorted(deck, key=spades_high)[0])
    # 洗牌
    from random import shuffle

    def set_card(deck, position, card):
        deck._cards[position] = card
    FrenchDeck.__setitem__ = set_card
    shuffle(deck)
    print(deck[:3])
