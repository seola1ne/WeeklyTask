import pymysql

class EnrollmentDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='jehyun')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS enrollment (
            id INT AUTO_INCREMENT,
            student_id int NOT NULL,
            course_id int NOT NULL,
            lecture_id int NOT NULL,
            PRIMARY KEY(id)
            )
            """
        self.cur.execute(sql)
        self.db.commit()

    def add_enrollment(self, enrollment):
        sql = """
        INSERT INTO enrollment (student_id, course_id, lecture_id)
        SELECT %s, %s, %s FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM enrollment
            WHERE student_id = %s AND course_id = %s AND lecture_id = %s
        )
        """
        params = (enrollment.student_id, enrollment.course_id, enrollment.lecture_id,
                enrollment.student_id, enrollment.course_id, enrollment.lecture_id)
        self.cur.execute(sql, params)
        self.db.commit()

    
    def delete_enrollment(self, enrollment_id):
        sql = """DELETE from enrollment where id={0}
        """.format(enrollment_id)
        self.cur.execute(sql)
        self.db.commit()
    
    # Student Number	Student Name	Course Name	Professor	Credit
    def get_all_enrollment(self):
        sql = """SELECT 
                    s.number AS 'Student Number',
                    s.name AS 'Student Name',
                    c.name AS 'Course Name',
                    c.professor AS 'Professor',
                    c.credit AS 'Credit'
                FROM 
                    enrollment e
                JOIN 
                    student s ON e.student_id = s.number
                JOIN 
                    course c ON e.course_id = c.id"""
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_all_student(self):
        sql = "select * from student"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def get_course_by_id(self, id):
        sql = "select course_id from lecture where id={0}".format(id)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result
    
    def get_all_lecture(self):
        sql = """SELECT l.id, c.name AS course_name, p.name AS professor_name
                FROM lecture l
                JOIN course c ON l.course_id = c.id
                JOIN professor p ON l.professor_id = p.id"""
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
