from models.professor import ProfessorDB

class ProfessorService:
    def __init__(self):
        self.professor_db = ProfessorDB()
        
    def get_all(self):
        return [{'id':s[0], 'name':s[1], 'major':s[2], 'email':s[3]} for s in self.professor_db.get_all()]

    def add(self, professor):
        return self.professor_db.add(professor)