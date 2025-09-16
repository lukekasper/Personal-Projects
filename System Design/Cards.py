from abc import ABC, abstractmethod
from enum import Enum
import sys
import random


class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    CLUB = 2
    SPADES = 3


class Card(ABC):
    def __init__(self, value, suit):
        self._base_value = value
        self.suit = suit

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
        return self._base_value == 1

    def is_face_card(self):
        return 10 < self._base_value <= 13

    @property
    def value(self):
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self._base_value

    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 13:
            self._base_value = new_value
        else:
            raise ValueError(f'Invalid card value: {new_value}')

    def __str__(self):
        return f"{self.value} of {self.suit.name}"


class Hand:
    def __init__(self, cards=None):
        self.cards = cards if cards else []

    def add_card(self, card):
        self.cards.append(card)

    @abstractmethod
    def score(self):
        pass


class BlackJackHand(Hand):
    BLACKJACK = 21

    def __init__(self, cards=None):
        super().__init__(cards)

    def score(self):
        if not self.cards:
            return 0

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
        self.deal_index += 1
        return card

    def shuffle(self):
        random.shuffle(self.cards)
        self.deal_index = 0


class BlackJackGame:
    def __init__(self):
        self.deck = self._create_deck()
        self.deck.shuffle()
        self.player_hand = BlackJackHand()
        self.dealer_hand = BlackJackHand()

    def _create_deck(self):
        cards = []
        for suit in Suit:
            for value in range(1, 14):
                cards.append(BlackJackCard(value, suit))
        return Deck(cards)

    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())

    def show_hands(self):
        print("Player's Hand:")
        for card in self.player_hand.cards:
            print(card)
        print(f"Score: {self.player_hand.score()}\n")

        print("Dealer's Hand:")
        for card in self.dealer_hand.cards:
            print(card)
        print(f"Score: {self.dealer_hand.score()}\n")

    def play(self):
        self.deal_initial_cards()
        self.show_hands()
        # Extend with hit/stand logic, dealer rules, win/loss resolution


if __name__ == "__main__":
    game = BlackJackGame()
    game.play()
