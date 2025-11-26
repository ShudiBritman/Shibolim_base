class Room:
    room_id = 0
    def __init__(self):
        Room.room_id += 1
        self.list_of_soldiers = []
        self.bed_amount = 8
        self.id = Room.room_id

    def add_soldier(self, soldier):
        if len(self.list_of_soldiers) < self.bed_amount:
            self.list_of_soldiers.append(soldier)
            soldier.is_inserted = True
            print("adding a soldier")
            return True
        return False

