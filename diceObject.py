import random
from colorama import Fore

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        
    def get_positive_count(self): # user enters preferred number to roll a dice
        while True:
            try:
                preferred_number = int(input(Fore.WHITE + "Enter your preferred number to roll a dice: "))
                if preferred_number <= 0:
                    raise ValueError(Fore.RED + "Please enter a positive integer.")
                return preferred_number
            except ValueError as e: 
                print(e)

    def roll(self): # to simulate rolling of a single dice
        dice_numbers = []
        max = self.sides
        preferred_number = self.get_positive_count()
        for i in range(preferred_number): # dice numbers appear preferred_number times
            dice_number = random.randint(1, max)
            print(Fore.WHITE + f"Dice number for roll {i+1}: {dice_number}")
            dice_numbers.append(dice_number) # each dice number will be appended to dice_numbers list
        return dice_numbers

    def roll_dice(self):
        dice_numbers = self.roll()
        # print(dice_numbers) for debugging purpose

        print("-------------------")
        dice_sum = sum(dice_numbers)
        print(Fore.GREEN + f"Total: {dice_sum}")

        # use all() function to check if all values match with the first item
        if all(x == dice_numbers[0] for x in dice_numbers) and all(x == self.sides for x in dice_numbers):
            print("You are on a roll! You got all", self.sides, "!")
        elif all(x == dice_numbers[0] for x in dice_numbers):
            print("Yay! All rolls were the same!")

        # searching for number 6
        six_count = dice_numbers.count(self.sides)
        if six_count == 0:
            print(Fore.BLUE + "Sorry! No", self.sides, "found!")
        else:
            print(Fore.BLUE + f"Got {self.sides} in '{six_count}' roll(s).")
        print("=" * 40)
