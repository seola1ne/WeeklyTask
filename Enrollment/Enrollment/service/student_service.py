from model.student import StudentDB

class StudentService:
    def __init__(self):
        self.studentDB = StudentDB()
        
    def get_all_student(self):
        return [{'number':s[1], 'name':s[2], 'gender':s[3]} for s in self.studentDB.get_all_student()]

    def add_student(self, student):
        self.studentDB.add_student(student)

    def get_schedule_student(self, student_id):
        return [{'course_name':s[0], 'day':s[1], 'start_time':s[2], 'professor_name': s[3], 'credit': s[4]} for s in self.studentDB.get_schedule_student(student_id)]

