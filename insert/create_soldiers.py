from base.soldier import Soldier
from .insert import sort_by_distance
#from dal.soldier_dal import insert_table_soldiers

def create_all_soldiers(all_soldiers):
    list_of_soldiers = []
    for soldier in all_soldiers:
        s_soldier = create_soldier(soldier)
        list_of_soldiers.append(s_soldier)
    #insert_table_soldiers(list_of_soldiers)
    soldiers_insert = sort_by_distance(list_of_soldiers)
    return soldiers_insert




def create_soldier(personal_data):
    if personal_data[0] // 10000000 != 1:
        return None
    ma = personal_data[0]
    first_name = personal_data[1]
    last_name = personal_data[2]
    gender = personal_data[3]
    city_of_residence = personal_data[4]
    distance = personal_data[5]
    soldier = Soldier(ma, first_name, last_name, gender, city_of_residence, distance)
    return soldier