from models.student import StudentDB

class StudentService:
    def __init__(self):
        self.student_db = StudentDB()
        
    def get_all(self):
        return [{'id':s[0],'number':s[1], 'name':s[2], 'gender':s[3]} for s in self.student_db.get_all()]    
    
    def add(self, student):
        self.check_duplication(student)
        return self.student_db.add(student)
    
    def check_duplication(self, student):
        results = self.student_db.select_by_number(student)
        for c in results:
            if c[1] == student.number:
                raise Exception('이미 등록된 학생입니다.')