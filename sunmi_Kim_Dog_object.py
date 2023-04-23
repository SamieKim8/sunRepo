# Date: 04/22/2023
# Author: Sunmi Kim
# Title: Dog class and its client
# Description: Program to interact with a dog

from colorama import Fore
weights = [15.0]

class Dog:
    def __init__(self, name, color, weight=10.0, isHungry=True): # constructor
        self.name = name
        self.color = color
        self.weight = weight
        self.isHungry = isHungry

    def bark(self): # Dog's 1st behavior
        print(Fore.CYAN + f"{self.name} : Woof Woof")

    def eat(self): # Dog's 2nd behavior
        self.weight = weights[-1]
        self.weight += 0.1 # gms
        print(Fore.YELLOW + f"{self.name} : Chomp Chomp")
        weights.append(self.weight)
        #print(weights) for debugging purpose
        self.isHungry = False

    def walk(self): # Dog's 3rd behavior
        #print("before walk:",weights) #for debugging purpose
        self.weight = weights[-1]
        if self.weight <= 15:
            self.isHungry == True
            self.bark()
        else: # self.weight > 15.0:
            self.isHungry == False
            self.weight -= 0.1 # gms
            print(Fore.BLUE + f"{self.name} : Step Step")
            weights.append(self.weight)
            #print("after walk:",weights)

    def printStatus(self): # Print status
        self.weight = weights[-1]
        if self.weight > 15.0:
            self.isHungry == False
            print(Fore.GREEN + f"{self.name} is {self.color} in color weighs {self.weight} kg and is not hungry.")
        else: 
            self.isHungry == True
            print(Fore.GREEN + f"{self.name} is {self.color} in color weighs {self.weight} kg and is hungry.")


