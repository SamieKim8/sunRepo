# Date: 04/10/2023
# Author: Sunmi Kim
# Description: Dice Simulator Program

from colorama import Fore

def display_title(): 
    print(Fore.RED + "=" * 40)
    print(Fore.GREEN + "====== Welcome to the Dice Roller ======")
    print(Fore.BLUE + "=" * 40)
    print()

def get_positive_count(): # user enters preferred number to roll a dice
    while True:
        try:
            preferred_number = int(input(Fore.WHITE + "Enter your preferred number to roll a dice: "))
            if preferred_number <= 0:
                raise ValueError(Fore.RED + "Please enter a positive integer.")
            return preferred_number
        except ValueError as e: # ValueError e customized
            print(e)

def roll():
    dice_numbers = []
    preferred_number = get_positive_count()
    #print(preferred_number)
    for i in range(preferred_number): # dice input appear preferred_number times
        while True:
            try:
                dice_number = int(input(Fore.WHITE + f"Enter the dice number for roll {i+1}: "))
                if dice_number < 1 or dice_number > 6: # validation check as dice has only 6 numbers
                    raise ValueError(Fore.RED + "Dice number should be between 1 and 6.")
                dice_numbers.append(dice_number) # each dice number will be appended to dice_numbers list
                break
            except ValueError as e:
                print(e)
    return dice_numbers

def roll_dice():
    dice_numbers = roll()
    # print(dice_numbers) for debugging purpose

    print("-------------------")
    dice_sum = sum(dice_numbers)
    print(Fore.GREEN + f"Total: {dice_sum}")

    # use all() function to check if all values match with the first item
    if all(x == dice_numbers[0] for x in dice_numbers) and all(x == 6 for x in dice_numbers):
        print("You are on a roll! You got all 6!")
    elif all(x == dice_numbers[0] for x in dice_numbers):
        print("Yay! All rolls were the same!")

    # searching for number 6
    six_count = dice_numbers.count(6)
    if six_count == 0:
        print(Fore.BLUE + "Sorry! No 6 found!")
    else: # six_count > 0 but not all items are 6
        print(Fore.BLUE + f"Got 6 in '{six_count}' roll(s).")
    print(Fore.WHITE + "=" * 40)

def main():
    display_title() # display title function
    start = "y"
    while start.lower() == "y":
        roll_dice()
        start = input("Roll again? (y/n): ")
        print()
    print("Have a nice day!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
