from abc import ABC, abstractmethod
from enum import Enum
import random


class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    SPADE = 2
    CLUB = 3


class Card(ABC):

    def __init__(self, value, suit):
        self.suit = suit
        self._base_value = value


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


    def _is_ace(self):
        return self._base_value == 1
    

    def __is_face_card(self):
        return 10 < self._base_value <= 13


    @property
    def value(self):
        if self._is_ace:
            return 1
        elif self.__is_face_card:
            return 10
        else:
            return self._base_value
        
    
    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 14:
            self._base_value = new_value
        else:
            raise ValueError(f'{new_value} is not a valid value.')
        

    def __str__(self):
        name_map = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        display = name_map.get(self._base_value, str(self._base_value))
        return f"{display} of {self.suit.name.capitalize()}"
        
    
class Hand(ABC):
    
    def __init__(self, cards=None):
        self.cards = cards if cards else []


    def add_card(self, card):
        self.cards.append(card)


    @abstractmethod
    def total_score(self):
        pass
    

class BlackJackHand(Hand):

    BLACKJACK = 21
    
    def __init__(self, cards=None):
        super().__init__(cards)


    def total_score(self):
        if not self.cards:
            return 0
        
        max_val = 0
        min_val = float('inf')

        for score in self._possible_scores():
            if score > self.BLACKJACK:
                min_val = min(min_val, score)
            else:
                max_val = max(max_val, score)
        
        return max_val if max_val != 0 else int(min_val)


    def _possible_scores(self):
        scores = [0]

        for card in self.cards:

            if card.isInstance(card, BlackJackCard) and card._is_ace():
                scores = [x + y for x in scores for y in (1, 11)]
            else:
                scores = [x + card.value for x in scores]

        return list(set(scores))
    

class Deck(object):

    def __init__(self, cards):
        self.cards = cards
        self.index = 0


    def deal_card(self):
        if self.index >= len(self.cards):
            print("No more cards to deal, shuffling deck.")
            self.shuffle()
            self.deal_card()

        card = self.cards[self.index]
        self.index += 1
        return card

    
    def shuffle(self):
        random.shuffle(self.cards)
        self.index = 0

                
class BlackJackGame(object):

    def __init__(self):
        self.deck = self._create_deck()
        self.player_hand = BlackJackHand()
        self.dealer_hand = BlackJackHand()


    def _create_deck(self):
        cards = []
        for suit in Suit:
            for value in range(1, 14):
                cards.append(BlackJackCard(value, suit))

        return Deck(cards)
    

    def deal_hands(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card)
            self.dealer_hand.add_card(self.deck.deal_card)

    
    def show_hands(self):
        print("Player's Hand:")
        for card in self.player_hand.cards:
            print(card)
        print(f"Score: {self.player_hand.total_score()}\n")

        print("Dealer's Hand:")
        for card in self.dealer_hand.cards:
            print(card)
        print(f"Score: {self.dealer_hand.total_score()}\n")


    def play(self):
        self.deal_initial_cards()
    
        # Player turn
        while True:
            self.show_hands()
            if self.player_hand.score() > BlackJackHand.BLACKJACK:
                print("Player busts! Dealer wins.\n")
                return
            move = input("Hit or Stand? (h/s): ").strip().lower()
            if move == 'h':
                self.player_hand.add_card(self.deck.deal_card())
            elif move == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
    
        # Dealer turn
        print("\nDealer's turn...")
        while self.dealer_hand.score() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
    
        self.show_hands()
    
        # Win/loss resolution
        player_score = self.player_hand.score()
        dealer_score = self.dealer_hand.score()
    
        if dealer_score > BlackJackHand.BLACKJACK:
            print("Dealer busts! Player wins.\n")
        elif player_score > dealer_score:
            print("Player wins!\n")
        elif player_score < dealer_score:
            print("Dealer wins!\n")
        else:
            print("It's a tie!\n")


if __name__ == "__main__":
    game = BlackJackGame()
    game.play()
