# Date: 04/15/2023
# Author: Sunmi Kim
# Title: Contacts Manager
# Description: Program to help user manage contacts information
# Supports
#   listing all contacts,
#   viewing/adding/deleting a contact,
#   printing a given field for all contacts.
# Program uses dictionary of dictionaries to hold the contacts information.

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

def view(contacts): # view selected contact 
    name_input = input("Enter the name: ")
    name = name_input.title()
    if name in contacts:
        print(f"Viewing contact for {name}:")
        name = contacts[name]
        if name.get("address"):
            print("\tAddress: " + name["address"])
        if name.get("state"):
            print("\tState: " + name["state"])
        if name.get("company"):
            print("\tCompany: " + name["company"])
        if name.get("landline"):
            print("\tLandline: " + name["landline"])
        if name.get("mobile"):
            print("\tMobile: " + name["mobile"])
    else:
        print(f"No contact found for that name, '{name}'")
    print()

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

def field():
    while True:
        try:
            field = input(Fore.WHITE + "\t1. address \n\t2. state \n\t3. company \n\t4. landline \n\t5. mobile\n" +
                "Please select the field you want to view: ")
            if field == str(1) or field == "address": # address
                selected_value = "address"     
                return selected_value
            elif field == str(2) or field == "state": # state
                selected_value = "state"
                return selected_value
            elif field == str(3) or field == "company": # company
                selected_value = "company"
                return selected_value
            elif field == str(4) or field == "landline": # landline
                selected_value = "landline"
                return selected_value
            elif field == str(5) or field == "mobile": # mobile
                selected_value = "mobile"
                return selected_value
            else:
                raise ValueError(Fore.RED + "Invalid value. Please enter a number (1~5) or a field name.")
        except ValueError as e:
            print(e)

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
