'''
Card and dech mechanics
'''
from uuid import uuid4
from random import choice, randint, shuffle


# Card types
BASIC = 'basic'
ITEM = 'item'
CREATURE = 'creature'
ROOM = 'room'
EVENT = 'event'
CHARACTER = 'character'


class Card:
    flavour_text = ''
    card_type = BASIC
    deck_id = None


class Deck:
    '''An ordered deck of cards'''
    def __init__(self, cards, deck_id=None, shuffle_on_init=True):
        self._cards = cards
        self._discarded = []
        self._removed = []

        if deck_id is None:
            deck_id = str(uuid4())

        self._id = deck_id

        # Assign the cards to this deck
        for card in self._cards:
            card.deck_id = self._id

        if shuffle_on_init:
            # Shuffle the initial order of the deck
            self.shuffle()

    def shuffle(self):
        '''Shuffle this deck'''
        shuffle(self._cards)

    def draw(self, n=1):
        '''Draw n cards from the deck'''
        return [self._cards.pop(0) for _ in range(n)]

    def random_draw(self, n=1):
        '''Make a random selection from the deck'''
        drawn = []
        for k in range(n):
            card = choice(self._cards)
            self._cards.remove(card)
            drawn.append(card)

        return drawn

    def insert(self, card, index=None):
        '''Insert a card into the deck'''
        if index is None:
            index = randint(0, len(self._cards))

        card.deck_id = self._id

        self._cards.insert(index, card)

    def insert_last(self, card):
        '''Add a card to the end of the deck'''
        self.insert(card, len(self._cards)+1)

    def insert_first(self, card):
        self.insert(card, 0)
