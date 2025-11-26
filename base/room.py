class Room:
    def __init__(self):
        self.list_of_soldiers = []
        self.bed_amount = 8

    def add_soldier(self, soldier):
        if len(self.list_of_soldiers) < self.bed_amount:
            self.list_of_soldiers.append(soldier)
            soldier.is_inserted = True
            print("adding a soldier")
            return True
        return False

