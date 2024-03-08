from models.todo_model import TodoList
from models.todo_db import TodoDB

class TodoService:
    def __init__(self):
        self.todo_list = TodoList()
        self.todo_db = TodoDB()
        
    def get_tasks(self):
        return self.todo_list.get_tasks()
    
    def add_tasks(self, task):
        self.todo_list.add_tasks(task)
        self.todo_db.add(task)
        
    def complete_task(self, index):
        self.todo_list.complete_task(index)
        self.todo_db.complete(index)
        
    def delete_task(self, index):
        self.todo_list.delete_task(index)
        self.todo_db.delete(index)