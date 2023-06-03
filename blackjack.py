# Name: Sunmi Kim
# Title: Blackjack Phase 2 | blackjack.py
# Date: 06/02/2023

from blackjack_objects import Card, Deck, Hand

class Blackjack:
    def __init__(self, startingBalance):
        self.startingBalance = startingBalance        

    def displayCards(self, hand, title):
        # Prints title, hand (cards), and the points of that hand
        print(title)
        for card in hand._Hand__cards:
            print(card.displayCard())
        print("Total points:", hand.points)

    def getBet(self):
        userInput = int(input("Place your bet amount: "))
        if userInput < 0:
            raise ValueError("Bet should be a positive amount")
        elif userInput > self.startingBalance:
            raise ValueError(f"Bet can be less than or equal to {self.startingBalance}")

    def getBet(self):
        while True:
            try:
                userInput = int(input("Place your bet amount: "))
                if userInput < 0:
                    raise ValueError("Invalid amount. Enter a positive number")
                elif userInput > self.startingBalance:
                    raise ValueError(f"Bet should be less than or equal to {self.startingBalance}")
                return userInput
            except ValueError as e:
                print(e)

    def setupRound(self):
        ''' Setup the round by doing these steps:
        - initialize self.deck to a new Deck object and shuffle it
        - initialize self.dealerHand and self.playerHand to new Hand objects
        - deal two cards to the playerHand, and one card to the dealerHand
        - finally, print dealerHand and playerHand using displayCards method
        '''
        self.deck = Deck()
        self.deck.shuffle()
        self.dealerHand = Hand(dealer=True)
        self.playerHand = Hand()
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())
        self.displayCards(self.dealerHand, "\nDealer's Show Card:")
        self.displayCards(self.playerHand, "\nYour Cards:")
        
    def takePlayerTurn(self):
        ''' Method to simulate player playing one turn by dealing a card
        to the player's hand.'''
        self.playerHand.addCard(self.deck.dealCard()) 


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    # initialize starting money
    money = 100
    print("Starting Balance:", money)

    # instantiate object of Blackjack class 
    blackjack = Blackjack(money)
    
    print("Setting up a round...")
    blackjack.getBet()
    blackjack.setupRound()

    print("\nPlaying Player Hand...")

    while True:
        action = input("Do you want to Hit (h) or Stand (s)? ")
        if action.lower() == "s":  # Stand
            break
        elif action.lower() == "h":  # Hit
            blackjack.takePlayerTurn()
            blackjack.displayCards(blackjack.playerHand, "\nYour Cards:")
            if blackjack.playerHand.points > 21:
                print("Busted! Your points:", blackjack.playerHand.points)
                return
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    print("\nYour points:", blackjack.playerHand.points)
    # Add code to play the player hand
    # Prompt the user to whether to Hit (h) or Stand (s)
    # If player says stand,
    #      print player's points and exit
    # else
    #    call takePlayerTurn method to deal a card to the player
    #    Check if the hand is busted, if so print player's points and exit
    #    otherwise prompt again   
    print("Good bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
