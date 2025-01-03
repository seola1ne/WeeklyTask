from model.course import CourseDB

class CourseService:
    def __init__(self):
        self.course_db = CourseDB()

    def get_all_course(self):
        return [{'name':s[0], 'credit':s[1]} for s in self.course_db.get_all_course()]

    def add_course(self, course):
        self.course_db.add_course(course)