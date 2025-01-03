from model.lecture import LectureDB

class LectureService:
    def __init__(self):
        self.lectureDB = LectureDB()  

    def get_all_professor(self):
        return [{'id':s[0], 'name':s[1], 'major':s[2], 'email':s[3]} for s in self.lectureDB.get_all_professor()]
    def get_all_course(self):
        return [{'id':s[0], 'name':s[1], 'professor':s[2], 'credit':s[3]} for s in self.lectureDB.get_all_course()]
    
    def get_all_lecture(self):
        return [{'course_name': lecture[0],
                'professor_name': lecture[1],
                'professor_major': lecture[2],
                'credit': lecture[3],
                'day': lecture[4],
                'start_time': lecture[5]} for lecture in self.lectureDB.get_all_lecture()]

    def add_lecture(self, lecture):
        self.lectureDB.add_lecture(lecture)
    def delete_lecture(self, lecture):
        self.lectureDB.delete_lecture(lecture)

