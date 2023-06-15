# Name: Sunmi Kim
# Class: Object Oriented Programming with Python
# Title: Blackjack Phase 3 | gui_blackjack.py - Presentation Tier
# Date: 06/14/2023

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from blackjack import Blackjack
from blackjack_objects import Card, Hand, Deck 

STARTING_BALANCE = 100

class BlackjackFrame(ttk.Frame): # child class of ttk.Frame (super class)
    def __init__(self, parent): # Constructor
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent

        # Define string variables for text entry fields
        self.money = tk.StringVar()
        self.bet = tk.StringVar()
        self.dealerCards = tk.StringVar()
        self.dealerPoints = tk.StringVar()
        self.playerCards = tk.StringVar()
        self.playerPoints = tk.StringVar()
        self.result = tk.StringVar()

        # Initialize game variables
        self.game = Blackjack(STARTING_BALANCE)
        self.gameOver = True

        # Initialize components
        self.initComponents()

        # Display current money amount
        self.money.set("$"+str(self.game.money))

        #Initialize bet to 0
        self.bet.set("0")

    def initComponents(self):
        self.pack()
        
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Money:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.money,
                  state="readonly").grid(
            column=1, row=0, sticky=tk.W)

        ttk.Label(self, text="Bet:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.bet).grid(
            column=1, row=1, sticky=tk.W)

        ttk.Label(self, text="DEALER").grid(
            column=0, row=2, sticky=tk.E)
        
        ttk.Label(self, text="Cards:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.dealerCards,
                  state="readonly").grid(
            column=1, row=3, sticky=tk.W)

        ttk.Label(self, text="Points:").grid(
            column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.dealerPoints,
                  state="readonly").grid(
            column=1, row=4, sticky=tk.W)

        ttk.Label(self, text="YOU").grid(
            column=0, row=5, sticky=tk.E)
        
        ttk.Label(self, text="Cards:").grid(
            column=0, row=6, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.playerCards,
                  state="readonly").grid(
            column=1, row=6, sticky=tk.W)

        ttk.Label(self, text="Points:").grid(
            column=0, row=7, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.playerPoints,
                  state="readonly").grid(
            column=1, row=7, sticky=tk.W)

        self.makeButtons1()

        ttk.Label(self, text="RESULT:").grid(
            column=0, row=9, sticky=tk.E)
        ttk.Entry(self, width=50, textvariable=self.result,
                  state="readonly").grid(
            column=1, row=9, sticky=tk.W)

        self.makeButtons2()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons1(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=1, row=8, sticky=tk.W)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Hit", command=self.hit) \
            .grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Stand", command=self.stand) \
            .grid(column=1, row=0)

    def makeButtons2(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=1, row=10, sticky=tk.W)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Play", command=self.play) \
            .grid(column=0, row=0)
        ttk.Button(buttonFrame, text="Exit", command=self.exit) \
            .grid(column=1, row=0)
        
    # Method to update the dealer hand and the dealer points in the GUI
    def displayDealer(self):
        if self.game.dealerHand != None:
            cards = self.game.dealerHand.shortDisplay()
            self.dealerCards.set(cards)
            self.dealerPoints.set(str(self.game.dealerHand.points))         

    # Method to update the player hand and the dealer points in the GUI
    def displayPlayer(self):
        if self.game.playerHand != None:
            cards = self.game.playerHand.shortDisplay()
            self.playerCards.set(cards)
            self.playerPoints.set(str(self.game.playerHand.points))   

    def displayResult(self):
        # Calls determineOutcome to decide what the outcome of the game is.
        outcome = self.game.determineOutcome(self.bet)
        # Updates the result and the money
        balance = outcome[0]
        result = outcome[1]
        self.money.set("$" + str(balance))
        self.result.set(result)
 
    def playerCanPlayTurn(self):
        # This confirms that the game is underway
        if not self.gameOver: # player can play a turn
            self.result.set("")
            return True
        else: # this game is not underway, update the result and returns False
            self.result.set("Game is not underway")
            return False

    def hit(self):
        # confirms that user can play a turn, if not returns
        if not self.playerCanPlayTurn():
            return
        # else calls the takePlayerTurn() and 
        self.game.takePlayerTurn()
        # reports the player state by calling displayPlayer
        self.displayPlayer()

        # check if player is busted if so ends the game and updates the result by calling displayResult
        if self.game.playerHand.points > 21:
            self.gameOver = True
            self.displayResult()

    def stand(self):
        # confirms that user can play a turn if not returns
        if not self.playerCanPlayTurn():
            return
        # else, ends the game
        self.gameOver = True

        if self.game.playerHand.points != 21:
            self.game.takeDealerTurn() # has the dealer play his turn
            self.displayDealer() # reports the dealer state by calling displayDealer()

        self.displayResult() # Finally, updates the result by calling displayResult()
            
    def play(self): # Method to start a new game
        if not self.gameOver: # checks that the game is not already underway and return
            self.result.set("Game already in progress!")
            return
        
        # 1) read the bet amount 2) verify that it is valid
        bet_amount = int(self.bet.get())
        if bet_amount <= 0 or bet_amount > self.game.startingBalance:
            messagebox.showerror("Invalid Bet Amount", "Invalid bet amount!")
            return

        self.gameOver = False
        self.game.betAmount = bet_amount
        self.game.setupRound()
        self.displayPlayer()
        self.displayDealer()

        self.game.determineOutcome(self.bet)  # Pass the bet to determineOutcome

        # Before returning, checks if either player has a blackjack, if so ends the game
        if self.game.playerHand.points == 21 or self.game.dealerHand.points == 21:
            self.gameOver = True
            self.displayResult()

    def exit(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blackjack")
    BlackjackFrame(root)
    root.mainloop()
