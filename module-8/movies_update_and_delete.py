# Code created for Module 8.2 CSD310-A339 by Liz Hinz
import mysql.connector
from mysql.connector import errorcode

# Establish database connection configuration 
config = {
    "user": "root",
    "password": "lukenick14144!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("""
        SELECT film_name AS Name,
            film_director AS Director,
            genre_name AS Genre,
            studio_name AS 'Studio Name'
        FROM film INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)

    # get the results from the cursor object
    films = cursor.fetchall()

    print('\n -- {} --'.format(title))

    # iterate over the film data set and display the results
    for film in films:
        print('Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n'.format(film[0], film[1], film[2], film[3]))

def main():
    try:
        # connect to database
        db = mysql.connector.connect(**config)
        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
        input("\n\n Press any key to continue...")
        cursor = db.cursor()

        show_films(cursor, 'DISPLAYING FILMS')

        # Insert new record into film table
        cursor.execute("""
            INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
            VALUES ('Nope', '2022', 130, 'Jordan Peele',
                    (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),
                    (SELECT genre_id FROM genre WHERE genre_name = 'Horror'))
        """)
        db.commit()

        # Display the selected fields and the associated label
        show_films(cursor, 'DISPLAYING FILMS AFTER INSERT')

        # Update Alien genre from SciFi to horror
        cursor.execute("""
            UPDATE film
            SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
            WHERE film_name = 'Alien'
        """)
        db.commit()

        # Display films with update
        show_films(cursor, 'DISPlAYING FILMS AFTER UPDATE - Changed Alien to Horror')

        # Delete Gladiator entry
        cursor.execute("""
            DELETE FROM film WHERE film_name = 'Gladiator'
        """)
        db.commit()

        # Call the show_films function to display the selected fields
        show_films(cursor, 'DISPLAYING FILMS AFTER DELETE')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    main()


