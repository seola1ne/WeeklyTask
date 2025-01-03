from flask import Flask 
from controllers.user_controller import user_blueprint
from controllers.question_controller import question_blueprint
from controllers.answer_controller import answer_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(question_blueprint)
app.register_blueprint(answer_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

# 해야 할 것
# MVC패턴에 맞춰서 html 수정
# answer delete
# answer edit 