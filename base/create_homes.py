from .home import Home
#from dal.homes_dal import insert_homes

def create_homes():
    home1 = Home()
    home2 = Home()
    homes = [home1, home2]
    #insert_homes(homes[0])
    #insert_homes(homes[1])
    return homes