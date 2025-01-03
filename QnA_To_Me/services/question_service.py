from models.question import QuestionDB

class QuestionService:
    def __init__(self):
        self.question_db = QuestionDB()
        
    def get_all(self):
        return [
        {
            'id': s[0],
            'contents': s[1],
            'category': s[2],
            'create_date': s[3]
        }
        for s in self.question_db.get_all()
    ]

    def add(self, question):
        self.check_duplication(question)
        return self.question_db.add(question)
        
    def check_duplication(self, question):
        results = self.question_db.select_by_contents(question)
        for c in results:
            if c[1] == question.contents:
                raise Exception('이미 등록된 질문입니다.')