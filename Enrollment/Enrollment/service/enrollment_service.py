from model.enrollment import EnrollmentDB

class EnrollmentService:
    def __init__(self):
        self.enrollment = EnrollmentDB()
        
    def get_all_enrollment(self):
        return [{'student_number':s[0], 'student_name':s[1], 'course_name':s[2], 'professor_name':s[3], 'credit':s[4]} for s in self.enrollment.get_all_enrollment()]

    def get_all_student(self):
        return [{'id':s[1], 'name':s[2]} for s in self.enrollment.get_all_student()]

    def get_all_lecture(self):
        return [{'id': lecture[0],
                'course_name': lecture[1],
                'professor_name': lecture[2],
                } for lecture in self.enrollment.get_all_lecture()]

    def add_enrollment(self, enrollment):
        self.enrollment.add_enrollment(enrollment)

    def get_course_by_id(self, id):
        return self.enrollment.get_course_by_id(id)

    def delete_enrollment(self, enrollment_id):
        self.enrollment.delete_enrollment(enrollment_id)