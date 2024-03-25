from models.enrollment import EnrollmentDB

class EnrollmentService:
    def __init__(self):
        self.enrollment_db = EnrollmentDB()
        
    def get_all(self):
        return [{'student_number':s[0],'student_name':s[1], 'course_name':s[2], 'professor':s[3], 'credit':s[4]} for s in self.enrollment_db.get_all()]
    
    def get_students(self):
        return [{'id':s[0],'number':s[1], 'name':s[2], 'gender':s[3]} for s in self.enrollment_db.get_students()]    
    
    def get_courses(self):
        return [{'id':s[0],'name':s[1], 'professor':s[2], 'credit':s[3]} for s in self.enrollment_db.get_courses()]
    
    def add(self, enrollment):
        self.enrollment_db.add(enrollment)
        
    def delete(self, enrollment_id):
        self.enrollment_db.delete(enrollment_id)