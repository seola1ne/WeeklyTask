import pymysql
import datetime

class LectureDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='jehyun')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS lecture (
                id INT AUTO_INCREMENT PRIMARY KEY,
                professor_id INT,
                course_id INT,
                day VARCHAR(10),
                start_time VARCHAR(30)
            );
            """
        self.cur.execute(sql)
        self.db.commit()


    def get_all_professor(self):
        sql = "select * from professor"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_all_course(self):
        sql = "select * from course"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def get_all_lecture(self):
        sql = "SELECT course.name, professor.name, professor.major, course.credit, lecture.day, lecture.start_time FROM lecture INNER JOIN professor ON lecture.professor_id = professor.id INNER JOIN course ON lecture.course_id = course.id"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result


    def add_lecture(self, lecture):
        sql = """INSERT IGNORE INTO lecture (professor_id, course_id, day, start_time) 
                VALUES (%s, %s, %s, %s)"""
        professor_id = lecture.professor_id
        course_id = lecture.course_id
        day = lecture.day
        start_time = lecture.start_time
        self.cur.execute(sql, (professor_id, course_id, day, start_time))
        self.db.commit()

    def delete_lecture(self, lecture):
        sql = "DELETE FROM lecture WHERE id = %s"
        self.cur.execute(sql, (lecture,))
        self.db.commit()
