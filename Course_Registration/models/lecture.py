import pymysql

class LectureDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Lecture (
            id INT AUTO_INCREMENT,
            professor_id int NOT NULL,
            course_id int NOT NULL,
            day datetime not null,
            start_time time not null,
            end_time time not null,
            FOREIGN KEY(professor_id) references professor (id),
            FOREIGN KEY(course_id) references course (id),
            UNIQUE INDEX(professor_id, course_id),
            PRIMARY KEY(id)
            )
            """
        self.cur.execute(sql)
        self.db.commit()
        print("connect ok")
        
    def get_all(self):
        sql = """SELECT 
                l.id,
                c.name AS name, 
                p.name AS name, 
                p.major AS major, 
                c.credit, 
                l.day, 
                l.start_time, 
                l.end_time
            FROM 
                lecture l
            JOIN 
                course c ON l.id = c.id
            JOIN 
                professor p ON l.id = p.id;
        """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, lecture):
        sql = "insert into Lecture (professor_id, course_id, day, start_time, end_time) values (%s, %s, %s, %s, %s)"
        params = (lecture.professor_id, lecture.course_id, lecture.day, lecture.start_time, lecture.end_time)
        self.cur.execute(sql, params)
        self.db.commit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             