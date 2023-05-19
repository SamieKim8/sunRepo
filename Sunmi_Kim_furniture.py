# Title: Furniture Inheritance
# Date: 05/18/2023
# Student: Sunmi Kim
# Description: Built-in Object class methods, Superclass, Subclass, Inheritance, and Polymorphism 

class Furniture: # superclass
    def __init__(self, weight): # constructor
            self.__weight = weight
            if weight <= 0:
                raise ValueError("Weight must be positive")

    # public properties        
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, newWeight): # check for valueError
        if newWeight <= 0:
            raise ValueError("Weight must be positive")
        else:
            self.__weight = newWeight
          
    # making the Furniture class comparable based on weight property          
    def __eq__(self, other): 
        return self.weight == other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __str__(self): # Object built-in method
        return "Item Weight: " + str(self.weight) + " lbs"

class Table(Furniture): # Subclass 1
    def __init__(self, weight, wood):
        super().__init__(weight)  # call superclass constructor
        if not isinstance(wood, str): # if wood argument is not a string
            raise TypeError("wood must be a string")
        self.wood = wood # Subclass specific attribute

    def __str__(self): # Subclass method 1 for Polymorphism
        return "Table Item Weight: " + str(self.weight) + " lbs Made of: " + str(self.wood)

class Bed(Furniture): # Subclass 2 
    def __init__(self, weight, size):
        Furniture.__init__(self, weight) # call superclass constructor
        self.size = size
        if size not in ["Twin", "Full", "Queen", "King"]:
            raise ValueError("Invalid bed size")
        
    def __str__(self): # Subclass method 2 for Polymorphism
        return "Bed Item Weight: " + str(self.weight) + " lbs Size: " + str(self.size)
    
class FurnitureGallery:
    def __init__(self): # constructor with no arguments
        # private attribute / a list of Furniture class and derived classes objects
        self.__furnList = [] # initializing __furnList

    def addFurniture(self, furniture):
        if not isinstance(furniture, Furniture):
            raise TypeError("furniture argument must be an instance of Furniture or one of its derived classes")
        self.__furnList.append(furniture)

    def sort(self): # sorts the __furnList based on weight
        self.__furnList.sort(key=lambda x: x.weight)
    
    # making this class iterable to iterate the objects in the list
    def __iter__(self): 
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index >= len(self.__furnList):
            raise StopIteration
        
        item = self.__furnList[self.__index]
        self.__index += 1
        return item
