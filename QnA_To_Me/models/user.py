import pymysql

class UserDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS User (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                join_date DATETIME NOT NULL,
                PRIMARY KEY (id)
        )"""
        self.cur.execute(sql)
        self.db.commit()
        
    def get_all(self):
        sql = "select * from User"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def add(self, user):
        sql = """INSERT INTO User (name, email, join_date)
            SELECT  '{0}', '{1}', '{2}'
            FROM dual
            WHERE NOT EXISTS
            (SELECT name, email, join_date
            FROM User
            WHERE name='{0}' and email='{1}' and join_date='{2}'
            )
        """.format(user.name, user.email, user.join_date)
        self.cur.execute(sql)
        self.db.commit()
    
    def select_by_email(self, user):
        sql = "select * from User where email = '{0}'".format(user.email)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result