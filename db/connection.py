import sqlite3

conn = sqlite3.connect("Shibolim_base.db")
cursor = conn.cursor()


def get_cursor():
    return cursor