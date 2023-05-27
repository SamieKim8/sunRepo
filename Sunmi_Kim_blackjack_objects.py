# Name: Sunmi Kim
# Date: 05/24/2023
# Title: BlackJack classes - Card, Deck, Hand and cards dictionary

import random

class Card: # Blackjack card class
    CARDS_CHARACTERS = {"Spades": "♠",
                        "Hearts": "♥", 
                        "Diamonds": "♦", 
                        "Clubs": "♣"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit 
        
    @property # read-only public property that represents the value of the card.
    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':          
            return 11
        else:
            return int(self.rank)

    def displayCard(self): # method
        return self.rank + " of " + self.suit + " " + Card.CARDS_CHARACTERS[self.suit]

class Deck:
    def __init__(self):
        self.__deck = []  # 52 objects of Card class with one of each card type
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        
        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(rank, suit))

    @property
    def count(self):
        # equal to the count of cards in the __deck list
        return len(self.__deck)

    def shuffle(self):
        import random # shuffles the deck to a random order
        random.shuffle(self.__deck)

    def dealCard(self): # removes a card from the deck and returns it
        if self.count == 0:
            return None
        else:
            return self.__deck.pop()

class Hand:
    def __init__(self): # private attribute which is a list of objects of Card class
        self.__cards = []

    @property # equal to the count of cards in the __cards list
    def count(self):
        return len(self.__cards)

    @property
    def points(self): # equal to the total points of the cards in the hand
        total_points = 0
        for card in self.__cards:
            total_points += card.value
        return total_points
    
    def addCard(self, card):
        # takes one argument of Card class object and appends it to the __cards list
        self.__cards.append(card)

    def displayHand(self):
        # prints the hand by printing the strings returned by 
        # displayCard method of each of the cards in the __cards list
        for card in self.__cards:
            print(card.displayCard())

