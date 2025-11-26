class Home:
    def __init__(self):
        self.list_of_rooms = []
        self.max_room = 10

    def add_room(self, room):
        if len(self.list_of_rooms) > self.max_room:
            self.list_of_rooms.append(room)
            return True
        return False
