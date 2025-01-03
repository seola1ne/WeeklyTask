import pymysql

class ProfessorDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Professor (
            id INT AUTO_INCREMENT,
            name varchar(45) NOT NULL,
            major varchar(45) NOT NULL,
            email varchar(45) not null,
            PRIMARY KEY(id)
            )
            """
        self.cur.execute(sql)
        self.db.commit()
        print("connect ok")
        
    def get_all(self):
        sql = "select * from Professor"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, professor):
        sql = "insert into Professor (name, major, email) values (%s, %s, %s)"
        params = (professor.name, professor.major, professor.email)
        self.cur.execute(sql, params)
        self.db.commit()