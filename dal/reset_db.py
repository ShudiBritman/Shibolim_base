from db.connection import get_cursor


cursor = get_cursor()


def initialize_scheme():
    cursor.execute("CREATE TABLE homes (id PRIMARY KEY, name VARCHAR(50))")
    cursor.execute("CREATE TABLE rooms (id PRIMARY KEY, home INT)")
    cursor.execute("CREATE TABLE soldiers (ma PRIMARY KEY, first_name VARCHAR(100), last_name VARCHAR(100), gender VARCHAR(10), city VARCHAR(20), distance INT, is_inserted BOLLEAN)")
    cursor.close()
