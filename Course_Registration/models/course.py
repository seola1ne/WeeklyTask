import pymysql

class CourseDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS course (
            id INT AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            professor VARCHAR(45) NOT NULL,
            credit INT NOT NULL,
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()

    def add(self, course):
        sql = """INSERT INTO course (name, professor, credit) 
                select '{0}', '{1}', {2}
                from dual
                where not exists
                (select name, professor, credit
                from course
                where name='{0}' and professor='{1}' and credit={2}
                )
                """.format(course.name, course.professor, course.credit)
        self.cur.execute(sql)
        self.db.commit()

    def get_all(self):
        sql = "select * from course"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def select_by_name(self, course):
        sql = "select * from course where name = '{0}'".format(course.name)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result