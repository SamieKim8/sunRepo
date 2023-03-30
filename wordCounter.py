# Title: Gutenberg Word Counter
# Name: Sunmi Kim
# Date: 03/05/2023

from colorama import Fore

# three books A, B, C, and E for exit 
filename_a = "anneofgreengables.txt"
filename_b = "anneofavonlea.txt"
filename_c = "anneoftheisland.txt"

search_list = []

def display_menu():
    print(Fore.RED + "=====*=====*=====*=====*=====*=====*=====*=====")
    print(Fore.GREEN + "==== Gutenberg Story Word Counter Program ====")
    print(Fore.BLUE + "=====*=====*=====*=====*=====*=====*=====*=====")
    print()
    print(Fore.WHITE + "Please choose from one of the stories below: ")
    print("A - Anne of Green Gables (1908)")
    print("B - Anne of Avonlea (1909)")
    print("C - Anne of the Island (1915)")
    print("E - Exit Program")
    print()   

def word_validation():
    while True:
        try:
            search_string = input("What would you like to search for? ")
            if not search_string.isalpha():
                raise ValueError(Fore.RED + "Please enter a word or a string not numbers.")
            break
        except ValueError as ve:
            print(ve)
        finally: 
            return search_string

def string_search(filename):    
    # Open the file and read its contents
    with open(filename, "r", encoding = 'utf-8') as story1:
        # save the entire story to a string
        contents = story1.read()
    
    # break the string into a list of words
    num_words = len(contents.split())

    # number of words in the list = print(len(num_words))
    # Print the number of words
    print("The story contains '{0}' words.\n".format(num_words))

    # answer = "y"
    while True:
        #search_string = input("What would you like to search for? ")
        search_string = word_validation()
       
        # Count the number of occurrences of the search string
        num_occurrences = contents.count(search_string)

        # Print the number of occurrences
        print(Fore.BLUE + "\nThe string '{0}' appears '{1}' times in '{2}'.\n".format(search_string, num_occurrences, filename))
        search_list.append(search_string)
        search_list.append(num_occurrences)
        # print(search_list)
        answer = input(Fore.WHITE + "Would you like to search again? (y/n) ")
        if answer.lower() == "y":
            if filename == filename_a:
                book_title = "Anne of Green Gables"
                search_list.append(book_title)
            elif filename == filename_b:
                book_title = "Anne of Avonlea"
                search_list.append(book_title)
            elif filename == filename_c:
                book_title = "Anne of the Island"
                search_list.append(book_title)
            continue
        elif answer.lower() == "n":
            break
        else:
            print("Invalid input. Please choose either 'Y' or 'N': ")

def display_search_list(): # to display string search result
    print(Fore.GREEN + f"{'BOOK':30} {'SEARCH TERM':20} {'RESULTS':5}")
    for i in range(0, len(search_list), 3): 
        # search list formatted for proper alignment
        print(Fore.WHITE + f"{search_list[i]:30} {search_list[i+1]:20} {search_list[i+2]:5}")

def main():     
    # List user menu
    while True:       
        display_menu() 
        command = input("Your choice (A, B, C or E): ")
        if command.lower() == "a":
            book_title = "Anne of Green Gables"
            print("\nGreat!, we will work with '{}'\n".format(book_title))
            search_list.append(book_title)
            string_search(filename_a)
        elif command.lower() == "b":
            book_title = "Anne of Avonlea"
            print("\nGreat!, we will work with '{}'\n".format(book_title))
            search_list.append(book_title)
            string_search(filename_b)
        elif command.lower() == "c":
            book_title = "Anne of the Island"
            print("\nGreat!, we will work with '{}'\n".format(book_title))
            search_list.append(book_title)
            string_search(filename_c)
        elif command.lower() == "e":
            break
        else:
            print("Not a valid input. Please select from A, B, C and E.\n")
            continue
    
    display_search_list()
    print()
    print("Thank you for searching! Goodbye.")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
