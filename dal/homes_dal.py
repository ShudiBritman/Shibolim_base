from db.connection import get_cursor
from .rooms_dal import insert_rooms_table


cursor = get_cursor()
def insert_homes(home):
    cursor.execute('''INSERT INTO homes (id)
                       VALUES(home.id)''')
    print("adding a home")
    for room in home.list_of_rooms:
        insert_rooms_table(room.id, home.id)
    cursor.close()

