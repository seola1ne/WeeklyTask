import pymysql

class ReservationDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS reservation (
            id INT AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            email VARCHAR(45) NOT NULL,
            phone VARCHAR(45) NOT NULL,
            num_guests INT NOT NULL,
            date_time DATETIME NOT NULL,
            restaurant_id INTEGER NOT NULL,
            FOREIGN KEY (restaurant_id) REFERENCES restaurant (id),
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()
        print("connect ok")
        
    def add(self, reservation):
        print(reservation.name)
        sql = """INSERT INTO reservation (restaurant_id, name, email, phone, num_guests, date_time) 
        values ({0}, '{1}', '{2}', '{3}', {4}, '{5}')
        """.format(reservation.restaurant_id, reservation.name, reservation.email, reservation.phone, reservation.num_guests, reservation.date_time)
        self.cur.execute(sql)
        self.db.commit()
       
    def get_all(self):
        sql = "select * from reservation"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def delete(self, reservation_id):
        sql = "delete from reservation where id = {0};".format(reservation_id)
        result = self.cur.execute(sql)
        self.db.commit()
        return result