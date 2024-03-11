from models.blog_db import BlogDB

class BlogService:
   def __init__(self):
       self.blog_db = BlogDB()
       
   def get_posts(self):
       return self.blog_db.getAll()
   
   def get_post(self, id):
       return self.blog_db.getOne(id)
   
   def add_post(self, title, content, author):
       return self.blog_db.add(title, content, author)
       
   def update_post(self, title, content, author, id):
       return self.blog_db.update(title, content, author, id)
       
   def delete_post(self, id):
       return self.blog_db.delete(id)
