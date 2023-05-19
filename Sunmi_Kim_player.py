# Title: Player Inheritance
# Date: 05/11/2023
# Student: Sunmi Kim
# Description: Superclass, Subclass, Inheritance, and Polymorphism 

class Player: # Superclass or parent class 
    def __init__(self, name, position):
            self.__name = name
            self.__position = position
            if len(name) == 0: 
                raise ValueError("name cannot be empty.")
            elif len(position) == 0:
                raise ValueError("position cannot be empty.")

    # Two public properties        
    @property
    def name(self):
        return self.__name
    
    @property
    def position(self):
        return self.__position

    # Superclass method for Polymorphism
    def getStats(self):
        return f"Player Name: {self.name} Position: {self.position}"

class Pitcher(Player): # Subclass 1 (child class 1)
    def __init__(self, name, wins, loss): # position removed here and below constructor
        super().__init__(name, "Pitcher") # call superclass constructor making position fixed.
        if wins < 0:
            raise ValueError("wins cannot be negative.")
        if loss < 0:
            raise ValueError("loss cannot be negative.")
        self.wins = wins
        self.loss = loss

    def getStats(self): # Subclass method 1 for Polymorphism
        return f"Player Name: {self.name} Position: {self.position} Stats: {self.wins}-{self.loss} win-loss"
   
class Batter(Player): # Subclass 2 (child class 2)
    def __init__(self, name, position, at_bats, hits):
        Player.__init__(self, name, position)
        self.at_bats = at_bats
        self.hits = hits     
        if at_bats < 0:
            raise ValueError("ba_Bats cannot be negative.")
        elif hits < 0:
            raise ValueError("hits cannot be negative.")
        
    @property
    def average(self):
        average = round((self.hits / self.at_bats), 3)
        return average

    def getStats(self): # Subclass method 2 for Polymorphism
        return f"Player Name: {self.name} Position: {self.position} Stats: Batting Avg: {self.average}"             
