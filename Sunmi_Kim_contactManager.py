# Date: 04/24/2023
# Author: Sunmi Kim
# Title: Contacts Manager
# Description: Program to help user manage contacts information

from colorama import Fore

def display_title(): # title
    print(Fore.RED + "=" * 41)
    print(Fore.GREEN + "== Welcome to contacts manager program ==")
    print(Fore.BLUE + "=" * 41)
    print()

def display_menu(): # initial Command menu
    print(Fore.WHITE + "COMMAND MENU")
    print("\tlist - List all contacts")
    print("\tview - View a contact")
    print("\tadd -  Add a contact")
    print("\tdel -  Delete a contact")
    print("\tfield - View fields for all")
    print("\texit - Exit program")
    print()

def list(contacts): # display existing contact names
    if len(contacts) == 0:
        print(Fore.BLUE + "No contacts to show.\n")
        return
    else:
        i = 1
        for contact in sorted(contacts): # contacts sorted
            #print(contact)
            print("\t" + str(i) + ". " + contact)
            i += 1

def view(contacts):
    while True:
        name_input = input("Enter the name: ")
        if not name_input.isalpha():
            print("Please enter a valid name with only letters.")
            continue
        name = name_input.title()
        if name in contacts:
            print(f"Viewing contact for {name}:")
            contact_info = contacts[name]
            for field, value in contact_info.items():
                if value:
                    print(f"\t{field.title()}: {value}")
            break
        else:
            print(f"No contact found for '{name}'")

def add_contact(contacts): # add a new contact
    name_input = input("Name: ")
    name = name_input.title()
    if name not in contacts:
        address = input("Enter address: ")
        mobile = input("Enter mobile: ")
        company = input("Enter company: ")
    else:
        print(name + " already exists in the contacts.")

    # Create a dictionary for the new contact
    contact = {"address": address,
               "mobile": mobile,
               "company": company
    } 
    # Add the name to the contacts using name as key
    contacts[name] = contact

def del_contact(contacts): # delete an existing contact
    name_input = input("Name: ")
    name = name_input.title()
    if name in contacts:
        del contacts[name]
        print(Fore.BLUE + f"Contact for '{name}' deleted.")
    else:
        print(f"No contact found for that name, '{name}'.")

def field(): # user can view available columns of existing contacts
    field_options = {
        "1": "address",
        "2": "state",
        "3": "company",
        "4": "landline",
        "5": "mobile"
    }
    while True:
        print("Please select the field you want to view:")
        for option, field_name in field_options.items():
            print(f"\t{option}. {field_name.title()}")
        field_input = input("Enter the field number or name: ")
        selected_value = field_options.get(field_input) or field_input.lower()
        if selected_value in field_options.values():
            return selected_value
        else:
            print(Fore.RED + "Invalid value. Please enter a number (1~5) or a field name.")

def field_display(contacts): # display field info based on user selected_value
    selected_value = field()
    print(Fore.GREEN + f"Printing {selected_value} for all contacts") 
    for key in sorted(contacts.keys()):
        #print(key)
        if selected_value in contacts[key]:
            print(f"{key:10}: {contacts[key][selected_value]:30}")
        else:
            print(f"{key:10}: **No data**")        

def main(): # program starts in main function
    contacts = {
        "Joel":
            {"address": "1500 Anystreet, San Francisco, CA 94110", 
             "state": "California",             
             "company":"A startup",
             "mobile": "555-555-1111"},
        "Anne":
            {"address": "1000 Somestreet, Fresno, CA 93704",
             "state": "California",
             "landline": "125-555-2222", 
             "company": "Some Great Company"},
        "Sally":
            {"state": "Illinois", 
             "landline":"217-555-1222", 
             "company": "Illinois Technologies",
             "mobile": "217-333-2353"},
        "Ben":
            {"address": "1400 Another Street, Fresno CA 93704",
             "state": "California", 
             "mobile": "125-555-4444"}             
    }

    display_title()
    display_menu()
    while True:
        command = input(Fore.WHITE + "Please enter the command: ").lower()
        if command == "list":
            list(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add_contact(contacts)
        elif command == "del":
            del_contact(contacts)
        elif command == "field":
            field_display(contacts)
        elif command == "exit":
            print("Good Bye!")
            break
        else:
            print(Fore.RED + "Invalid command. Please try again.")

# if started as the main module, call the main function
if (__name__ == "__main__"):
    main()
