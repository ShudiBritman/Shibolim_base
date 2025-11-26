from db.connection import get_cursor



cursor = get_cursor()

def insert_rooms_table(id, home_id):
    cursor.execute('''INSERT INTO rooms (id, home_id)
                   VALUES(id, home_id)''')
    print(f"adding a room to room{home_id}")
    cursor.close()