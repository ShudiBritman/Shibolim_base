from sort import bobble_sort
from base.home import Home


def insert_by_distance(soldiers):
    soldiers = bobble_sort(soldiers)
    pointer = 0
    home1 = Home()
    home2 = Home()


def add_soldier_to_room(home, soldiers, pointer):
    bed_amount = home.list_of_rooms[0].bed_amount
    for i in range(len(home.list_of_rooms)):
        for j in range(bed_amount):
            home.list_of_rooms[i].add_soldier(soldiers[pointer])
            soldiers[pointer].is_inserted = True





