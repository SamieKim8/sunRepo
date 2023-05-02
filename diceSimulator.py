# Date: 05/02/2023
# Author: Sunmi Kim
# Description: Dice Simulator Program

from diceObject import Dice
from colorama import Fore

def display_title(): 
    print(Fore.RED + "=" * 40)
    print(Fore.GREEN + "====== Welcome to the Dice Roller ======")
    print(Fore.BLUE + "=" * 40)
    print()

def main():
    display_title() # display title function
    start = "y"
    while start.lower() == "y":
        dice = Dice(sides=6)
        dice.roll_dice()

        start = input("Roll again? (y/n): ")
        print()
    print("Have a nice day!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
