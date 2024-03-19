import pymysql

class BlogDB:
   def __init__(self):
       self.db = pymysql.connect(host='localhost', user='root', password='1234', db='WeeklyTask')
       self.cur = self.db.cursor()
       print("connect ok")
       
   def get_all(self):
       sql = "select * from blog"
       self.cur.execute(sql)
       result = self.cur.fetchall()
       return result
       
   def getOne(self, id):
       sql = "select * from blog where id = %s" 
       self.cur.execute(sql, (id))
       result = self.cur.fetchone()
       return result
       
   def add(self, title, content, author):
       sql = "insert into blog (title, content, author) values (%s, %s, %s)"
       self.cur.execute(sql, (title, content, author))
       self.db.commit()
       return True
       
   def update(self, title, content, author, id):
       sql = "update blog set title = %s, content = %s, author = %s where id = %s"
       self.cur.execute(sql, (title, content, author, id)) 
       self.db.commit()
       return True
       
   def delete(self, id):
       sql = "delete from blog where id = %s"
       self.cur.execute(sql, (id))
       self.db.commit()
       return True
