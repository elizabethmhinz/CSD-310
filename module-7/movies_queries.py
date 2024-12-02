# Code created for Module 7.2 CSD310-A339 by Liz Hinz
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "lukenick14144!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True

}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
                                    
    input("\n\n Press any key to continue...")


    cursor = db.cursor()

    # Query 1 - select all the fields for the studio tables
    cursor.execute('SELECT studio_id, studio_name FROM studio')
    studios = cursor.fetchall()
    print('\n-- DISPLAYING Studio RECORDS --')
    for studio_id,studio_name in studios:
        print(f'Studio ID: {studio_id}\nStudio Name: {studio_name}\n')

    # Query 2 - select all the fields for the genre tables
    cursor.execute('SELECT genre_id, genre_name FROM genre')
    genres = cursor.fetchall()
    print('\n-- DISPLAYING Genre RECORDS --')
    for genre_id,genre_name in genres:
        print(f'Genre ID: {genre_id}\nGenre Name: {genre_name}\n')
        
    # Query 3 - select movies names for those movies that have a run time of less than two hours.
    cursor.execute('SELECT film_name, film_runtime FROM film WHERE film_runtime < 120')
    short_movies = cursor.fetchall()
    print('\n-- DISPLAYING Short Films RECORDS --')
    for film_name, film_runtime in short_movies:
        print(f'Film Name: {film_name}\nFilm Runtime: {film_runtime}\n')

    # Query 4 - get a list of film names, and directors grouped by director
    cursor.execute('SELECT film_name, film_director FROM film ORDER BY film_director')
    films_by_director = cursor.fetchall()
    print('\nFilms grouped by film director:')
    for film_name, film_director in films_by_director:
        print(f'Film Name: {film_name}\nFilm Director: {film_director}\n')
        

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    try:
        cursor.close()
    except:
        pass
    db.close()
    
