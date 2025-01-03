from models.answer import AnswerDB

class AnswerService:
    def __init__(self):
        self.answer_db = AnswerDB()
        
    def get_all(self):
        return [
        {
            'user_name': s[0],
            'question_contents': s[1],
            'answer_contents': s[2],
            'answer_date': s[3]
        }
        for s in self.answer_db.get_all()
        ]
        
    def get_users(self):
        return [
            {
                'id': s[0],
                'name': s[1],
                'email': s[2],
                'join_date': s[3]
            }
            for s in self.answer_db.get_users()
        ]
        
    def get_user_by_name(self, name):
        return [
            {
                'id': s[0],
                'name': s[1],
                'email': s[2],
                'join_date': s[3]
            }
            for s in self.answer_db.get_user_by_name(name)
        ]
    
    def get_questions(self):
        return [
            {
                'id': s[0],
                'contents': s[1],
                'category': s[2],
                'create_date': s[3]
            }
            for s in self.answer_db.get_questions()
        ]
    
    def add(self, answer):
        return self.answer_db.add(answer)

    def delete(self, answer_id):
        return self.answer_db.delete(answer_id)
    
    # def edit(self, answer):
    #     return self.answer_db.edit(answer)  