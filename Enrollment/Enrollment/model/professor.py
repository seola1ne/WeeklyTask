import pymysql

class ProfessorDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='jehyun')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS professor (
            id INT AUTO_INCREMENT,
            name VARCHAR(45) NOT NULL,
            major VARCHAR(45) NOT NULL,
            email VARCHAR(45) NOT NULL,
            PRIMARY KEY(id))"""
        self.cur.execute(sql)
        self.db.commit()

    def add_professor(self, professor):
        sql = """INSERT INTO professor (name, major, email) 
        select '{0}', '{1}', '{2}'
        from dual
        where not exists
        (select name, major, email
        from professor
        where name='{0}' and major='{1}' and email='{2}'
        )
        """.format(professor.name, professor.major, professor.email)
        self.cur.execute(sql)
        self.db.commit()
    
    def get_all_professor(self):
        sql = "select * from professor"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def get_schedule_professor(self, professor_id):
        sql = """
            SELECT c.name AS course_name, l.day, l.start_time, c.credit
            FROM professor p
            JOIN lecture l ON p.id = l.professor_id
            JOIN course c ON l.course_id = c.id
            WHERE p.id = {0}
        """.format(professor_id)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result