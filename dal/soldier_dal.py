from db.connection import get_cursor


def insert_table_soldiers(rows):
    cursor = get_cursor()
    insert_query = '''insert into soldiers(
                            ma,
                            first_name,
                            last_name,
                            gender,
                            city,
                            distance)
                            values (%s, %s, %s, %s, %s, %s)'''
    for row in rows:
        cursor.execute(insert_query, row)