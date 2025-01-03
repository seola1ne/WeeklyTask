from flask import render_template, request, redirect, url_for, Blueprint

from services.professor_service import ProfessorService
from util.dto import ProfessorFormDto

professor_blueprint = Blueprint('professor', __name__)
professor_service = ProfessorService()

@professor_blueprint.route('/')
def index():
    return render_template('index.html')

@professor_blueprint.route('/professor_management', methods=['GET'])
def gets():
    if request.method == 'GET':
        professors = professor_service.get_all()
        return render_template('professor_management.html', professors = professors)

@professor_blueprint.route('/register_professor', methods=['POST'])
def add():
    professor_dto = ProfessorFormDto(
                                    name = request.form['name'],
                                    major = request.form['major'],
                                    email = request.form['email'],
    )
    professor_service.add(professor_dto)
    return redirect(url_for('professor.gets'))