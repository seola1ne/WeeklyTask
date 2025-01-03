from flask import render_template,redirect,url_for, request, Blueprint, Response, json

from service.professor_service import ProfessorService
from util.dto import ProfessorFormDto

professor_blueprint = Blueprint('professor', __name__)
professor_service = ProfessorService()

@professor_blueprint.route('/')
def index():
    return render_template('index.html')

@professor_blueprint.route('/register_professor', methods=['POST'])
def post():    
    professor_dto = ProfessorFormDto(
                                    name=request.form['name'],
                                    major=request.form['major'],
                                    email=request.form['email'],
    )
    professor_service.add_professor(professor_dto)
    return redirect(url_for('professor.gets'))

@professor_blueprint.route('/professor_management', methods=['GET'])
def gets():
    professors = professor_service.get_all_professor()
    return render_template('professor_management.html', professors = professors)

@professor_blueprint.route('/professors', methods=['GET'])
def get_professors():
    students = professor_service.get_all_professor()
    return Response(json.dumps(students, ensure_ascii=False), mimetype='application/json; charset=utf-8')

@professor_blueprint.route('/schedule/professor/<int:professor_id>', methods=['GET'])
def get_schedule(professor_id):
    schedule = professor_service.get_schedule_professor(professor_id)
    return Response(json.dumps(schedule, ensure_ascii=False), mimetype='application/json; charset=utf-8')

