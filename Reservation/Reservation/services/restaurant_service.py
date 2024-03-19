from models.restaurant_db import RestaurantDB

class RestaurantService:
    def __init__(self):
        self.restaurant_db = RestaurantDB()
    
    def get_all(self):
        return self.restaurant_db.get_all()