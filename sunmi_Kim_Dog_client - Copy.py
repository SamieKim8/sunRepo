from colorama import Fore
from sunmi_Kim_Dog_object import Dog # import Dog class

def main():
    print(Fore.RED + "=" * 40)
    print(Fore.GREEN + "==== Willie welcomes you! Woof woof ====")
    print(Fore.BLUE + "=" * 40)
    print(Fore.WHITE)

    dog_name = input("Enter your dog's name: ")
    dog_color = input("Enter your dog's color: ")
    willie = Dog(dog_name, dog_color, weight=15)
    
    while True:
        userInput = input(Fore.WHITE + "Enter the command\n'S' to get Status enquiry, \t\t'F' to feed the dog,"
             "\n'W' to take it for a walk, \t\t'Q' to exit:\n") 
        if userInput.upper() == 'S':            
            willie.printStatus()
            print("-" * 40)
        elif userInput.upper() == 'F':
            willie.eat()
            print("-" * 40)
        elif userInput.upper() == 'W':
            willie.walk()
            print("-" * 40)
        elif userInput.upper() == 'Q':
            print(Fore.MAGENTA + "Good bye! Woof woof")
            print(Fore.WHITE)
            break
        else:
            print("Invalid command. Please try again.")
            continue           

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
