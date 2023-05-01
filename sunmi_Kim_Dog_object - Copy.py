# Date: 04/30/2023
# Author: Sunmi Kim
# Title: Dog class and its client
# Description: Program to interact with a dog

from colorama import Fore

class Dog:
    def __init__(self, name, color, weight=10): # parameters / constructor # 10.0 kg
        self.name = name # initializing... with below
        self.color = color
        self.weight = weight
        self.isHungry = True # initializes isHungry to True

    def bark(self): # Dog's 1st behavior
        print(Fore.CYAN + f"{self.name} : Woof Woof")

    def eat(self): # Dog's 2nd behavior 
        if self.isHungry == False:
            print(Fore.GREEN + f"{self.name} is not hungry right now.")
        else: 
            print(Fore.YELLOW + f"{self.name} : Chomp Chomp")
            self.isHungry = False
            self.weight += 0.1 # gms   
            return self.isHungry

    def walk(self): # Dog's 3rd behavior
        if self.isHungry == True:
            self.bark()
        else: # self.isHungry == False:
            self.weight -= 0.1 # gms
            self.isHungry = True # after walking, isHungry is True
            print(Fore.BLUE + f"{self.name} : Step Step")

    def printStatus(self): # Print status
        if self.isHungry == False:
            print(Fore.GREEN + f"{self.name} is {self.color} in color weighs {self.weight} kg and is not hungry.")
        else: #self.isHungry == True
            print(Fore.GREEN + f"{self.name} is {self.color} in color weighs {self.weight} kg and is hungry.")
