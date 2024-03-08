
class TodoList:
    def __init__(self):
        self.tasks = []
            
    def get_tasks(self):
        return self.tasks
    
    def add_tasks(self, task):
        self.tasks.append(task)
        
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['complete'] = True
        
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]