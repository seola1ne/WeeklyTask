class ReservationFormDto:
    def __init__(self, restaurant_id, name, email, phone, num_guests, date_time):
        self._restaurant_id = restaurant_id
        self._name = name
        self._email = email
        self._phone = phone
        self._num_guests = num_guests
        self._date_time = date_time
        
    # property 함수로 지정해 주면 field처럼 사용할 수 있음
    @property
    def restaurant_id(self):
        return self._restaurant_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone(self):
        return self._phone
    
    @property
    def num_guests(self):
        return self._num_guests
    
    @property
    def date_time(self):
        return self._date_time