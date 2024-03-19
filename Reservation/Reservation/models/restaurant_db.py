import pymysql

class RestaurantDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS restaurant (
            id INT AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            address VARCHAR(45) NOT NULL,
            phone VARCHAR(45) NOT NULL,
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()
        
        sql = """insert into restaurant(name, address, phone)
            select '김해시락국밥', '부산소마고 옆', '051-1111-2222'
            from dual
            where not exists
            (select name, address, phone
            from restaurant
            where name='김해시락국밥' and address='부산소마고 옆' and phone='051-1111-2222')"""
        self.cur.execute(sql)    
            
        sql = """insert into restaurant(name, address, phone)
            select '마산뼈해장국', '우리 집 옆', '055-2222-1111'
            from dual
            where not exists
            (select name, address, phone
            from restaurant
            where name='마산뼈해장국' and address='우리 집 옆' and phone='055-1111-2222')"""
        self.cur.execute(sql)
        self.db.commit()
        print("connect ok")
        
    def get_all(self):
        sql = "select * from restaurant;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result