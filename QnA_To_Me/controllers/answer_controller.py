from flask import render_template, request, redirect, url_for, Blueprint

from services.answer_service import AnswerService
from util.dto import AnswerFormDto

answer_blueprint = Blueprint('answer', __name__)
answer_service = AnswerService()

@answer_blueprint.route('/')
def index():
    return render_template('index.html')

@answer_blueprint.route('/answer_list', methods=['GET'])
def gets():
    answers = answer_service.get_all()
    return render_template('answer_list.html', answers = answers)

@answer_blueprint.route('/answer_add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        questions = answer_service.get_questions()
        return render_template('answer_add.html', questions = questions)
    
    elif request.method == 'POST':
        user_name = request.form['userName']
        users = answer_service.get_user_by_name(user_name)
        if users:
            user = users[0] 
        else:
            return redirect(url_for('index.html', error='사용자가 없습니다.'))
        
        print("user", user)
        answer_dto = AnswerFormDto(
                answer_contents = request.form['answerContents'],
                answer_date = request.form['answerDate'],
                user_id = user['id'],
                question_id = int(request.form['questionId'])
        )
        print(answer_dto)
        answer_service.add(answer_dto)        
        return redirect(url_for('answer.gets'))


@answer_blueprint.route('/answer_edit', methods=['POST'])
def edit():
    return redirect(url_for('answer.gets'))

@answer_blueprint.route('/delete_answer', methods=['POST'])
def delete():
    answer_id = int(request.form['answer_id']),
    print(answer_id)
    answer_service.delete(answer_id) 
    return redirect(url_for('answer.gets'))