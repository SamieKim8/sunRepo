# Name: Sunmi Kim
# Title: Blackjack Phase 2 | objects.py (Card, Deck, Hand classes)
# Date: 06/02/2023

import random

class Card: 
    SUIT_ORDER = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    RANK_ORDER = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    CARDS_CHARACTERS = {"Spades": "♠",
                        "Hearts": "♥", 
                        "Diamonds": "♦", 
                        "Clubs": "♣"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit 

# to define a custom comparison method for the Card class 
# that specifies how two Card objects should be compared. 
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # def __lt__(self, other): # This should be updated as below
    #     return self.rank < other.rank # Compare based on the numerical value of the ranks        
    def __lt__(self, other): 
        if self.suit != other.suit:
            return self.SUIT_ORDER.index(self.suit) > self.SUIT_ORDER.index(other.suit)
        else:
            return self.RANK_ORDER.index(self.rank) > self.RANK_ORDER.index(other.rank)

    @property # read-only public property that represents the value of the card.
    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':          
            return 11
        else:
            return int(self.rank)

    def displayCard(self): 
        return f"{self.rank} of {self.suit} {Card.CARDS_CHARACTERS[self.suit]}"

class Deck:
    def __init__(self):
        self.__deck = []  # 52 objects of Card class with one of each card type
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        
        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(rank, suit))
   
    def __len__(self):
        # returns the length of the __deck list
        return len(self.__deck)

    def shuffle(self):
        # shuffles the deck to a random order
        random.shuffle(self.__deck)

    def dealCard(self): # removes a card from the deck and returns it
        if len(self.__deck) == 0:
            return None
        else:
            return self.__deck.pop()

class Hand: # make the Hand class printable
    def __init__(self, dealer=False): # private attribute - a list of objects of Card class
        self.__cards = []
        self.dealer = dealer
  
    def __len__(self):
        # returns the length of the __hand list
        return len(self.__cards)
    
    @property # update points that value of an Ace can be either 1 or 11
    def points(self): 
        total_points = 0
        for card in self.__cards:
            total_points += card.value
            if total_points > 21 and card.value == 11:
                total_points -= 10
        return total_points
       
    def addCard(self, card):
        # one argument of Card class object and appends it to the __cards list
        self.__cards.append(card)

    def __str__(self): # To display the sorted cards by suit and rank
        sorted_cards = sorted(self.__cards, key=lambda card: (card.suit, card.rank))  
        hand_str = ""
        for card in sorted_cards:
            hand_str += card.displayCard() + "\n"
        return hand_str
    
    def shortDisplay(self):
        # returns a string with the rank and suit symbol of the sorted cards in the hand
        # such as 10♣ 3♦ Queen♥ Ace♠
        sorted_cards = sorted(self.__cards, key=lambda card: (card.suit, card.rank))
        return " ".join(card.rank + Card.CARDS_CHARACTERS[card.suit] for card in sorted_cards)
    
    @property
    def isBusted(self):
        return self.points > 21
        
    @property
    def hasBlackjack(self):
        return self.points == 21 and len(self.__cards) == 2
