from model.professor import ProfessorDB

class ProfessorService:
    def __init__(self):
        self.professorDB = ProfessorDB()
        
    def get_all_professor(self):
        return [{'name':s[1], 'major':s[2], 'email':s[3]} for s in self.professorDB.get_all_professor()]

    def add_professor(self, professor):
        self.professorDB.add_professor(professor)

    def get_schedule_professor(self, professor_id):
        return self.professorDB.get_schedule_professor(professor_id)