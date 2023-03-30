# Title: Random Character Generator
# Name: Sunmi Kim
# Date: 02/17/2023

from colorama import Fore
import random

def display_title(): # display_title() function to display title
    print()
    print(Fore.RED + "=====*=====*=====*=====*=====*=====*=====*=====")
    print(Fore.GREEN + "========== Random Character Generator =========")
    print(Fore.BLUE + "=====*=====*=====*=====*=====*=====*=====*=====")

def get_name(): # get_name() function to display user name
    firstName = input(Fore.WHITE + "\nPlease enter your first name: ")
    #print("Hello, " + firstName + "!" + " Welcome to the RPG game! \nYou will be the judge in this game!")
    print(f'Hello, {firstName}! Welcome to the RPG game! \nYou will be the judge in this game!')
    print()

def random_character_generator(): # generate two random characters
    # List of names
    names = ["Noah", "Enoch", "Elijah", "Elisha", "Abraham", "Isaac", "Jacob", "Joseph", 
         "Judah", "Jesse", "David", "Moses", "Joshua", "Judas", "Ruth", 
         "Samuel", "Kings", "Chloe", "Ezra", "Nehemiah", "Esther", "Job", "Poet", "Solomon", "Jesse", 
         "Songs", "Isaiah", "Jeremiah", "Laura", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", 
         "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", 
         "Matthew", "Mark", "Luke", "John", "Peter", "James", "Paul", "Barnabas", "Matthias", "Lydia"]

    # List of attributes
    attributes = ["Adventure", "Creativeness", "Friendliness", "Intelligence", "Reliability", "Trustworthiness", 
              "Dependence", "Passion", "Compassion", "Excellence", "Integrity", "Humility", "Loveliness", 
              "Joy", "Peace", "Patience", "Kindness", "Goodness", "Gentleness", "Faithfulness", "Self-control"]

    # List of greetings
    greetings = ["Hi there!", "Hey, how's it going?", "Glad to see you!", 
                 "Good afternoon!", "Nice to meet you!", "Hello, stranger!"]

    # Generate 2 random users
    users = []

    for i in range(2):
        name = random.choice(names)
        attribute = random.choice(attributes)
        greeting = random.choice(greetings)
        strength = random.randint(51, 100)
        balance = random.randint(1, 10)
        speed = random.randint(11, 50)
        charisma = random.randint(101, 200)
        user = {
            "name": name, 
            "attribute": attribute, 
            "greeting": greeting,
            "strength": strength,
            "balance": balance,
            "speed": speed,
            "charisma": charisma,
            #"total": strength + balance + speed + charisma
        }
        users.append(user)
        #return users
        #print(users)

    # print the list of users:
    print()
    for user in users:
        print(f"Name:       {user['name']}")
        print(f"Attribute:  {user['attribute']}")
        print(f"Greeting:   {user['greeting']}")
        print(f"Strength:   {user['strength']}")
        print(f"Balance:    {user['balance']}")
        print(f"Speed:      {user['speed']}")
        print(f"Charisma:   {user['charisma']}")    
        print()
    # print(users)
    # for testing purpose: print(type(users))

    print(Fore.GREEN + "The total value of {0} is {1}.".format(users[0]['name'], users[0]['strength'] + users[0]['balance'] + users[0]['speed'] + users[0]['charisma']))
    print(Fore.BLUE + "The total value of {0} is {1}.\n".format(users[1]['name'], users[1]['strength'] + users[1]['balance'] + users[1]['speed'] + users[1]['charisma']))

def main():
    display_title()
    get_name() # will be a judge
    winners = []

    answer = input("Would you like to start the RPG game? (y/n)\n")

#   answer = "y"
    while answer.lower() == "y":
        menu = int(input(Fore.WHITE + "\n***** Menu *****\n\n1 - Start RPG game using two random characters."
                         + "\n\n2 - I'm done with this game. Exit\n"))
        if menu == 1:
            random_character_generator()
            winner = input(Fore.WHITE + "Who do you think is a winner? Enter winner's name: ")
            winners.append(winner)
            print(Fore.LIGHTYELLOW_EX + "Winners List: ", winners)

        elif menu == 2:
            print("Winners List: ", winners)
            print("Thanks for playing! Have a nice day!")
            print()
            break

        else:
            print("Invalid input. Please choose either 1 or 2\n")
    else: 
        print("Have a nice day!")

if __name__ == "__main__":
    main()
