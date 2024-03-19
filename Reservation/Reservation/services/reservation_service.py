from models.reservation_db import ReservationDB

class ReservationService:
    def __init__(self):
        self.reservation_db = ReservationDB()
        
    def get_all(self):
        return self.reservation_db.get_all()

    def add(self, restaurant_dto):
        self.reservation_db.add(restaurant_dto)
    
    def delete(self, reservation_id):
        try:
            return self.reservation_db.delete(reservation_id)
        except Exception as ex:
            print(ex)