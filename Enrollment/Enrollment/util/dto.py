class StudentFormDto:
    def __init__(self, number, name, gender):
        self._number = number
        self._name = name
        self._gender = gender
    
    @property
    def number(self):
        return self._number
    
    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return self._gender


class CourseFormDto:
    def __init__(self, name, credit):
        self._name = name
        self._credit = credit
    
    @property
    def name(self):
        return self._name
    
    @property
    def credit(self):
        return self._credit
    

class EnrollmentFormDto:
    def __init__(self, student_id, course_id, lecture_id):
        self._student_id = student_id
        self._course_id = course_id
        self._lecture_id = lecture_id
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def lecture_id(self):
        return self._lecture_id
    
class ProfessorFormDto:
    def __init__(self, name, major, email):
        self._name = name
        self._major = major
        self._email = email
    
    @property
    def name(self):
        return self._name
    
    @property
    def major(self):
        return self._major
    
    @property
    def email(self):
        return self._email
    
class LectureFormDto:
    def __init__(self, professor_id, course_id, day, start_time):
        self._professor_id = professor_id
        self._course_id = course_id
        self._day = day
        self._start_time = start_time
    
    @property
    def professor_id(self):
        return self._professor_id
    
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def day(self):
        return self._day

    @property
    def start_time(self):
        return self._start_time
