# Name: Sunmi Kim
# Date: 06/04/2023

import sys
import os
import sqlite3
from contextlib import closing

from objects import Category
from objects import Movie

conn = None 

def connect():
    global conn
    if not conn:
        DB_FILE = "\Python Test\database\db_tester/movies.sqlite"        
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_category(row):
    return Category(row["categoryID"], row["categoryName"])

def make_movie(row):
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"],
            make_category(row))

def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            return make_category(row)
        else:
            return None
           
def get_movie(movie_id):
    query = '''select name from Movie where movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (movie_id,))
        result = c.fetchone()
        if result:
            return result[0]  # Extract the movie name from the row
        else:
            print("Movie not found") # return None as Movie not found

def get_movies_by_category(category_id):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_movies_by_minutes(minutes):
    query = '''SELECT movieID, Movie.name, year, 
                      minutes, Category.name as Category 
               FROM Movie join Category  
                      on Movie.categoryID = Category.categoryID 
               WHERE minutes < ? order by minutes ASC'''
    with closing(conn.cursor()) as c:
        c.execute(query, (minutes,))
        movies = c.fetchall()
        print(f"MOVIES - LESS THAN {minutes} MINUTES")
        print(f"{'ID':2}  {'Name':35} {'Year':4} {'Mins':4}  {'Category':15}")
        print("-" * 70)

    for i in movies:
        print(f"{i['movieID']:2}  {i['name']:35} {i['year']:4} {i['minutes']:4}  {i['Category']:15}")
    print()

def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def add_movie(movie):
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()

def delete_movie(movie_id):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        conn.commit()
        # test = conn.commit()
        # print("Test", test)
