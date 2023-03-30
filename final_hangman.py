# Name: Sunmi Kim
# Date: 03/16/2023
# Title: Word Guessing Game (HangMan)

import final_wordlist as fwl
from colorama import Fore

hangman = [
    """
    ------
    |    |
    |
    |
    |
    |
    |
   ----------
   """,
   """
    ------
    |    |
    |    O
    |
    |
    |
    |
   ----------
   """,
   """
    ------
    |    |
    |    O
    |    |
    |
    |
    |
   ----------
   """,
   """
    ------
    |    |
    |    O
    |   \|
    |
    |
    |
   ----------
   """,
   """
    ------
    |    |
    |    O
    |   \|/
    |
    |
    |
   ----------
   """,
   """
    ------
    |    |
    |    O
    |   \|/
    |    |
    |
    |
   ----------
   """,
   """
    ------
    |    |
    |    O
    |   \|/
    |    |
    |   /
    |   
   ----------
   """,
   """
    ------
    |    |
    |    O
    |   \|/
    |    |
    |   / \\
    |   
   ----------
   """
]

def display_title():
    print(Fore.RED + "=====*=====*=====*=====*=====*=====*=====*=====")
    print(Fore.GREEN + "======== Word Guessing Game (HangMan) =========")
    print(Fore.BLUE + "=====*=====*=====*=====*=====*=====*=====*=====")
    print(Fore.WHITE + hangman[7])

def display_menu():
    print(Fore.WHITE + "-" * 30)
    print(Fore.WHITE + "\tTopics to choose: \n\t1. Fruit \n\t2. Animal \n\t3. Country")
    print(Fore.WHITE + "-" * 30)

# User can choose a topic for the game
def user_topic():
    while True:
        try:
            # User will choose topic among 3 lists - Fruit, Animal, and Country 
            topic = input(Fore.LIGHTYELLOW_EX + "Please choose your topic: ")
            print(Fore.WHITE + "-" * 30)
            if topic.isalpha():
                raise ValueError("Please enter a number between 1 and 3.")
            elif topic == str(1):
                print(Fore.LIGHTGREEN_EX + "'Fruit' is selected.")
                topic = fwl.fruits
                return topic
            elif topic == str(2):
                print(Fore.LIGHTMAGENTA_EX + "'Animal' is selected.")
                topic = fwl.animals
                return topic
            elif topic == str(3):
                print(Fore.LIGHTCYAN_EX + "'Country' is selected.")
                topic = fwl.countries
                return topic
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError as ve:
            print(ve)
            continue

# Get a random word from the word list
def get_word():
    word = fwl.get_random_word()
    return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))
    
    if num_wrong >= 1: # num_wrong allowed up to 8 times
        draw_hangman(num_wrong)

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
    
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 8 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            num_wrong += 1

        num_guesses += 1
        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 80)
    if remaining_letters == 0:
        print("Congratulations! You got it in", 
               num_guesses, "guesses.")   
        return True
    else:    
        print("Sorry, you lost.")
        print("The word was:", word)
        return False

def draw_hangman(num_wrong): #draw_hangman based on number of wrongs
    #num_wrong = (num_wrong)    
    if num_wrong == 1:
        print(hangman[1])
    elif num_wrong == 2:
        print(hangman[2])
    elif num_wrong == 3:
        print(hangman[3])
    elif num_wrong == 4:
        print(hangman[4])
    elif num_wrong == 5:
        print(hangman[5])
    elif num_wrong == 6:
        print(hangman[6])
    elif num_wrong == 7:
        print(hangman[7])
    else:
        print("You've incorrectly guessed 8 times.")

def main():
    print()
    display_title()
    game_result = False
    wins = 0
    lose = 0
    again = "y"

    while again.lower() == "y":
        display_menu()
        game_result = play_game()
        print() # "To check Return Value in main() "
        if game_result == True:
            wins += 1
        elif game_result == False:
            lose += 1
        else:
            print("Something must be gone wrong.")
            break
        # adding colorama style to display the game result
        print(Fore.LIGHTYELLOW_EX + "=" * 20)
        print(f"| You've won:  '{wins}' |")
        print(f"| You've lost: '{lose}' |")
        print(Fore.LIGHTYELLOW_EX + "=" * 20)
        print()
        again = input(Fore.WHITE + "Do you want to play again (y/n)?: ")
        print()
    else:
        words_played = fwl.used_fruits + fwl.used_animals + fwl.used_countries
        print(f"Words played in this game: {words_played}")
        print("Thanks for playing! Have a nice day.")
        print()

if __name__ == "__main__":
    main()
