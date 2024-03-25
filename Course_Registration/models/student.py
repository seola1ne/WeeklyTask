import pymysql

class StudentDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT,
            number INT NOT NULL,
            name VARCHAR(45) NOT NULL,
            gender VARCHAR(45) NOT NULL,
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()

    def add(self, student):
        sql = """INSERT INTO student (number, name, gender) 
        select {0}, '{1}', '{2}'
        from dual
        where not exists
        (select number, name, gender
        from student
        where number={0} and name='{1}' and gender='{2}'
        )
        """.format(student.number, student.name, student.gender)
        self.cur.execute(sql)
        self.db.commit()
    
    def get_all(self):
        sql = "select * from student"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def select_by_number(self, student):
        sql = "select * from student where number = '{0}'".format(student.number)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result