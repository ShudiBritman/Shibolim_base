class Soldier:
    def __init__(self, ma, first_name, last_name, gender, city_of_residence, distance):
        self.ma = ma
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city_of_residence = city_of_residence
        self.distance = distance
        self.is_inserted = None

    def __str__(self):
        return f"ma:{self.ma}, first name:{self.first_name}, last name: {self.last_name}, gender:{self.gender} city_of_residence:{self.city_of_residence}, is inserted:{self.is_inserted}"