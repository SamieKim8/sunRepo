# Name: Sunmi Kim
# Date: 06/04/2023

import db
from objects import Movie

def display_welcome():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("min  - View movies by minutes")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    print()
    category = db.get_category(category_id)
    movies = db.get_movies_by_category(category_id)
    display_movies(movies, category.name.upper())
    
def display_movies(movies, title_term):
    print("MOVIES -" + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)

    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_minutes():
    minutes = int(input("Maximum number of minutes: "))
    db.get_movies_by_minutes(minutes)

def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    movie = Movie(name=name, year=year, minutes=minutes,
                  category=category)
    db.add_movie(movie)    
    print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    movie_name = db.get_movie(movie_id)
    while True:
        try:
            confirm = input(f"Are you sure you want to delete '{movie_name}'? (y/n) ")
            if confirm.lower() == "":
                raise ValueError("Enter either 'y' or 'n'")
            elif confirm.lower() == "n":
                print(f"{movie_id} '{movie_name}' will not be deleted.")
                break
            elif confirm.lower() != "y":
                raise ValueError("Enter either 'y' or 'n'")
            else:
                db.delete_movie(movie_id)
                print(f"Movie ID {movie_id} '{movie_name}' was deleted from database.\n")
                break
        except ValueError as e:
            print(e)
       
def main():
    db.connect()
    display_welcome()
    display_categories()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "min":
            display_movies_by_minutes()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
