from models.user import UserDB

class UserService:
    def __init__(self):
        self.user_db = UserDB()
        
    def get_all(self):
        return [
            {
                'id': s[0],
                'name': s[1],
                'email': s[2],
                'join_date': s[3]
            }
            for s in self.user_db.get_all()
        ]
        
    def add(self, user):
        self.check_duplication(user)
        return self.user_db.add(user)
        
    def check_duplication(self, user):
        results = self.user_db.select_by_email(user)
        for c in results:
            if c[2] == user.email:
                raise Exception('이미 등록된 사용자입니다.')