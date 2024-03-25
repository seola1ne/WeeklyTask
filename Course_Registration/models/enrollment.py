import pymysql

class EnrollmentDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS enrollment (
            id INT AUTO_INCREMENT,
            student_id int NOT NULL,
            course_id int NOT NULL,
            FOREIGN KEY(student_id) references student (id),
            FOREIGN KEY(course_id) references courese (id),
            UNIQUE INDEX(student_id, course_id),
            PRIMARY KEY(id)
            )
            """
        self.cur.execute(sql)
        self.db.commit()
        print("connect ok")

    def add(self, enrollment):
        # sql = """INSERT INTO enrollment (student_id, course_id) 
        #         select {0}, {1}
        #         from dual
        #         where not exists
        #         (select student_id, course_id
        #         from enrollment
        #         where student_id={0} and course_id={1}
        #         )
        #         """.format(enrollment.student_id, enrollment.course_id)
        sql = ("insert ignore into enrollment(student_id, course_id) values({0}, {1})").format(enrollment.student_id, enrollment.course_id)
        self.cur.execute(sql)
        self.db.commit()
    
    def delete(self, enrollment_id):
        sql = """DELETE from enrollment where id={0}""".format(enrollment_id)
        self.cur.execute(sql)
        self.db.commit()
    
    def get_all(self):
        sql = """SELECT s.number, s.name, c.name, c.professor, c.credit
                FROM student s
                JOIN enrollment e 
                ON (s.id = e.student_id)
                JOIN course c ON (c.id = e.course_id)"""
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_students(self):
        sql = "select * from student"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_courses(self):
        sql = "select * from course"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result