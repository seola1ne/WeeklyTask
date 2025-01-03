class UserFormDto:
    def __init__(self, name, email, join_date):
        self._name = name
        self._email = email
        self._join_date = join_date
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def join_date(self):
        return self._join_date


class QuestionFormDto:
    def __init__(self, contents, category, create_date):
        self._contents = contents
        self._category = category
        self._create_date = create_date
    
    @property
    def contents(self):
        return self._contents
    
    @property
    def category(self):
        return self._category
    
    @property
    def create_date(self):
        return self._create_date
    

class AnswerFormDto:
    def __init__(self, answer_contents, answer_date, user_id, question_id):
        self._answer_contents = answer_contents
        self._answer_date = answer_date
        self._user_id = user_id
        self._question_id = question_id
    
    @property
    def answer_contents(self):
        return self._answer_contents
    
    @property
    def answer_date(self):
        return self._answer_date
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def question_id(self):
        return self._question_id