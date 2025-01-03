import pymysql

class CourseDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='jehyun')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS course (
            id INT AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            credit INT NOT NULL,
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()

    def add_course(self, course):
        sql = """INSERT INTO course (name, credit) 
                select '{0}', {1}
                from dual
                where not exists
                (select name, credit
                from course
                where name='{0}'and credit={1}
                )
                """.format(course.name, course.credit)
        self.cur.execute(sql)
        self.db.commit()

    
    def get_all_course(self):
        sql = "select * from course"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    