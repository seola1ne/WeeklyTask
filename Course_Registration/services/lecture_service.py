from models.lecture import LectureDB

class LectureService:
    def __init__(self):
        self.lecture_db = LectureDB()
        
    def get_all(self):
        return [{'id':s[0],'course_name':s[1], 'professor_name':s[2], 'major':s[3], 'credit':s[4], 'day':s[5], 'start_time':s[6], 'end_time':s[7]} for s in self.lecture_db.get_all()]
 