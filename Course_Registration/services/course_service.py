from models.course import CourseDB

class CourseService:
    def __init__(self):
        self.course_db = CourseDB()
        
    def get_all(self):
        return [{'id':s[0],'name':s[1], 'professor':s[2], 'credit':s[3]} for s in self.course_db.get_all()]
        
    def add(self, course):
        self.check_duplication(course)
        self.course_db.add(course)
    
    def check_duplication(self, course):
        results = self.course_db.select_by_name(course)
        for c in results:
            if c[1] == course.name and c[2] == course.professor:
                raise Exception('이미 등록된 과목입니다.')