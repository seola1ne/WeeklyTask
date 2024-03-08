import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='reTodolist')
        self.cur = self.db.cursor()
        print("connect ok")
        
    def add(self, task):
        sql = "insert into todos(task) values('{0}')".format(task['name'])
        self.cur.execute(sql)
        self.db.commit()
        
    def complete(self, index):
        sql = "update todos set completed = 'True' where indexx = '{0}'".format(index)
        self.cur.execute(sql)
        self.db.commit()
        
    def delete(self, index):
        sql = "delete from todos where indexx = '{0}'".format(index)
        self.cur.execute(sql)
        self.db.commit()