from base.home import Home
from base.create_homes import create_homes



def sort_by_distance(soldiers):
    homes = create_homes()
    soldiers.sort(key=lambda s: s.distance)
    response_dict = add_soldier_to_room(homes, soldiers)
    return response_dict




def add_soldier_to_room(homes, soldiers):
    soldiers_data = []
    were_assigned = 0
    not_were_assigned = 0
    for soldier in soldiers:
        space_available = False
        for i in range(len(homes)):
            home = homes[i]
            for j in range(len(home.list_of_rooms)):
                room = homes[i].list_of_rooms[j]
                if room.add_soldier(soldier):
                    space_available = True
                    inserted = {"ma":soldier.ma, "inserted":True, "home":i, "room":j}
                    soldiers_data.append(inserted)
                    were_assigned += 1
                    break
                if space_available:
                    break
        if not space_available:
            inserted = {"ma":soldier.ma, "inserted":"waiting_list"}
            soldiers_data.append(inserted)
            not_were_assigned += 1
    response_dict = {"were_assigned":were_assigned, "not_were_assigned":not_were_assigned, "soldiers":soldiers_data}
    return response_dict

