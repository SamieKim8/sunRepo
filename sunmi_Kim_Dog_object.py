# Date: 04/30/2023
# Author: Sunmi Kim
# Title: Dog class and its client
# Description: Program to interact with a dog
# After dog1 eat, the weight increased 0.1 and shouldn't be hungry in printStatus. Please update accordingly. 

from colorama import Fore

class Dog:
    def __init__(self, name, color, weight=10000, isHungry=True): # constructor # 10.0 kg
        self.name = name
        self.color = color
        self.weight = weight
        self.isHungry = isHungry

    def bark(self): # Dog's 1st behavior
        print(Fore.CYAN + f"{self.name} : Woof Woof")

    def eat(self): # Dog's 2nd behavior 
        print(Fore.YELLOW + f"{self.name} : Chomp Chomp")
        self.isHungry = False
        self.weight += 100 # gms   
        return self.isHungry

    def walk(self): # Dog's 3rd behavior
        if self.isHungry == True:
            self.bark()
        else: # self.isHungry == False:
            self.weight -= 100 # gms
            self.isHungry = True # after walking, isHungry is True
            print(Fore.BLUE + f"{self.name} : Step Step")

    def printStatus(self): # Print status
        if self.isHungry == False:
            print(Fore.GREEN + f"{self.name} is {self.color} in color weighs {self.weight/1000:.1f} kg and is not hungry.")
        else: #self.isHungry == True
            print(Fore.GREEN + f"{self.name} is {self.color} in color weighs {self.weight/1000:.1f} kg and is hungry.")


