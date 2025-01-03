import pymysql

class QuestionDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Question (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            contents VARCHAR(255) NOT NULL,
            category VARCHAR(50) NOT NULL,
            create_date DATETIME NOT NULL
        )"""
        self.cur.execute(sql)
        self.db.commit()
        
    def get_all(self):
        sql = "select * from Question"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, question):
        sql = """INSERT INTO Question (contents, category, create_date)
            SELECT  '{0}', '{1}', '{2}'
            FROM dual
            WHERE NOT EXISTS
            (SELECT contents, category, create_date
            FROM Question
            WHERE contents='{0}' and category='{1}' and create_date='{2}'
            )
        """.format(question.contents, question.category, question.create_date)
        self.cur.execute(sql)
        self.db.commit()
    
    def select_by_contents(self, question):
        sql = "select * from Question where contents = '{0}'".format(question.contents)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result