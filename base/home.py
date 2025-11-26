from room import Room


class Home:
    def __init__(self):
        self.max_room = 10
        self.list_of_rooms = self.add_room()


    def add_room(self):
        for i in range(self.max_room):
            room = Room()
            self.list_of_rooms.append(room)
        return self.list_of_rooms

    def Check_occupancy(self):
        return len(self.list_of_rooms) < self.max_room


