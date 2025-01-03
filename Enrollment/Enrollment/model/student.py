import pymysql

class StudentDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='jehyun')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT,
            number INT NOT NULL,
            name VARCHAR(45) NOT NULL,
            gender VARCHAR(45) NOT NULL,
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()

    def add_student(self, student):
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
    
    def get_all_student(self):
        sql = "select * from student"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_schedule_student(self, student_id):
        sql = """
            SELECT c.name AS course_name, l.day, l.start_time, p.name AS professor, c.credit
            FROM enrollment e
            JOIN lecture l ON e.lecture_id = l.id
            JOIN course c ON e.course_id = c.id
            JOIN professor p ON l.professor_id = p.id
            WHERE e.student_id = %s;
        """
        self.cur.execute(sql, (student_id))
        result = self.cur.fetchall()
        return result
