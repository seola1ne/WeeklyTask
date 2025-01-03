from flask import render_template, request, redirect, url_for, Blueprint

from services.question_service import QuestionService
from util.dto import QuestionFormDto

question_blueprint = Blueprint('question', __name__)
question_service = QuestionService()

@question_blueprint.route('/')
def index():
    return render_template('index.html')

@question_blueprint.route('/question_management', methods=['GET'])
def gets():
    questions = question_service.get_all()
    return render_template('question_management.html', questions = questions)

@question_blueprint.route('/question_add', methods=['POST'])
def add():
    question_dto = QuestionFormDto(
                                contents=request.form['contents'],
                                category=request.form['category'],
                                create_date=request.form['createDate'],
    )
    question_service.add(question_dto)
    print(question_dto)
    return redirect(url_for('question.gets'))