# Name: Sunmi Kim
# Class: Object Oriented Programming with Python
# Title: Blackjack Phase 3 | blackjack.py - Business Tier
# Date: 06/14/2023

from blackjack_objects import Card, Deck, Hand

class Blackjack: 
    def __init__(self, startingBalance):
        self.startingBalance = startingBalance    
        self.money = startingBalance    

    def displayCards(self, hand, title):
        # Prints title, hand (cards), and the points of that hand
        print(title)
        for card in hand._Hand__cards:
            print(card.displayCard())
        print("Total points:", hand.points)

    def getBet(self, bet):
        while True:
            try:
                userInput = int(bet.get())
                if userInput < 0:
                    raise ValueError("Invalid amount. Enter a positive number")
                elif userInput > self.startingBalance:
                    raise ValueError(f"Bet should be less than or equal to {self.startingBalance}")
                else:
                    return userInput
            except ValueError as e:
                print(e)

    def setupRound(self):       
        # initialize self.deck to a new Deck object and shuffle it
        self.deck = Deck()
        self.deck.shuffle()
        # initialize self.dealerHand and self.playerHand to new Hand objects
        self.dealerHand = Hand(dealer=True)
        self.playerHand = Hand()
        # deal two cards to the playerHand, and one card to the dealerHand
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())
        # finally, print dealerHand and playerHand using displayCards method
        self.displayCards(self.dealerHand, "\nDealer's Show Card:")
        self.displayCards(self.playerHand, "\nYour Cards:")
        
    def takePlayerTurn(self):
        # Method to simulate player playing one turn by dealing a card to the player's hand.
        self.playerHand.addCard(self.deck.dealCard()) 
  
    def takeDealerTurn(self): # dealer must continue taking cards until total reaches 17
        while self.dealerHand.points < 17:
            self.dealerHand.addCard(self.deck.dealCard())
        return self.dealerHand.points
    
    def determineOutcome(self, bet):
        # Calculate the outcome of the game
        self.bet = self.money
        player_points = self.playerHand.points
        dealer_points = self.dealerHand.points
        result = ""

        if player_points == dealer_points:
            result = "Push! It's a tie."   
            balance = self.money         
        elif player_points > 21:
            result = "Player Busts! You lose."
            balance = self.money - int(bet.get()) 
        elif dealer_points > 21:
            result = "Yah! Dealer Busts! You win."
            balance = self.money + int(bet.get())
        elif player_points == 21 and len(self.playerHand._Hand__cards) == 2:
            result = "Blackjack! You win!"
            balance = self.money + (int(bet.get()) * 1.5)
        elif dealer_points == 21 and len(self.dealerHand._Hand__cards) == 2:
            result = "Dealer blackjack! You lose!"
            balance = self.money - int(bet.get()) 
        elif player_points > dealer_points:
            result = "You win!"
            balance = self.money + int(bet.get())
        elif player_points < dealer_points:
            result = "You lose."
            balance = self.money - int(bet.get())
        else:
            result = "Unanticipated result"
            balance = self.money
        return balance, result

# def main():
#     print("BLACKJACK!")
#     print("Blackjack payout is 3:2")

#     # initialize starting money
#     money = 100
#     print("Starting Balance:", money)

#     # instantiate object of Blackjack class 
#     blackjack = Blackjack(money)
    
#     print("Setting up a round...")
#     blackjack.getBet()
#     blackjack.setupRound()

#     print("\nPlaying Player Hand...")

#     while True:
#         # Prompt the user to whether to Hit (h) or Stand (s)
#         action = input("Do you want to Hit (h) or Stand (s)? ")
#         if action.lower() == "s":  # Stand
#             break
#         elif action.lower() == "h":  # Hit
#             blackjack.takePlayerTurn()
#             blackjack.displayCards(blackjack.playerHand, "\nYour Cards:")
#             if blackjack.playerHand.points > 21:
#                 print("Busted! Your points:", blackjack.playerHand.points)
#                 return
#         else:
#             print("Invalid input. Please enter 'h' or 's'.")

#     print("\nYour points:", blackjack.playerHand.points)
#     print("Good bye!")


# # if started as the main module, call the main function
# if __name__ == "__main__":
#     main()
