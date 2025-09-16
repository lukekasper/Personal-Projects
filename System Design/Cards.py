from abc import ABC, abstractmethod
from enum import Enum
import sys
import random


class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3


class Card(ABC):
    def __init__(self, value, suit):
        self._value = value
        self.suit = suit
        self.is_available = True

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, other):
        pass


class BlackJackCard(Card):
    def __init__(self, value, suit):
        super().__init__(value, suit)

    def is_ace(self):
        return self._value == 1

    def is_face_card(self):
        return 10 < self._value <= 13  # Jack, Queen, King

    @property
    def value(self):
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self._value

    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 13:
            self._value = new_value
        else:
            raise ValueError(f'Invalid card value: {new_value}')


class Hand:
    def __init__(self, cards=None):
        self.cards = cards if cards else []

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        return sum(card.value for card in self.cards)


class BlackJackHand(Hand):
    BLACKJACK = 21

    def __init__(self, cards=None):
        super().__init__(cards)

    def score(self):
        min_over = sys.maxsize
        max_under = -sys.maxsize
        for score in self.possible_scores():
            if self.BLACKJACK < score < min_over:
                min_over = score
            elif max_under < score <= self.BLACKJACK:
                max_under = score
        return max_under if max_under != -sys.maxsize else min_over

    def possible_scores(self):
        scores = [0]
        for card in self.cards:
            if isinstance(card, BlackJackCard) and card.is_ace():
                scores = [x + y for x in scores for y in (1, 11)]
            else:
                scores = [x + card.value for x in scores]
        return list(set(scores))


class Deck:
    def __init__(self, cards=None):
        self.cards = cards if cards else []
        self.deal_index = 0

    def remaining_cards(self):
        return len(self.cards) - self.deal_index

    def deal_card(self):
        if self.deal_index >= len(self.cards):
            return None
        card = self.cards[self.deal_index]
        card.is_available = False
        self.deal_index += 1
        return card

    def shuffle(self):
        random.shuffle(self.cards)
        self.deal_index = 0
        for card in self.cards:
            card.is_available = True
