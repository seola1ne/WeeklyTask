import pymysql

class AnswerDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='weeklytask')
        self.cur = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Answer (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            answer_contents VARCHAR(255) NOT NULL,
            answer_date DATETIME NOT NULL,
            user_id INT,
            question_id INT,
            FOREIGN KEY (user_id) REFERENCES User(id),
            FOREIGN KEY (question_id) REFERENCES Question(id),
            UNIQUE INDEX(user_id, question_id)
        )"""
        self.cur.execute(sql)
        self.db.commit()
        
    def get_all(self):
        sql = """SELECT User.name, Question.contents AS QuestionContents, Answer.answer_contents AS AnswerContents, Answer.answer_date AS AnswerDate
                FROM Answer
                INNER JOIN Question ON Answer.question_id = Question.id
                INNER JOIN User ON Answer.user_id = User.id
            """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def get_users(self):
        sql = "select * from User"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_user_by_name(self, name):
        sql = "select * from User where name = '{0}'".format(name)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def get_questions(self):
        sql = "select * from Question"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def add(self, answer):
        sql = """INSERT IGNORE INTO Answer(answer_contents, answer_date, user_id, question_id) VALUES (%s, %s, %s, %s)"""
        params = (answer.answer_contents, answer.answer_date, answer.user_id, answer.question_id)
        self.cur.execute(sql, params)
        self.db.commit()
        
    def delete(self, answer_id):
        sql = """DELETE from Answer where id = {0}""".format(answer_id)
        self.cur.execute(sql)
        self.db.commit()
        
    # def edit(self, answer):
    #     sql = """UPDATE Answer 
    #     SET 
    #     WHERE id = {0} """